#!/usr/bin/env python
# coding: utf-8


#importing necessary packages and specifying paths 
import os
import pandas as pd
from sqlalchemy.types import String, Date, Numeric

#reminder that you need to run the database file first, making sure that your .env file has been created with the proper credentials
from database import engine

IN_PATH = os.path.join("Data", "Sunscreen_Comments_Full.csv")
IN_PATH2= os.path.join("Data", "Fitered_Ingredients.csv")

#importing the data we want to upload to the database

df = pd.read_csv(IN_PATH)
df2= pd.read_csv(IN_PATH2)

#this creates the table called 'comment_data' in the datbase. We will use this to later create the reviewer location map, using the variable called countries. 
df.to_sql(
    'comment_data', 
    engine,
    index=False 
)

#this creates the table called 'filtered_sunscreen'. We will use this to later create the map that specifies where sunscreens were manufactured.
df2.to_sql( 
    'filtered_sunscreen',
    engine,
    index=False)

#great so all of the data is uploaded to the database! We will use these two tables in tableau to create two cool map plots which you can find in the readme.
#We used tableau and tableau only to plot the data and create the visualizations, accessing the database to call the exact columns we wanted and using count functions to get values.






