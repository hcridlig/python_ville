import pandas as pd
from geopy import distance

def main():
    pass

def import_data():
    df = pd.read_csv('laposte_hexasmal.csv', sep=';')
    return df

#def distance(p1x, p1y, p2x, p2y):
    #return round((((p1x - p2x) ** 2 + (p1y - p2y) ** 2) ** 0.5)*100, 2)


if __name__ == '__main__':
    #print(data["coordonnees_gps"].loc[data['Nom_commune'] == city])
    main()
    data = import_data()
    #city = str(input("Ville de départ : "))
    coordinates = data["coordonnees_gps"].loc[data['Nom_commune'] == "PARIS 01"]
    
    coordinates2 = data["coordonnees_gps"].loc[data['Nom_commune'] == "ST PHILIPPE"].values[0].split(',')

    #print(distance(float(coordinates[0]), float(coordinates[1]), float(coordinates2[0]), float(coordinates2[1])))
    #print(distance.distance(tuple(coordinates), tuple(coordinates2)))

    #print(str(coordinates).split(",")[1])
    #data = data.reset_index()
    #for row in data.iterrows():
        #print(row[1]["Nom_commune"] + row[1]["coordonnees_gps"])
    
    #data.insert(6, "Distance", 0)
    #print(data)
    print(tuple(data["coordonnees_gps"].values[0].split(',')))
    #data["Distance"].replace(0, distance.distance(tuple(coordinates), ), inplace=True)
    #data["Distance"] = distance.distance(tuple(coordinates), tuple(data["coordonnees_gps"].values[0].split(',')))
    #data["Distance"] = data.Nom_commune.apply(lambda x: distance.distance(tuple(coordinates), tuple(data["coordonnees_gps"].loc[data['Nom_commune'] == x].values[0].split(','))))
    data = data[data['coordonnees_gps'].notna()]
    
    #data["Distance"] = str(data.applymap(distance.distance, args=((tuple(coordinates)), (tuple(coordinates2)))))
    data["Distance"] = data.apply(lambda x: distance.distance(tuple(coordinates), tuple(x["coordonnees_gps"].split(','))), axis=1)
    print(data)