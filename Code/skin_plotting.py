import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import os

# read data
df=pd.read_csv(os.path.join('Data','Skin_wreviews_cleaned.csv'))

# Skintone = df.groupby('Skin_Tone')
# st_size=Skintone.size()

df.groupby(['Skin_Tone']).size().plot.pie()