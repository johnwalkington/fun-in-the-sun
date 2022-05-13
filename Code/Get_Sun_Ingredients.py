import os
import pandas as pd

IN_PATH = os.path.join("Data", "Product_Info_Sunscreen.csv")
OUT_PATH = os.path.join("Data", "Fitered_ingredients.csv")

df = pd.read_csv(IN_PATH)

# this file is used to translate chemical names to trade names, the beggining of this file is used  to import data
filter_ingredients = df["Ingredients"]

ingredient_list = []

# this code is getting the ingredient strings isolated, making sure that things will be nice and clean. We're converting to uppercase because a lot of the ingredients have inconsistent casing.

for i in range(len(filter_ingredients)):
    row = filter_ingredients[i]
    minilist = row.upper().split(",")
    for item in minilist:
        if item in ingredient_list:
            ingredient_list = ingredient_list
        else:
            ingredient_list += [item.strip()]

# okay this list is HUGE, but it's formatted this way to catch typos, weird formatting, Japan calls Titanium Dioxide Tianium Oxide etc, it's loading in a dictionary!

ingredient_dict = {
    "BIS-ETHYLHEXYLOXYPHENOL METHOXYPHENYL TRIAZINE": "TINOSORB S",
    "BUTYL METHOXYDIBENZOYLMETHANE": "AVOBENZONE",
    "DIETHYLAMINO HYDROXYBENZOYL HEXYL BENZOATE": "UVINUL A PLUS",
    "DIETHYLHEXYL BUTAMIDO TRIAZONE": "ISCOTRIZINOL",
    "DIBENZIMIDAZOLE TETRASULFONATE": "NEO HELIOPAN AP",
    "DROMETRIZOLE TRISILOXANE": "MEXORYL XL",
    "ETHYLHEXYL METHOXYCINNAMATE": "OCTINOXATE",
    "ETHYLHEXYL SALICYLATE": "OCTISALATE",
    "ETHYLHEXYL TRIAZONE": "UVINUL T 150",
    "HOMOSALATE": "HOMOSALATE",
    "ISOAMYL P-METHOXYCINNAMATE": "AMILOXATE",
    "METHYLENE BIS-BENZOTRIAZOLYL TETRAMETHYLBUTYLPHENOL": "TINOSORB M",
    "PHENYLBENZIMIDAZOLE SULFONIC ACID": "ENSULIZOLE",
    "POLYSILICONE-15": "PARSOL SLX",
    "TEREPHTHALYLIDENE DICAMPHOR SULFONIC ACID": "MEXORYL SX",
    "TRIS-BIPHENYL TRIAZINE": "TINOSORB A2B",
    "TITANIUM OXIDE": "TITANIUM DIOXIDE",
    "ZINC OXIDE (CI 77947)": "ZINC OXIDE",
    "TITANIUM DIOXIDE (CI 77891)": "TITANIUM DIOXIDE",
    "AVOBENZONE": "AVOBENZONE",
    "OCTOCRYLENE": "OCTOCRYLENE",
    "ZINC OXIDE": "ZINC OXIDE",
    "TITANIUM DIOXIDE": "TITANIUM DIOXIDE",
    "BISETHYLHEXYLOXYPHENOL METHOXYPHENYL TRIAZINE": "TINOSORB S",
    " ETHYLHEXYLMETHOXYCINNAMATE": "OCTINOXATE",
    "BIS-ETHYLHEXYLOXYPHENOLMETHOXYPHENYLTRIAZINE": "TINOSORB S",
    "LOW TEMPERATURE FIRED ZINC OXIDE": "ZINC OXIDE",
    "FINE PARTICLE TITANIUM OXIDE": "TITANIUM DIOXIDE",
    "T-BUTYLMETHOXYDIBENZOYLMETHANE": "AVOBENZONE",
    "HEXYL DIETHYLAMINOHYDROXYBENZOYL BENZOATE": "UVINUL A PLUS",
    "DIETHYLAMINOHYDROXY HEXYL BENZOYL BENZOATE": "UVINUL A PLUS",
    "BISETHYLHEXYLOXYPHENOL METHOXYPHENYLTRIAZINE": "TINOSORB S",
    "HEXYL DIETHYLAMINOHYDROXYBENZOYLBENZOATE": "UVINUL A PLUS",
    "ETHYLHEXYLTRIAZONE": "UVINUL T 150",
    "HEXYL DIETHYLAMINOHYDROXYBENZOYLBENZOIC ACID": "UVINUL A PLUS",
    "ETHYL METHOXYL METHOXYCINNAMATE": "OCTINOXATE",
    "METHYLENEBISBENZOTRIAZOLYLTETRAMETHYLBUTYLPHENOL": "TINOSORB M",
}

keys = ingredient_dict.keys()


row_ingredient_list = []

# okay this is actually doing the data recoding, we're finally getting most of the chemical names, typos and all to read in properly.

for i in range(len(filter_ingredients)):
    row = filter_ingredients[i]
    minilist = row.upper().split(",")
    for i in range(len(minilist)):
        if minilist[i].strip() in keys:
            minilist[i] = ingredient_dict[minilist[i].strip()]
        else:
            minilist[i] = None
    row_ingredient_list += [list(filter(None, minilist))]


df["Filtered_Ingredients"] = row_ingredient_list

df = df[df["Filtered_Ingredients"].map(lambda d: len(d)) > 0]

df.to_csv(OUT_PATH)
