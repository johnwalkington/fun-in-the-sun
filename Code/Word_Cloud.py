from wordcloud import WordCloud
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic("matplotlib", "inline")


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

stop = stopwords.words("English")
from langdetect import detect

comm = pd.read_csv(IN_PATH).iloc[:, 1:]
comm.Comment = comm.Comment.apply(lambda x: str(x)[1:-1])

# Here we read in the comment data, and for the graphs that we will generate we
# need to tokenize the comments every word.

# To ensure that we get the most relevant words, bigrams, and trigrams, we need to clean the
# text data by eliminating any potnetial stopwords ("I", "doesn't") and remove punctuation.
bidict = FreqDist()
tridict = FreqDist()
count = 0
for comment in comm["Comment"]:
    try:
        if detect(comment) == "en":
            sample = comment.lower().split()
            words = [w for w in sample if w not in stop]
            words = word_tokenize(" ".join(words))
            words = [w for w in words if w not in stop]
            words = [re.sub("[^A-Za-z0-9]+", "", w) for w in words]
            words = [w for w in words if w]
            # Below we try to normalize the words, by forcing an action to encompass one
            # part of speech (a verb in this case). For example, the action "applying", "apply",
            # "applyed" all encompass the same overall meaning but would be counted seperately
            # without lemmatization.
            single_words = [lemmatize.lemmatize(w, pos="v") for w in words]

            # After the normalization, we pass the single most common words, bigrams,
            # and trigrams into a dictionary.

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


# In the following lines of code we convert the dictionary into a dataframe, taking the 30
# most common words, bigrams, and trigrams. We plot them and save them.
c_df = pd.DataFrame.from_dict(freqdist, orient="index")
c_df.columns = ["Count"]
get_ipython().run_line_magic("matplotlib", "inline")
c_df = c_df.sort_values("Count", ascending=False).head(30)


# Here is a barplot of the 30 most single common words.
sns.set(rc={"figure.figsize": (11.7, 8.27)})
sns.barplot(c_df.index, c_df.Count)
plt.xticks(rotation=90)
plt.xlabel("Words")
plt.title("30 Single Most Common Words Among Sunscreen Commenters")
plt.savefig("Plots/Single_Word_Freq.png", dpi=300, bbox_inches="tight")
plt.show()


# Here is another visualization of the same data; a wordcloud.

single_text = ""
for word in c_df.index:
    single_text += word
    single_text += " "

wc = WordCloud()
wc.generate(single_text)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.savefig("Plots/Single_Word_WordCloud.png", dpi=300, bbox_inches="tight")
plt.show()


# Here we perform an equivalent analysis, just using the bigram dictionary.


c_df = pd.DataFrame.from_dict(bidict, orient="index")
c_df.columns = ["Count"]
get_ipython().run_line_magic("matplotlib", "inline")
c_df = c_df.sort_values("Count", ascending=False).head(30)


new_ind = []
for bi in c_df.index:
    new_ind.append("-".join(list(bi)))
c_df.index = new_ind


sns.set(rc={"figure.figsize": (11.7, 8.27)})
sns.barplot(c_df.index, c_df.Count)
plt.xticks(rotation=90)
plt.xlabel("2-Paired Words")
plt.title("30 Most Common 2-Paired Words Among Sunscreen Commenters")
plt.savefig("Plots/Bigram_Word_Freq.png", dpi=300, bbox_inches="tight")
plt.show()


bi_text = ""
for word in c_df.index:
    bi_text += word
    bi_text += " "

wc = WordCloud(collocation_threshold=3)
wc.generate(bi_text)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.savefig("Plots/Bigram_Word_WordCloud.png", dpi=300, bbox_inches="tight")
plt.show()


# Once again, we perform the same analysis but using trigrams. This time, we only create a barplot
# and not a wordcloud, as it would be overly cluddered.


c_df = pd.DataFrame.from_dict(tridict, orient="index")
c_df.columns = ["Count"]
get_ipython().run_line_magic("matplotlib", "inline")
c_df = c_df.sort_values("Count", ascending=False).head(30)
new_ind = []
for bi in c_df.index:
    new_ind.append("-".join(list(bi)))
c_df.index = new_ind


sns.set(rc={"figure.figsize": (11.7, 8.27)})
sns.barplot(c_df.index, c_df.Count)
plt.xticks(rotation=90)
plt.xlabel("3-Paired Words")
plt.title("30 Most Common 3-Paired Words Among Sunscreen Commenters")
plt.savefig("Plots/Trigram_Word_Freq.png", dpi=300, bbox_inches="tight")
plt.show()
