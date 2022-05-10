import os
import streamlit as st
import pandas as pd
import numpy as np

product_path = os.path.join("Data", "Product_Info_Sunscreen.csv")

df = pd.read_csv(product_path)

prices_dirty = df['Price'].tolist()

prices = []
for item in prices_dirty:
    prices += [float(item[3:len(item)])]

prices = pd.Series(prices)

hist_values = np.histogram(
    prices, bins=20, range=(0,120))[0]

st.bar_chart(hist_values)
