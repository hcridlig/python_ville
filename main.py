import pandas as pd
from geopy import distance
import numpy as np
import time
import sort

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


def sort_data(arr):
    
    n = len(arr)
    swapped = False
    
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j][6] > arr[j + 1][6]:
                swapped = True
                arr[[j, j+1]] = arr[[j+1, j]]
                
        if swapped == False:
            break
    
    return pd.DataFrame(arr, columns=['Code_commune_INSEE', 'Nom_commune', 'Code_postal', 'Ligne_5', 'Libellé_d_acheminement', 'coordonnees_gps', 'Distance',])

        



if __name__ == '__main__':
    main()
    data = import_data()
    coordinates = data["coordonnees_gps"].loc[data['Nom_commune'] == "PARIS 01"]

    #coordinates2 = data["coordonnees_gps"].loc[data['Nom_commune'] == "ST PHILIPPE"].values[0].split(',')

    print(tuple(data["coordonnees_gps"].values[0].split(',')))
    data = data[data['coordonnees_gps'].notna()]
    data["Origin"] = coordinates.values[0]
    data[['Origin_lat', 'Origin_long']] = data['Origin'].str.split(',', n=1, expand=True)
    data = data.drop("Origin", axis=1)
    
    start = time.time()
    print(coordinates.values[0])
    data[['lat2', 'long2']] = data['coordonnees_gps'].str.split(',', n=1, expand=True)
    data.drop("coordonnees_gps", axis=1)
    data["Distance"] =  distance_calculate(data["Origin_lat"].astype(float), data['Origin_long'].astype(float), data['lat2'].astype(float), data['long2'].astype(float))
    print(time.time() - start)
    print(data)
    
    data = data.drop("Origin_lat", axis=1)
    data = data.drop("Origin_long", axis=1)
    data = data.drop("lat2", axis=1)
    data = data.drop("long2", axis=1)
    
    start = time.time()
    data = sort_data(data.to_numpy())
    print(data)
    print(time.time() - start)
    