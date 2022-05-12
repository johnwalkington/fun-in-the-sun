import os
import pandas as pd

IN_PATH = os.path.join("Data", "Product_Info_Sunscreen.csv")
OUT_PATH = os.path.join("Data", "Split_Recode_Product_Info.csv")

df = pd.read_csv(IN_PATH)

filter_ingredients = df['Ingredients']

ingredient_list = []

for i in range(len(filter_ingredients)):
    row = filter_ingredients[i]
    minilist = row.upper().split(",")
    for item in minilist:
        if item in ingredient_list:
            ingredient_list = ingredient_list
        else:
            ingredient_list += [item.strip()]