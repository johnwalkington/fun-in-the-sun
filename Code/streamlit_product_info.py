import os
import streamlit as st
import pandas as pd

product_path = os.path.join("Data", "Product_Info_Sunscreen.csv")

df = pd.read_csv(product_path)

st.dataframe(df)