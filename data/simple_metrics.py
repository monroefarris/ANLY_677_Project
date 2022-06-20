import pandas as pd 

data = pd.read_csv('objects.csv')

print("THERE ARE " + str(len(data)) + " OBJECTS IN THE DATASET\n")

data = data.groupby('classification').size().reset_index()

print("THE DATASET IS DISTRIBUTED AS FOLLOWS:")
print(data)