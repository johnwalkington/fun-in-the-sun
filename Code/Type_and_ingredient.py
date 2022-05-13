#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import csv
import os
import dataframe_image as dfi


# Read data for ingredient
df_ingred = pd.read_csv(os.path.join("Data", "Fitered_ingredients.csv"))
df_ingred = df_ingred.reset_index()[["Catalog No.", "Filtered_Ingredients"]]
df_ingred = df_ingred.rename(
    columns={
        "Catalog No.": "Product_ID",
        "Filtered_Ingredients": "Filtered_Ingredients",
    }
)
df_ingred


# Read data for skin type
df_type = pd.read_csv(os.path.join("Data", "Skin_wreviews_cleaned.csv"))
df_type = df_type.reset_index()[["Product_ID", "Skin_Type"]]
df_type


# Doing inner join
inner_join_df = pd.merge(df_ingred, df_type, on="Product_ID", how="inner")
inner_join_df


# Combination type
Comb_df = inner_join_df[inner_join_df["Skin_Type"] == "Combination"].reset_index()
Comb_df = Comb_df.iloc[:, 1:]

# 1794 rows (53.5%)


# Dry type
Dry_df = inner_join_df[inner_join_df["Skin_Type"] == "Dry"].reset_index()
Dry_df = Dry_df.iloc[:, 1:]

# 697 rows (20.4%)


# Oily type
Oily_df = inner_join_df[inner_join_df["Skin_Type"] == "Oily"].reset_index()
Oily_df = Oily_df.iloc[:, 1:]

# 486 rows (14.2%)


# Normal type
Norm_df = inner_join_df[inner_join_df["Skin_Type"] == "Normal"].reset_index()
Norm_df = Norm_df.iloc[:, 1:]

# 394 rows (11.9%)


# In[ ]:


# In[2]:


# Finding top 10 ingredients for Combination type skin


# In[3]:


Comb_df = Comb_df.drop_duplicates("Product_ID")


# In[4]:


di = {}


# In[5]:


for ing_list in Comb_df.Filtered_Ingredients:
    for ing in ing_list.strip("[").strip("]").strip('"').strip("'").split(","):
        ing = ing.strip("'").strip().strip("'").strip()
        ing = str(ing)

        if ing not in di.keys():
            di[ing] = 1
        else:
            di[ing] += 1


# In[6]:


df_comb = pd.DataFrame.from_dict(di, orient="index", columns=["Count"])


# In[7]:


df_comb = df_comb.reset_index()
df_comb.columns = ["Ingredient", "Count"]
df_comb = df_comb.sort_values("Count", ascending=False).head(15)


# In[8]:


df_comb = df_comb.reset_index().iloc[:, 1:]
df_comb


# In[ ]:


# In[9]:


# Finding top 10 ingredients for Dry type skin


# In[10]:


Dry_df = Dry_df.drop_duplicates("Product_ID")


# In[11]:


di = {}


# In[12]:


for ing_list in Dry_df.Filtered_Ingredients:
    for ing in ing_list.strip("[").strip("]").strip('"').strip("'").split(","):
        ing = ing.strip("'").strip().strip("'").strip()
        ing = str(ing)

        if ing not in di.keys():
            di[ing] = 1
        else:
            di[ing] += 1


# In[13]:


df_dry = pd.DataFrame.from_dict(di, orient="index", columns=["Count"])


# In[14]:


df_dry = df_dry.reset_index()
df_dry.columns = ["Ingredient", "Count"]
df_dry = df_dry.sort_values("Count", ascending=False).head(15)


# In[15]:


df_dry = df_dry.reset_index().iloc[:, 1:]
df_dry


# In[ ]:


# In[16]:


# Finding top 10 ingredients for Oily type skin


# In[17]:


Oily_df = Oily_df.drop_duplicates("Product_ID")
di = {}
for ing_list in Oily_df.Filtered_Ingredients:
    for ing in ing_list.strip("[").strip("]").strip('"').strip("'").split(","):
        ing = ing.strip("'").strip().strip("'").strip()
        ing = str(ing)

        if ing not in di.keys():
            di[ing] = 1
        else:
            di[ing] += 1
df_oily = pd.DataFrame.from_dict(di, orient="index", columns=["Count"])
df_oily = df_oily.reset_index()
df_oily.columns = ["Ingredient", "Count"]
df_oily = df_oily.sort_values("Count", ascending=False).head(15)
df_oily = df_oily.reset_index().iloc[:, 1:]
df_oily


# In[ ]:


# In[18]:


# Finding top 10 ingredients for Normal type skin


# In[19]:


Norm_df = Norm_df.drop_duplicates("Product_ID")
di = {}
for ing_list in Norm_df.Filtered_Ingredients:
    for ing in ing_list.strip("[").strip("]").strip('"').strip("'").split(","):
        ing = ing.strip("'").strip().strip("'").strip()
        ing = str(ing)

        if ing not in di.keys():
            di[ing] = 1
        else:
            di[ing] += 1
df_norm = pd.DataFrame.from_dict(di, orient="index", columns=["Count"])
df_norm = df_norm.reset_index()
df_norm.columns = ["Ingredient", "Count"]
df_norm = df_norm.sort_values("Count", ascending=False).head(15)
df_norm = df_norm.reset_index().iloc[:, 1:]
df_norm


# In[21]:


# In[20]:


# compare ingredients for all four skin types


# In[22]:


df_list = [df_comb, df_dry, df_oily, df_norm]
df_all = pd.concat(df_list, axis=1, ignore_index=True)
df_all.columns = [
    "Combination",
    "Count",
    "Dry",
    "Count",
    "Oily",
    "Count",
    "Normal",
    "Count",
]
df_all

# export df to image for readme

dfi.export(df_all, "Plots/ingredient_type.png")

#
