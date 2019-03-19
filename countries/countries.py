import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file = 'countries.csv'
df = pd.read_csv(file)

cols_to_conv= [
       'Pop. Density (per sq. mi.)', 'Coastline (coast/area ratio)',
       'Net migration', 'Infant mortality (per 1000 births)',
        'Literacy (%)', 'Phones (per 1000)', 'Arable (%)',
       'Crops (%)', 'Other (%)', 'Birthrate', 'Deathrate',
       'Agriculture', 'Industry', 'Service']

df[cols_to_conv]= (df[cols_to_conv].replace(',', '.', regex=True).astype(float))
df=df.rename(columns={'Agriculture':'Agriculture (%)','Industry':'Industry (%)', 'Service':'Service (%)'})


countries= df.iloc[0,0]
print(countries)
