import pandas as pd
import os
import re
import nltk.corpus
from nltk.tokenize import word_tokenize

# cleaning comments a bit more before making analysis

df = pd.read_csv(os.path.join("Data", "Skin_wreviews.csv"))
df["Comment"] = df["Comment"].str.lower()

df = df[~df["Comment"].str.contains(" un ", na=False)]
df = df[~df["Comment"].str.contains(" uno ", na=False)]
df = df[~df["Comment"].str.contains(" una ", na=False)]
df = df[~df["Comment"].str.contains(" e ", na=False)]
df = df[~df["Comment"].str.contains(" el ", na=False)]
df = df[~df["Comment"].str.contains(" la ", na=False)]
df = df[~df["Comment"].str.contains(" este ", na=False)]
df = df[~df["Comment"].str.contains(" est ", na=False)]
df = df[~df["Comment"].str.contains(" es ", na=False)]
df = df[~df["Comment"].str.contains(" ra ", na=False)]
df = df[~df["Comment"].str.contains(" gef ", na=False)]
df = df[~df["Comment"].str.contains(" se ", na=False)]
df = df[~df["Comment"].str.contains(" est ", na=False)]
df = df[~df["Comment"].str.contains(" er ", na=False)]
df = df[~df["Comment"].str.contains(" sie ", na=False)]
df = df[~df["Comment"].str.contains(" ich ", na=False)]
df = df[~df["Comment"].str.contains(" que ", na=False)]
df = df[~df["Comment"].str.contains(" den ", na=False)]

df = df.drop_duplicates().dropna()
df = df[df["Comment"].map(len) > 10]
df = df.reset_index()[["Product_ID", "Comment", "Skin_Tone", "Skin_Type"]]


# Finding basic information for skin tone and skin type of yesstyle customers

Skintone = df.groupby("Skin_Tone")
Skintone.size()

# Skin_Tone

# Deep              48
# Fair             590
# Light           1214
# Light Medium    1024
# Medium           513
# Medium Deep       39
# Olive             53
# Tan              188
# Very Deep         17

Skintype = df.groupby("Skin_Type")
Skintype.size()

# Skin_Type

# Combination    1971
# Dry             753
# Normal          438
# Oily            524


Skintone_Skintype = df.groupby(["Skin_Tone", "Skin_Type"])
Skintone_Skintype.size()

# Skin_Tone     Skin_Type

# Deep          Combination     24
#               Dry              7
#               Normal           2
#               Oily            15

# Fair          Combination    335
#               Dry            140
#               Normal          62
#               Oily            53

# Light         Combination    630
#               Dry            275
#               Normal         139
#               Oily           170

# Light Medium  Combination    559
#               Dry            187
#               Normal         125
#               Oily           153

# Medium        Combination    280
#               Dry            103
#               Normal          58
#               Oily            72

# Medium Deep   Combination     21
#               Dry              4
#               Normal           6
#               Oily             8

# Olive         Combination     23
#               Dry              7
#               Normal          13
#               Oily            10

# Tan           Combination     93
#               Dry             28
#               Normal          29
#               Oily            38

# Very Deep     Combination      6
#               Dry              2
#               Normal           4
#               Oily             5


Skintype_Skintone = df.groupby(["Skin_Type", "Skin_Tone"])
Skintype_Skintone.size()

# Combination  Deep             24
#              Fair            335
#              Light           630
#              Light Medium    559
#              Medium          280
#              Medium Deep      21
#              Olive            23
#              Tan              93
#              Very Deep         6

# Dry          Deep              7
#              Fair            140
#              Light           275
#              Light Medium    187
#              Medium          103
#              Medium Deep       4
#              Olive             7
#              Tan              28
#              Very Deep         2

# Normal       Deep              2
#              Fair             62
#              Light           139
#              Light Medium    125
#              Medium           58
#              Medium Deep       6
#              Olive            13
#              Tan              29
#              Very Deep         4

# Oily         Deep             15
#              Fair             53
#              Light           170
#              Light Medium    153
#              Medium           72
#              Medium Deep       8
#              Olive            10
#              Tan              38
#              Very Deep         5


outpath = os.path.join("Data", "Skin_wreviews_cleaned.csv")
df.to_csv(outpath)
