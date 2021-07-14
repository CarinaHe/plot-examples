import pandas as pd

file_object = pd.ExcelFile('WZPsGesamt.xlsx')
print(file_object.sheet_names)

# Load sheets with desired columns
diameter_class = pd.read_excel(
    'WZPsGesamt.xlsx',
    sheet_name='durchmesserklassen_richtig',
    usecols=['Plot', 'cluster_4_5_neu', 'Stand', 'Transect'])
print(diameter_class.columns)

tracks = pd.read_excel('WZPsGesamt.xlsx', sheet_name='site', usecols=['Plot', 'tracks_total'])
