import pandas as pd
import numpy as np
import nltk
import re
from textblob import TextBlob

from nltk.probability import FreqDist
freqdist = FreqDist()

from nltk.stem import WordNetLemmatizer
lemmatize = WordNetLemmatizer()

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

stop = stopwords.words('English')

comm = pd.read_csv('Sunscreen_Comments_Full.csv').iloc[:, 1:]
comm.Comment = comm.Comment.apply(lambda x: str(x)[1:-1])

# Change to comm['Comment'][:2] for only a fraction of the comments, so it doesn't take forever to run. 
for comment in comm['Comment']: 
    lower_comment = comment.lower()
    words = lower_comment.split()
    words = [w for w in words if w not in stop]
    reformat = ' '.join(words)
    words = word_tokenize(reformat)
    words = [re.sub('[^A-Za-z0-9]+', '', w) for w in words]
    words = [w for w in words if w]
    words = [lemmatize.lemmatize(w, pos = 'v') for w in words]
#     TextBlob(words).detect_language()
    # Need to filter outer comment by language 
    for w in words: 
        freqdist[w] += 1
c_df = pd.DataFrame.from_dict(freqdist, orient='index')
c_df.columns = ['Count']
%matplotlib inline
c_df.sort_values('Count', ascending=False).head(20).plot(kind = 'bar');
