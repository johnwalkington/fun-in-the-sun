#!/usr/bin/env python
# coding: utf-8

# In[25]:


#imports
from textblob import TextBlob
import pandas as pd
from langdetect import detect
import pandas as pd
import numpy as np
import nltk
import re
import os
import matplotlib.pyplot as plt
import seaborn as sns


# In[21]:


#defining what data we want to analyze, this is the dataset with all of the comments
IN_PATH = os.path.join("Data", "Sunscreen_Comments_Full.csv")


# In[22]:


#First, we define a function which converts the polarity number to an actual understandable value

def classify(polarity): 
    if polarity == 0: 
        return 'Neutral'
    elif polarity <= 1 and polarity > .5:
        return 'Very Postive'
    elif polarity <= .5 and polarity > 0: 
        return 'Positive'
    elif polarity < 0 and polarity >= -.5:
        return 'Negative'
    else: 
        return 'Very Negative'
    
#defining the dataframe, and helping nltk understand what it needs to be parsing through
comm = pd.read_csv(IN_PATH).iloc[:, 1:]
comm.Comment = comm.Comment.apply(lambda x: str(x)[1:-1])

#nltk will look at the comment, and disignate a polarity value to it, spitting it out as sentiment.
desig = []
count = 0

for comment in comm['Comment']:
    try: 
        if detect(comment) == 'en':
            pol = TextBlob(comment).sentiment.polarity
            desig.append(classify(pol))
        else: 
            desig.append('Unknown')
    except: 
        desig.append('Unknown')
        continue
    finally: 
        count += 1

comm['Sentiment'] = desig


# In[26]:


#plotting every single comment, based on sentiment. 

sent_counts = comm.Sentiment.value_counts()
plt.figure(figsize=(10,5))
sns.barplot(sent_counts.index, sent_counts.values, alpha=0.8)
plt.title('Review Counts Based on Polarity')
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Sentiment', fontsize=12)
plt.savefig("Plots/polarity_freq.png")
plt.show()


# In[ ]:




