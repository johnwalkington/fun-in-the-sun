#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
import dataframe_image as dfi


# In[2]:

# let's create a table that displays the frequency of sunfilters

IN_PATH = os.path.join("Data", "Fitered_ingredients.csv")
OUT_PATH = os.path.join("Data", "Filter_Freq.csv")
df = pd.read_csv(IN_PATH)
di = {}
for ing_list in df.Filtered_Ingredients:
    for ing in ing_list.strip("[").strip("]").strip('"').strip("'").split(","):
        ing = ing.strip("'").strip().strip("'").strip()
        ing = str(ing)
        if ing not in di.keys():
            di[ing] = 1
        else:
            di[ing] += 1
    df = pd.DataFrame.from_dict(di, orient="index", columns=["Count"])
    df = df.reset_index()
    df.columns = ["Ingredient", "Count"]
    df = df.sort_values("Count", ascending=False).head(15)
    df = df.reset_index().iloc[:, 1:]
    df


# In[16]:

# let's export the table we created as a png for the README

df_styled = df.style.background_gradient()  # adding a gradient based on values in cell
dfi.export(df_styled, "Plots/filter_freq.png")


# In[ ]:
