#!/usr/bin/env python
# coding: utf-8

# In[1]:


from re import A
import os
import pandas as pd
from sqlalchemy.types import String, Date, Numeric

from database import engine


# In[2]:

IN_PATH = os.path.join("Data", "Fitered_ingredients.csv")


df = pd.read_csv(IN_PATH)


# In[3]:


df.to_sql(
    'filtered_sunscreen', 
    engine,
    index=False # Not copying over the index
)


# In[ ]:




