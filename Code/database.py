#!/usr/bin/env python
# coding: utf-8

# In[4]:

# hey this file is just for basic set up of a database, your .env file should have the proper credientials to log into your own postgres database

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DATABASE_USERNAME = os.environ["DATABASE_USERNAME"]
DATABASE_PASSWORD = os.environ["DATABASE_PASSWORD"]
DATABASE_HOST = os.environ["DATABASE_HOST"]
DATABASE_PORT = os.environ["DATABASE_PORT"]
DATABASE_DATABASE = os.environ["DATABASE_DATABASE"]

SQLALCHEMY_DATABASE_URL = f"postgresql://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)


# In[5]:


engine.connect()


# In[ ]:
