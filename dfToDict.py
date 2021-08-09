# not working!!!! try to get data from a dataframe to a dictionary !!! not working !!!
import pandas as pd
# Watch out to use the right decimal separator!
data = pd.read_csv(
    "dmv.csv",
    delimiter=",",
    decimal=",",
    usecols=['Klasse', 'Anz_lebend'])


new_data = data.groupby(['Klasse'])['Anz_lebend'].sum()

#new_dict = new_data.to_dict
print(new_data.to_dict)
#new_dataframe.to_csv('test.csv')
#new_dict=dict(data.values)

#print(new_dict.items)
