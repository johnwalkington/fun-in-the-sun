#!/usr/bin/env python
# coding: utf-8

# In[118]:


from wordcloud import WordCloud
import seaborn as sns
import matplotlib.pyplot as plt 
get_ipython().run_line_magic('matplotlib', 'inline')


# In[119]:


import pandas as pd
import numpy as np
import nltk
import re
import os 

IN_PATH = os.path.join("Data", "Sunscreen_Comments_Full.csv")

# from textblob import TextBlob

from nltk.probability import FreqDist
freqdist = FreqDist()

from nltk.stem import WordNetLemmatizer
lemmatize = WordNetLemmatizer()

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

stop = stopwords.words('English')
from langdetect import detect
comm = pd.read_csv(IN_PATH).iloc[:, 1:]
comm.Comment = comm.Comment.apply(lambda x: str(x)[1:-1])

bidict = FreqDist()
tridict = FreqDist()
count = 0
for comment in comm['Comment']:
    try:
        if detect(comment) == 'en':
            sample = comment.lower().split()
            words = [w for w in sample if w not in stop]
            words = word_tokenize(' '.join(words))
            words = [w for w in words if w not in stop]
            words = [re.sub('[^A-Za-z0-9]+', '', w) for w in words]
            words = [w for w in words if w]
            single_words = [lemmatize.lemmatize(w, pos = 'v') for w in words]
            
            for w in single_words:
                freqdist[w] += 1
            
            for item in list(nltk.bigrams(words)): 
                bidict[item] += 1
                
            for item in list(nltk.trigrams(words)): 
                tridict[item] += 1
    except:
        continue
    finally:
        count += 1
        
   


# In[122]:


c_df = pd.DataFrame.from_dict(freqdist, orient='index')
c_df.columns = ['Count']
get_ipython().run_line_magic('matplotlib', 'inline')
c_df = c_df.sort_values('Count', ascending=False).head(30)


# In[123]:


sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.barplot(c_df.index, c_df.Count)
plt.xticks(rotation=90)
plt.xlabel('Words')
plt.title('30 Single Most Common Words Among Sunscreen Commenters')
plt.savefig('Plots/Single_Word_Freq.png', dpi=300, bbox_inches = "tight")
plt.show()


# In[124]:


single_text = ""
for word in c_df.index:
    single_text += word
    single_text += ' '
    
wc = WordCloud()
wc.generate(single_text)

# Display the generated image:
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.savefig('Plots/Single_Word_WordCloud.png', dpi=300, bbox_inches = "tight")
plt.show()


# In[125]:


c_df = pd.DataFrame.from_dict(bidict, orient='index')
c_df.columns = ['Count']
get_ipython().run_line_magic('matplotlib', 'inline')
c_df = c_df.sort_values('Count', ascending=False).head(30)


# In[126]:


new_ind = []
for bi in c_df.index: 
    new_ind.append('-'.join(list(bi)))
c_df.index = new_ind


# In[127]:


sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.barplot(c_df.index, c_df.Count)
plt.xticks(rotation=90)
plt.xlabel('2-Paired Words')
plt.title('30 Most Common 2-Paired Words Among Sunscreen Commenters')
plt.savefig('Plots/Bigram_Word_Freq.png', dpi=300, bbox_inches = "tight")
plt.show()


# In[128]:


bi_text = ""
for word in c_df.index:
    bi_text += word
    bi_text += ' '
    
wc = WordCloud(collocation_threshold=3)
wc.generate(bi_text)

# Display the generated image:
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.savefig('Plots/Bigram_Word_WordCloud.png', dpi=300, bbox_inches = "tight")
plt.show()


# In[129]:


c_df = pd.DataFrame.from_dict(tridict, orient='index')
c_df.columns = ['Count']
get_ipython().run_line_magic('matplotlib', 'inline')
c_df = c_df.sort_values('Count', ascending=False).head(30)
new_ind = []
for bi in c_df.index: 
    new_ind.append('-'.join(list(bi)))
c_df.index = new_ind


# In[130]:


sns.set(rc={'figure.figsize':(11.7,8.27)})
sns.barplot(c_df.index, c_df.Count)
plt.xticks(rotation=90)
plt.xlabel('3-Paired Words')
plt.title('30 Most Common 3-Paired Words Among Sunscreen Commenters')
plt.savefig('Plots/Trigram_Word_Freq.png', dpi=300, bbox_inches = "tight")
plt.show()


# In[ ]:




