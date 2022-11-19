import pandas as pd
from geopy import distance
import numpy as np
import time

def main():
    pass

def import_data():
    df = pd.read_csv('laposte_hexasmal.csv', sep=';')
    return df

def distance_calculate(org_lat, org_long, dest_lat, dest_long):
    org_lat, org_long, dest_lat, dest_long = map(np.radians, [org_lat, org_long, dest_lat, dest_long])

    new_lat = dest_lat - org_lat
    new_long = dest_long - org_long

    haversine = np.sin(new_lat * 0.5) ** 2 + np.cos(org_lat) * np.cos(dest_lat) * np.sin(new_long * 0.5) ** 2

    return 2 * np.arcsin(np.sqrt(haversine)) * 6371
    #return org_lat + org_long + dest_lat + dest_long


if __name__ == '__main__':
    main()
    data = import_data()
    coordinates = data["coordonnees_gps"].loc[data['Nom_commune'] == "PARIS 01"]

    coordinates2 = data["coordonnees_gps"].loc[data['Nom_commune'] == "ST PHILIPPE"].values[0].split(',')

    print(tuple(data["coordonnees_gps"].values[0].split(',')))
    data = data[data['coordonnees_gps'].notna()]
    data["Origin"] = coordinates.values[0]
    data[['Origin_lat', 'Origin_long']] = data['Origin'].str.split(',', n=1, expand=True)
    
    start = time.time()
    print(coordinates.values[0])
    data[['lat2', 'long2']] = data['coordonnees_gps'].str.split(',', n=1, expand=True)
    data.drop("coordonnees_gps", axis=1)
    data["Distance"] =  distance_calculate(data["Origin_lat"].astype(float), data['Origin_long'].astype(float), data['lat2'].astype(float), data['long2'].astype(float))
    print(time.time() - start)
    print(data)