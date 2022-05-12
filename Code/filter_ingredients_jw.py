import os
import pandas as pd

IN_PATH = os.path.join("Data", "Product_Info_Sunscreen.csv")
OUT_PATH = os.path.join("Data", "Split_Recode_Product_Info.csv")

df = pd.read_csv(IN_PATH)

filter_ingredients = df['Ingredients']

ingredient_list = []

for i in range(len(filter_ingredients)):
    row = filter_ingredients[i]
    minilist = row.upper().split(",")
    for item in minilist:
        if item in ingredient_list:
            ingredient_list = ingredient_list
        else:
            ingredient_list += [item.strip()]

ingredient_dict = {"BIS-ETHYLHEXYLOXYPHENOL METHOXYPHENYL TRIAZINE": "TINOSORB S", 
"BUTYL METHOXYDIBENZOYLMETHANE": "AVOBENZONE", "DIETHYLAMINO HYDROXYBENZOYL HEXYL BENZOATE": "UVINUL A PLUS", 
"DIETHYLHEXYL BUTAMIDO TRIAZONE": "ISCOTRIZINOL", "DIBENZIMIDAZOLE TETRASULFONATE": "NEO HELIOPAN AP", 
"DROMETRIZOLE TRISILOXANE": "MEXORYL XL", "ETHYLHEXYL METHOXYCINNAMATE": "OCTINOXATE", "ETHYLHEXYL SALICYLATE": "OCTISALATE", 
"ETHYLHEXYL TRIAZONE": "UVINUL T 150", "HOMOSALATE ISOAMYL P-METHOXYCINNAMATE": "AMILOXATE", 
"METHYLENE BIS-BENZOTRIAZOLYL TETRAMETHYLBUTYLPHENOL": "TINOSORB M", "OCTOCRYLENE PHENYLBENZIMIDAZOLE SULFONIC ACID": "ENSULIZOLE", 
"POLYSILICONE-15": "PARSOL SLX", "TEREPHTHALYLIDENE DICAMPHOR SULFONIC ACID":  "MEXORYL SX", 
"TRIS-BIPHENYL TRIAZINE": "TINOSORB A2B", "TITANIUM OXIDE": "TITANIUM DIOXIDE"}

keys = ingredient_dict.keys()

row_ingredient_list = []


for i in range(len(filter_ingredients)):
    row = filter_ingredients[i]
    minilist = row.upper().split(",")
    for i in range(len(minilist)):
        if minilist[i].strip() in keys:
            minilist[i] = ingredient_dict[minilist[i].strip()]
        else:
            minilist[i] = minilist[i]
    row_ingredient_list += [minilist]

df['Filtered_Ingredients'] = row_ingredient_list

df.to_csv(OUT_PATH)