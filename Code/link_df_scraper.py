import pandas as pd
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import time
import numpy as np
import os

chrome_path = os.path.join("drivers", "chromedriver 3")
driver = webdriver.Chrome(chrome_path)
OUT_PATH = os.path.join("Data", "Product_Links.csv")


mat = []
product_links = []

# Since YesStyle is a non-static website, we have to open it up using an automated browser and scrape the hyperlinks for the sunscreen product
# listings using Selenium. This requires chromedriver to be installed on one's computer, assuming one is using a Chrome browser.

for num in range(1, 17):
    try:
        next_page = f"https://www.yesstyle.com/en/beauty-sunscreens/list.html/bcc.15601_bpt.46#/sb=136&bcc=15601&pn={num}&bpt=46&bt=37&s=10&l={num}"
        driver.get(next_page)
        time.sleep(1)
        # These pages are the website links where the individual product listings are located, we manually create these website page links using a for loop.
        # In total there are 16 of them, making for roughly 550 sunscreen products.
        soup = BeautifulSoup(driver.page_source)
        product_links = []
        for s in soup.find_all("a"):
            if s.has_attr("href"):
                link = s["href"]
                if link.split("/")[-1].split(".")[0] == "pid":
                    product_links.append(s["href"])
        # After getting the soup variable, we get the "href" attribute for any tag with an "a" on it, which will give us all the product links.
        time.sleep(1)
        # To make sure we don't run into an error, moving between web pages too fast, we include implicit wait times.
        mat.append(product_links)
    except:
        continue
        driver.close()
driver.close()
time.sleep(1)
all_links = [link for i in range(len(mat)) for link in mat[i]]
all_links = list(set(all_links))
# Converting the matrix of product links, separated by website page, into one list.

link_df = pd.DataFrame([all_links]).transpose()
link_df.columns = ["Links"]
link_df.to_csv(OUT_PATH)
# We push the product links to a csv, after converting it into a dataframe.
