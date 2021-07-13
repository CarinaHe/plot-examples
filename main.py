## Ausarbeitung Masterthesis Samothraki Mai
## BHD-Klassen verteilung data + plot

# import matplotlib.pyplot as plt
# import numpy as np
import pandas as pd



dmkl=pd.read_excel('WZPsGesamt.xlsx', sheet_name='durchmesserklassen_richtig', usecols=['Plot', 'cluster_4_5_neu', 'Stand', 'Transect'])

tracks = pd.read_excel('WZPsGesamt.xlsx', sheet_name='site', usecols=['Plot', 'tracks_total'])

print(dmkl.columns)