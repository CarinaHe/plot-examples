
import pandas as pd
from matplotlib import pyplot

# Watch out to use the right decimal separator!
data = pd.read_csv(
    "dmv.csv",
    delimiter=",",
    decimal=",",
    usecols=['ID', 'Klasse', 'Anz_lebend', 'Anz_tot'])

new_dataframe = pd.DataFrame(columns=['ID', 'Klasse', 'Anz_lebend', 'Anz_tot'])
for i in range(1, 21):
    new_dataframe = new_dataframe.append(
        {'ID': i,
         'Klasse': i,
         'Anz_lebend': data.loc[data['Klasse'] == i, 'Anz_lebend'].sum(),
         'Anz_tot': data.loc[data['Klasse'] == i, 'Anz_tot'].sum()},
        ignore_index=True)
new_dataframe.to_csv('test.csv')

# the whole thing in one line:
# new_data = data.groupby(['Klasse'])['Anz_lebend'].sum()


# Plot with Pandas
new_dataframe.set_index('Klasse')
plot = new_dataframe.plot.bar(y=['Anz_lebend', 'Anz_tot'])
plot.figure.savefig('test.pdf')

# Plot with matplotlib
pyplot.figure(figsize=(5, 3))
# Changing line and marker properties
pyplot.bar(new_dataframe.Klasse, new_dataframe.Anz_lebend, color="blue", label="BHD-Verteilung")
pyplot.title("DBH-classes")
pyplot.legend(prop={"size": 12})
pyplot.show()
pyplot.savefig('test_m.pdf')
