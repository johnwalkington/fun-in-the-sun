import pandas as pd
import os
import re
import nltk.corpus

nltk.download('punkt')
nltk.download('stopwords')

df = pd.read_csv(os.path.join("Data", "Sunscreen_Comments_Full.csv"))
df = df.reset_index()[["Product_ID", "Comment", "Skin_Tone", "Skin_Type"]]


df["Skin_Tone"] = df["Skin_Tone"].str.replace("Skin Tone: ", "")

# getting product which has all skin tone and skin type information
df = df.dropna()

# remove punctuation
df["Comment"] = [re.sub("[^A-Za-z0-9]+", " ", w) for w in df["Comment"]]

# remove comments not in English
nltk.download("stopwords")
from nltk.corpus import stopwords

stop_words = stopwords.words("english")
df["Comment"] = df["Comment"].apply(
    lambda x: " ".join([word for word in x.split() if word not in (stop_words)])
)

df = df.reset_index()[["Product_ID", "Comment", "Skin_Tone", "Skin_Type"]]


outpath = os.path.join("Data", "Skin_wreviews.csv")
df.to_csv(outpath)
