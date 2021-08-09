import pandas as pd

data = pd.read_csv("dmv.csv", delimiter=",", usecols=['ID', 'Klasse', 'Anz_lebend'])

# Adding new columns to dataframe to split counts of the different classes
for i in range(10):
    data[i] = [row['Anz_lebend'] if (row['Klasse'] == i) else 0 for index, row in data.iterrows()]

data.to_csv('test.csv')
