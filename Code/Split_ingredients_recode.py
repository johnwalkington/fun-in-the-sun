#!/usr/bin/env python
# coding: utf-8

# In[6]:


import os
import pandas as pd


# In[7]:


IN_PATH = os.path.join("Data", "Product_Info_Sunscreen.csv")
OUT_PATH = os.path.join("Data", "Split_Recode_Product_Info.csv")
df = pd.read_csv(IN_PATH)


# In[4]:


df['Ingredients'] = df['Ingredients'].str.split(',')


filter_ingredients = [" Zinc Oxide", " zinc oxide", " titanium dioxide",  " bis-ethylhexyloxyphenol methoxyphenyl triazine",  " Bis-Ethylhexyloxyphenol Methoxyphenyl Triazine",
 " Titanium Dioxide", " Butyl Methoxydibenzoylmethane", " butyl methoxydibenzoylmethane", " Diethylamino Hydroxybenzoyl Hexyl Benzoate",
 " diethylamino hydroxybenzoyl hexyl benzoate", " Diethylhexyl Butamido Triazone", " diethylhexyl butamido triazone", " Disodium Phenyl Dibenzimidazole Tetrasulfonate",
 " disodium phenyl dibenzimidazole tetrasulfonate", " Drometrizole Trisiloxane", " drometrizole trisiloxane", " Ethylhexyl Methoxycinnamate", 
 " ethylhexyl methoxycinnamate", " Ethylhexyl Salicylate", "ethylhexyl salicylate", " Ethylhexyl Triazone", " ethylhexyl triazone",
 " Homosalate", " homosalate", " Isoamyl p-Methoxycinnamate", " isoamyl p-methoxycinnamate", " Methylene Bis-Benzotriazolyl Tetramethylbutylphenol",
 " methylene bis-benzotriazolyl tetramethylbutylphenol", " Octocrylene", " octocrylene", " Phenylbenzimidazole Sulfonic Acid", " phenylbenzimidazole sulfonic acid",
 " Polysilicone-15", " polysilicone-15", " Sodium Phenylbenzimidazole Sulfonate", " sodium phenylbenzimidazole sulfonate", 
 " Terephthalylidene Dicamphor Sulfonic Acid", " terephthalylidene dicamphor sulfonic acid", " Tris-Biphenyl Triazine", " tris-biphenyl triazine",
 " titanium oxide", " low temperature fired zinc oxide", " fine particle titanium oxide", " Zinc Oxide (CI 77947)", " Titanium Dioxide (CI 77891)", " Avobenzone"]

for i in range(len(filter_ingredients)):
    filter_ingredients[i] = filter_ingredients[i] 

def isInList(lists):
    s = []
    for [x] in lists:
        if ([x] in filter_ingredients):
            s.append([x])
    return s

df['SunFilter_Ingredients'] = df.apply(lambda x: isInList(x['Ingredients']),axis=1)

df = df[df['SunFilter_Ingredients'].map(lambda d: len(d)) > 0]

active_ingredients_list = []




#df['SunFilter_Ingredients'] = df['SunFilter_Ingredients'].str.replace(' POLYSILICONE-15','Parsol SLX')

#def replace_values(list_to_replace, item_to_replace, item_to_replace_with):
    #return [item_to_replace_with if item == item_to_replace else item for item in list_to_replace]
#replaced_list = replace_values(df['SunFilter_Ingredients'], ' POLYSILICONE-15', 'Parsol SLX')




# df["SunFilter_Ingregients"] = df["Ingredients"].map(lambda x: "Zinc Oxide" if " Zinc Oxide" in x 
# 	else "Tinosorb S" if " Bis-Ethylhexyloxyphenol Methoxyphenyl Triazine" in x 
# 	else "Titanium Dioxide" if " Titanium Dioxide" in x else "")




write_df1 = df.to_csv(os.path.join(OUT_PATH))




# In[ ]:




