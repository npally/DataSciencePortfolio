import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file= 'FastFoodRestaurants.csv'
df= pd.read_csv(file)

most_city = df['city'].value_counts().head(10)
print(most_city)
