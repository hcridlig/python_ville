import pandas as pd
from geopy import distance
import time
import numpy as np

def main():
    pass

def import_data():
    df = pd.read_csv('laposte_hexasmal.csv', sep=';')
    return df

#def distance(p1x, p1y, p2x, p2y):
    #return round((((p1x - p2x) ** 2 + (p1y - p2y) ** 2) ** 0.5)*100, 2)


# function to find the partition position
def partition(array, low, high):

  # choose the rightmost element as pivot
  pivot = array["Distance"].iloc[high]

  # pointer for greater element
  i = low - 1

  # traverse through all elements
  # compare each element with pivot
  for j in range(low, high):
    if array["Distance"].iloc[j] <= pivot:
      # if element smaller than pivot is found
      # swap it with the greater element pointed by i
      i = i + 1

      # swapping element at i with element at j
      (array.iloc[i], array.iloc[j]) = (array.iloc[j], array.iloc[i])

  # swap the pivot element with the greater element specified by i
  (array.iloc[i + 1], array.iloc[high]) = (array.iloc[high], array.iloc[i + 1])

  # return the position from where partition is done
  return i + 1

# function to perform quicksort
def quickSort(array, low, high):
  if low < high:

    # find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
    pi = partition(array, low, high)

    # recursive call on the left of pivot
    quickSort(array, low, pi - 1)

    # recursive call on the right of pivot
    quickSort(array, pi + 1, high)




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
    start = time.time()
    #data["Distance"] = data.apply(lambda x: distance.distance(tuple(coordinates), tuple(x["coordonnees_gps"].split(','))), axis=1)
    #data["Distance"] = np.vectorize(distance.distance)(tuple(coordinates), tuple(data["coordonnees_gps"]))
    #data["Distance"] = list(map(distance.distance, coordinates, data["coordonnees_gps"]))
    data["Distance"] = distance.distance(tuple(coordinates), tuple(data["coordonnees_gps"].values[0].split(',')))
    
    #print(tuple(data["coordonnees_gps"][3].split(',')))
    #condition = []
    #print(tuple	(coordinates))
    #output = [distance.distance(tuple(coordinates), tuple(data["coordonnees_gps"]))]
    #data["Distance"] = np.select(condition, output)
    print(data["Distance"])
    print(time.time() - start)
"""
    start = time.time()
    #quickSort(data, 0, len(data) - 1)
    data = data.sort_values(by=['Distance'])
    keys = data._get_label_or_level_values("Distance", axis=0)
    if None is not None:
                # error: List comprehension has incompatible type List[Series];
                # expected List[ndarray]
                keys = [
                    Series(k, name=name)  # type: ignore[misc]
                    for (k, name) in zip(keys, by)
                ]

                indexer = lexsort_indexer(keys, orders=ascending, na_position=na_position, key=key)
    print(f"Fin quicksort:",time.time() - start)
    print(data.head(100))"""