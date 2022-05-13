#!/usr/bin/env python
# coding: utf-8

# In[78]:


# imports

import pandas as pd
import numpy as np
import nltk
from langdetect import detect
import seaborn as sns
import matplotlib.pyplot as plt
from textblob import TextBlob
import os
from sklearn.metrics import classification_report, confusion_matrix


# In[ ]:


IN_PATH = os.path.join("Data", "Sunscreen_Comments_Full.csv")


# In[79]:


# reading in data
comm = pd.read_csv(IN_PATH).iloc[:, 1:]
comm.Comment = comm.Comment.apply(lambda x: x[1:-1])


# In[80]:


# defining a function that filters out non-english comments
def get_english(c):
    try:
        return detect(c) == "en"
    except:
        return False


# In[81]:


# getting the English comments
new_comm = comm[comm.Comment.apply(lambda x: get_english(x))]


# In[82]:


new_comm = new_comm.reset_index().iloc[:, 1:]


# In[83]:


# In[88]:


# creating a function to designate polarity, this time we're only looking at positive and negative comments


def classify(polarity):
    if polarity == 0:
        return "Neutral"
    elif polarity <= 1 and polarity > 0:
        return "Positive"
    else:
        return "Negative"


desig = []
count = 0

# This assigns polarity to each comment
for comment in new_comm["Comment"]:
    try:
        if detect(comment) == "en":
            pol = TextBlob(comment).sentiment.polarity
            desig.append(classify(pol))
        else:
            desig.append("Unknown")
    except:
        desig.append("Unknown")
        continue
    finally:
        count += 1

# assigns sentiment to the polarity value
new_comm["Sentiment"] = desig


# In[89]:


# now lets define a dummy variable assinging a value to a rating,
# yesstyle uses star ratings, just so it's clear where these values come from


def rating_to_dummy(rating):
    if 100 >= rating > 60:
        return 1
    elif 40 >= rating >= 0:
        return 0
    else:
        return "Delete"


# In[90]:


# let's use this function to get rating dummies for products, using star value as the "true" sentiment of a review
new_comm["Actual_Sentiment"] = new_comm.Rating.apply(lambda x: rating_to_dummy(x))


# In[91]:


# lets create a function that assigns a dummy to sentiment that we got from the classify function, predicted sentiment
def pred_sentiment_to_dummy(sent):
    if sent == "Positive":
        return 1
    if sent == "Negative":
        return 0


# In[95]:


# uses the above function to assign dummies
new_comm["Pred_Sentiment"] = new_comm.Sentiment.apply(
    lambda x: pred_sentiment_to_dummy(x)
)


# In[98]:


# filter out na values
new_comm = new_comm[new_comm.Pred_Sentiment.notna()]
new_comm = new_comm[new_comm.Actual_Sentiment.notna()]


# In[99]:


new_comm = new_comm[new_comm.Actual_Sentiment != "Delete"]


# In[100]:


# In[101]:


# converting predicted sentiment to integer
new_comm["Pred_Sentiment"] = new_comm.Pred_Sentiment.apply(lambda x: int(x))


# In[102]:


# setting up the prediction comparison
y_true, y_pred = new_comm["Actual_Sentiment"], new_comm["Pred_Sentiment"]


# In[103]:


y_pred = y_pred.astype(object)


# In[104]:


# creating a confidence test to see how close we were
conf_test = pd.DataFrame([y_true, y_pred]).transpose()


# In[105]:


# In[106]:


# creating a confusion matrix to vizualise the accuracy of our our test.
cm = confusion_matrix(conf_test.Actual_Sentiment, conf_test.Pred_Sentiment)
plt.figure(figsize=(5, 5))
sns.heatmap(
    cm,
    cmap="Blues",
    linecolor="black",
    linewidth=1,
    annot=True,
    fmt="",
    xticklabels=["Bad Reviews", "Good Reviews"],
    yticklabels=["Bad Reviews", "Good Reviews"],
)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("Plots/confusion.png")
plt.show()


# In[ ]:


# In[ ]:
