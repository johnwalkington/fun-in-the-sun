import pandas as pd 
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import numpy as np
import os

# You need to download chromedriver
# (doesn't matter if you have a mac or PC but check your version and downloaded the right one)


# Set a directory to store the csv files. Will be about 544 of them.
# The point of this is that if there is an error mid-way through, the scraper
# won't start from the very beginning and pick up where it is left off. 


dfs = []
driver = webdriver.Chrome('/Users/patrickpoleshuk/Downloads/chromedriver 3')
# Change this to the path of your chromedriver. 
df = pd.DataFrame()

num = 0

# You're going to have to change this first statement for loop statement. 
# for prod in all_links:

# -> Loop through the data columns of the links: I think it's something like this: "for link in df['Links']",
# instead of what is above. 
    
    file = "product{}.csv".format(str(num))
    if os.path.exists(file):
        num += 1
        continue
    
    driver.get(prod)

            
    time.sleep(6)
    for inst in range(1, 100):
        try:
            driver.find_element_by_xpath('/html/body/div[4]/main/div[6]/div[2]/button').click()
            time.sleep(5)
        except Exception as e:
            break
        finally: 
            try:
                driver.find_element_by_xpath('/html/body/div[4]/main/div[6]/div[2]/button').click()
                time.sleep(5)
            except: 
                break

    time.sleep(1)
    soup = BeautifulSoup(driver.page_source)

    mat = []
    fill = []
    for s in soup.find_all('tbody'): 
        line = (s.get_text(separator='|').split('|'))
        line = [e.replace('\n', '') for e in line]
        line = [e for e in line if e]
        mat.append(line)
    
    for i, name in enumerate(mat[0]): 
        if name == 'Catalog No.:': 
            cat_index = mat[0][i+1]

    comm = []
    for title, date, narr in zip(soup.find_all('div', {'class':'reviewTitle'}), 
                             soup.find_all('div', {'class':'reviewDate'}), 
                            soup.find_all('div', {'class':'reviewContent'})):
        fill.append(cat_index)
        fill.append(title.text)
        fill.append(date.text)
        fill.append(narr.text.strip('\n'))
        comm.append(fill)
        fill = []

    df = pd.DataFrame(comm)
    
#columns=['Cat_Index', 'Title', 'Date', 'Comment']).set_index('Cat_Index')

    dfs.append(df)
    print(file)
    df.to_csv(file)
    
    num += 1
    
driver.close()
