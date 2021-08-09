import pandas as pd

# file_object = pd.ExcelFile('WZPsGesamt.xlsx')
# print(file_object.sheet_names)

# Load sheets with desired columns
diameter_class = pd.read_excel(
    'WZPsGesamt.xlsx',
    sheet_name='durchmesserklassen_richtig',
    usecols=['Plot', 'cluster_4_5_neu', 'Stand', 'Transect'])
diameter_class.set_index('Plot')

tracks = pd.read_excel('WZPsGesamt.xlsx', sheet_name='site', usecols=['Plot', 'tracks_total'])
tracks.set_index('Plot')

# tracks['cluster'] = [row['diameter_class[cluster_4_5_neu]] '
#                         'if (row['diameter_class[cluster_4_5_neu'] == row['Plot']') else 0 for index, row in tracks.iterrows()]


