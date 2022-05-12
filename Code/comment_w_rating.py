import pandas as pd
import os
import re
import nltk.corpus
from nltk.corpus import stopwords


df=pd.read_csv(os.path.join('Data','Sunscreen_Comments_Full.csv'))
df=df.reset_index()[['Product_ID','Comment','Rating']]

df=df.dropna()

df['Comment'] = [re.sub('[^A-Za-z0-9]+', ' ', w) for w in df['Comment']]

nltk.download('stopwords')
stop_words = stopwords.words('english')
df['Comment'] = df['Comment'].apply(lambda x: " ".join([word for word in x.split() if word not in (stop_words)]))

df['Comment'] = df['Comment'].str.lower()

df = df[~df['Comment'].str.contains(' un ', na=False)]
df = df[~df['Comment'].str.contains(' uno ', na=False)]
df = df[~df['Comment'].str.contains(' una ', na=False)]
df = df[~df['Comment'].str.contains(' e ', na=False)]
df = df[~df['Comment'].str.contains(' el ', na=False)]
df = df[~df['Comment'].str.contains(' la ', na=False)]
df = df[~df['Comment'].str.contains(' este ', na=False)]
df = df[~df['Comment'].str.contains(' est ', na=False)]
df = df[~df['Comment'].str.contains(' es ', na=False)]
df = df[~df['Comment'].str.contains(' ra ', na=False)]
df = df[~df['Comment'].str.contains(' gef ', na=False)]
df = df[~df['Comment'].str.contains(' se ', na=False)]
df = df[~df['Comment'].str.contains(' est ', na=False)]
df = df[~df['Comment'].str.contains(' er ', na=False)]
df = df[~df['Comment'].str.contains(' sie ', na=False)]
df = df[~df['Comment'].str.contains(' ich ', na=False)]
df = df[~df['Comment'].str.contains(' que ', na=False)]
df = df[~df['Comment'].str.contains(' den ', na=False)]

df=df.drop_duplicates().dropna()
df=df[df['Comment'].map(len) > 10]


df=df.reset_index()[['Product_ID','Comment','Rating']]


outpath=os.path.join('Data','Comment_w_rating.csv')
df.to_csv(outpath)
