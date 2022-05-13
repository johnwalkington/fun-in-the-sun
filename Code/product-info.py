import pandas as pd 
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import numpy as np
import os

# Given the different ording of the scraper code, we repeated this first step
# in the product url dataframe. Only now, instead of pushing our findings into
# a csv, we keep the links so that we can extract relevant information from
# the individual product itself. 
chrome_path = os.path.join("drivers", "chromedriver 3")
driver = webdriver.Chrome(chrome_path)
OUT_PATH = os.path.join("Data", "Product_Info_Sunscreen.csv")

mat = []
product_links = []


for num in range(1, 17):
    try:
        next_page = f'https://www.yesstyle.com/en/beauty-sunscreens/list.html/bcc.15601_bpt.46#/sb=136&bcc=15601&pn={num}&bpt=46&bt=37&s=10&l={num}'
        driver.get(next_page)
        time.sleep(1)

        soup = BeautifulSoup(driver.page_source)
        product_links = []
        for s in soup.find_all('a'): 
            if s.has_attr('href'): 
                link = s['href']
                if link.split('/')[-1].split('.')[0] == 'pid':
                    product_links.append(s['href'])
        time.sleep(1)
                    
        mat.append(product_links)
    except: 
        continue
        driver.close()
driver.close()
time.sleep(1)
all_links = ([link for i in range(len(mat)) for link in mat[i]])
all_links = list(set(all_links))

driver = webdriver.Chrome(chrome_path)
# From the product links, we scrape the attributes of the sunscreen product itself. This includes things like
# ingredients, price, name of the product, country that it is imported from etc. 
json = {}
new_mat = []
d = {}
count = 0
# Once again we have a count to make sure everything is working fine, given that this takes a long time to run.
# The results are inputed as dictionaries and then put into a json format. 
for prod in all_links:
    try:
        driver.get(prod)
        time.sleep(1)
        soup = BeautifulSoup(driver.page_source)
        mat = []
        for ing in soup.find_all('span', {'ng-if':'productDataStatus.initialLoad'}):
            mat.append(ing.get_text(separator = '|').split('|'))
        ing_list = mat[0]
        ing_list = [ing.replace('\n', '') for ing in ing_list if len(ing) > 1][:-1]
        info_list = mat[1]
        info_list = [fo.replace('\n', '') for fo in info_list if len(fo) > 1]

        for key, val in list(zip(info_list[1:][::2], info_list[2:][::2])):
            d[key.split(':')[0].strip()] = val
        time.sleep(1)
        for s in soup.find_all('h1', {'class':'flex flex-xs-100'}):
            name = (s.get_text(separator = '|').split('|'))
            name = (''.join([n.replace('\n', '') for n in name if len(n) > 1]))
        for s in soup.find_all('span', {'class':'sellingPrice ng-binding'}):
            price = ''.join(s.text.split())
        time.sleep(2)
        d['Price'] = price
        d['Ingredients'] = "".join(ing_list)
        json[name] = d
        time.sleep(1)
        new_mat.append(info_list)
        d ={}
        count += 1  
        print(count)
    except:
        continue
# If the keys in the dictionaries have ":" at the end or any white space, we control for that here, and move our
# results into a dataframe. 
for d in json.keys():
    json[d] = {k.replace(":", ""): v for k, v in json[d].items()}
    json[d] = {k.strip(): v for k, v in json[d].items()}
sample = pd.DataFrame.from_dict(json.values(), orient="columns")
sample.reset_index(inplace=True)
sample["index"] = json.keys()
 
table1 = sample.set_index('Catalog No.')
table1.columns = ['Product', 'Imported Country', 'Other Info', 'Price', 'Ingredients', 'Made in', 
                 'Cruelty_free', 'Vegan']

table1['Ranking_In_Best_Seller_List'] = [i+1 for i in range(len(table1.iloc[:, 0]))]
# We push our dataframe to a csv. 
table1.to_csv(OUT_PATH)

