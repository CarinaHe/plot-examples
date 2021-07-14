import pandas as pd

# Watch out to use the right decimal separator!
data = pd.read_csv("dmv.csv", delimiter=",", decimal=",", usecols=['ID', 'Klasse', 'Anz_lebend'])
new_frame = pd.DataFrame(columns=['ID', 'Klasse', 'Anz_lebend'])

for i in range(1, 21):
    a = data.loc[data['Klasse'] == i, 'Anz_lebend'].sum()
    new_frame = new_frame.append({'ID': i, 'Klasse': i, 'Anz_lebend': a}, ignore_index=True)

new_frame.to_csv('test.csv')
