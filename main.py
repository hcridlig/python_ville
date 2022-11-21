import pandas as pd
import numpy as np
import time
from sqlalchemy import create_engine
import math

def main():
    pass

def import_data():
    df = pd.read_csv('laposte_hexasmal.csv', sep=';')
    return df

def distance_calculate(org_lat, org_long, dest_lat, dest_long):
    org_lat, org_long, dest_lat, dest_long = map(np.radians, [org_lat, org_long, dest_lat, dest_long])

    new_long = dest_long - org_long

    geodesique = np.arccos(np.sin(org_lat)*np.sin(dest_lat)+np.cos(org_lat)*np.cos(dest_lat)*np.cos(new_long))

    return geodesique * 6378.137


if __name__ == '__main__':
    main()
    data = import_data()
    #city = str(input("Ville de départ : "))
    coordinates = data["coordonnees_gps"].loc[data['Nom_commune'] == "PARIS 01"]


    print(tuple(data["coordonnees_gps"].values[0].split(',')))
    data = data[data['coordonnees_gps'].notna()]
    data["Origin"] = coordinates.values[0]
    data[['Origin_lat', 'Origin_long']] = data['Origin'].str.split(',', n=1, expand=True)
    data.drop(columns=['Origin'], axis=1)
    
    start = time.time()
    print(coordinates.values[0])
    data[['lat2', 'long2']] = data['coordonnees_gps'].str.split(',', n=1, expand=True)
    data.drop("coordonnees_gps", axis=1)
    data["Distance"] =  distance_calculate(data["Origin_lat"].astype(float), data['Origin_long'].astype(float), data['lat2'].astype(float), data['long2'].astype(float))
    print(f"Time for ditance ",time.time() - start)
    print(data)

    #Sort dataframe by distance
    start = time.time()
    engine = create_engine('sqlite://', echo=False)
    data.to_sql('data', con=engine)
    data = pd.read_sql_query("SELECT * FROM data ORDER BY Distance", engine)
    print(f"Time for sort ", time.time() - start)
    

    # Drop first row
    data.drop(index=data.index[0], axis=0, inplace=True)
    print(data)
    print(f"{' '*15}min : {round(data['Distance'].min(), 2)} km pour {data['Nom_commune'].loc[data['Distance'] == data['Distance'].min()].values[0]} ({data['Code_postal'].loc[data['Distance'] == data['Distance'].min()].values[0]})")
    print(f"{' '*2}Premier quartile : {round(data['Distance'].iloc[math.ceil(len(data)*0.25)], 2)} km pour {data['Nom_commune'].iloc[math.ceil(len(data)*0.25)]} ({data['Code_postal'].iloc[math.ceil(len(data)*0.25)]})")
    print(f"{' '*11}Mediane : {round(data['Distance'].iloc[math.ceil(len(data)*0.5)], 2)} km pour {data['Nom_commune'].iloc[math.ceil(len(data)*0.5)]} ({data['Code_postal'].iloc[math.ceil(len(data)*0.5)]})")
    print(f"troisième quartile : {round(data['Distance'].iloc[math.ceil(len(data)*0.75)], 2)} km pour {data['Nom_commune'].iloc[math.ceil(len(data)*0.75)]} ({data['Code_postal'].iloc[math.ceil(len(data)*0.75)]})")
    print(f"{' '*15}max : {round(data['Distance'].max(), 2)} km pour {data['Nom_commune'].loc[data['Distance'] == data['Distance'].max()].values[0]} ({data['Code_postal'].loc[data['Distance'] == data['Distance'].max()].values[0]})")