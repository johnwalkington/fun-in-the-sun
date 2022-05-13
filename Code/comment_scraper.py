import requests
import pandas as pd
import numpy as np 
from selenium import webdriver
import time
import os

chrome_path = os.path.join("drivers", "chromedriver 3")


IN_PATH = os.path.join("Data", "Product_Links.csv")

OUT_PATH = os.path.join("Data", "Sunscreen_Comments_Full.csv")

link_df = pd.read_csv(IN_PATH)
# We use the product links datframe from earlier. 
driver = webdriver.Chrome(chrome_path)
driver.get('https://laendercode.net/en/2-letter-list.html')
time.sleep(1)
soup = BeautifulSoup(driver.page_source)
driver.close()

# In order to get the commenter's country of origin, we have to parse their flag image url, and use those country
# initials to get the full name of the country. This requires, scraping from another page and creating a dictionary,
# with country initials as the key and full name of the country as the value. 

c = soup.find('tbody').get_text(separator = '|').split('|')
c = [e for e in c if len(e) > 1]
d_id = {}
for init, full in zip(c[::2], c[1::2]): 
    d_id[init.lower()] = full
    
    
# The count is there to make sure everything is working and running fine, as the scraper goes
# through hundreds of product pages. 

# Since YesStyle is very restrictive on webscraping, even using their own internal API, this code might get 
# blocked with a "401" error by the time anyone tries to run it. 
# In that case you may need to go to an API formatter like Insomnia and format the internal API link again by,
# for example, copying in a cURL into Insomnia and looking at its auto-generated headers. This will only work
# temporarily, as the requests status code will go from 200 to 401 after 30 or so minutes. 
url = "https://www.yesstyle.com/rest/customer-review/v1/reviewer-reviews"
dfs = []
count = 0
for product in link_df.Links:
    product_id = (product.split('/')[-1].split('.')[1])
    print(product)
    for page in range(1, 10**6):
    # We look through the dataframe link table, and customize this header to include all products.
    # Some products will not have any comments, and for products with something like 4,000 comments, the internal API
    # only has roughly a little over 1,000 comments archived. 
        querystring = {"pageNum":str(page),"reviewProductId":str(product_id),"reviewerRatingFilterOptionId":"8","sortByOptionId":"130"}

        payload = ""
        headers = {
    'cookie': "WTPERSIST=; ysesn=true; ysesnd=1651003979553; tcurrency=19; orderChannel=2; yshsdb=true; yshccmfg=true; yscmds=false; yscmda=false; yscmdp=false; coid=226; _gcl_au=1.1.608521574.1651003982; wtstp_nv=0; miCookieOptOut=1; ORA_FPC=id=185a6e98-84e8-4b40-bef3-eb2a331c8c3a; yssabnot=3; yshsabt=true; AssocLinkCode=1YBGMF7K; _dy_c_exps=; _dycnst=dg; _dyid=1567252878134553283; _dyid_server=1567252878134553283; _dy_c_att_exps=; LPVID=I0NTk1MDZhODNiM2RmYjRm; _dy_geo=US.NA.US_TX.US_TX_Austin; _dy_df_geo=United%20States.Texas.Austin; ysbasket=; ysbci=; yswishlist=; srlasod=""; yssid=3Ic3Gld1lw0ObLn5zU8%2B%2BlBZvsQccMt5toB217AAK7tljjHl3Sp3wg%3D%3D; _fbp=fb.1.1651352072631.1443248586; _clck=suyntw|1|f13|0; _dy_toffset=-2; _dy_ses_load_seq=39560%3A1651368071861; _dy_soct=531342.1016628.1651368071*517704.976733.1651368071; _uetvid=794dbfe0c74f11ecaac191e97868e5e2; _dycst=dk.m.c.ss.; ysv2_cookie=""; locale=en; ss_fix_1_c3RvcmVmcm9udA_w_s_w_s=MTcyLjMxLjIuMzI_w_s; lvni=69; ysgeln=""; _gid=GA1.2.947339821.1651773351; yshspbsi=true; preMaCo=ref:https://localhost:8888; __cf_bm=BYbI8CS9ZkK_cxLJI7WdOhNfpAo0qgg9FWLs2vU5vnI-1651774991-0-AeRZtsDBWL/aTFpJxObThKLUZh8VO58ita+CwSZlPP8bbXclAg17C6fWJmSYDyqN4yHkuQDWkMdK7EUUb8gwHj8=; ysbph=1100473375_1057996883_1075338426_1058331261_1052684630_1107744417_1071931173_1045868872_1077701949_1068351701_1048875972_1094424964_1055581849_1094981352_1066131843_1091552237_1103394129_1063056887_1074422962_1111620592_1065719343_1069644188_1067313175_1110189296_1106584439_1105364416_1063578220_1096470322_1099798067_1086222946_1098919248_1060114186_1094424963_1089312147; yslasturl=https%3A%2F%2Fwww.yesstyle.com%2Fen%2Fneogen-dermalogy-day-light-protection-airy-sunscreen-50ml%2Finfo.html%2Fpid.1100473375; wt_mcp_sid=2105935581; _ga=GA1.1.852685801.1651003983; _gat_UA-428450-19=1; wtstp_ttv2_s_737859735586197=9960; wtstp_rla=737859735586197%2C11%2C1651775176837; _ga_YM4H18NKQM=GS1.1.1651773347.32.1.1651775257.52; _dd_s=rum=0&expire=1651776159357",
    'authority': "www.yesstyle.com",
    'accept': "*/*",
    'accept-language': "en-US,en;q=0.9",
    'cache-control': "no-cache",
    'pragma': "no-cache",
    'referer': str(product),
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': "macOS",
    'sec-fetch-dest': "empty",
    'sec-fetch-mode': "cors",
    'sec-fetch-site': "same-origin",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
    'y-authorization': "d924346f9542f8779b4af657951a5c24da2f260326351b7fc7672528dc845201:22d02dc140e63a584635e4941f4fe19aebd1a966098a485d32da605c039dfb66",
    'y-expiration': "1651777048405",
    'y-string': "MOFU4P9HLq%2F3Bnssnx1ff5M7wfkY6%2BZQZpKGpHbHpwVCW6JUOm35k4VI8sK719DpJbzgsOWC142VgaHYlBgVPgNWkVnwU0G7Acc2GGob8JB3DHF9oQJtrpQA00uGSfJgnPOK6GDnAAH8l6ijGrdXlg%3D%3D"
        }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        
        r = response.json()
        # From the internal API, we can extract the information in a json format. From this we can parse it to get the
        # title of the comment, the comment body, the star rating (normalized as 20,40,60,80, 100), skin tone & skin type,
        # and country of origin.

        # Since the json file is complex, with lists of dictionaries and subsequent dictionaries of lists within that, all the
        # comment information is required to be parsed in a different way. 
        store = []
        for d in r.values(): 
            if type(d) != int:
                store.append(d)
        json = store[0]
        
        if not json:
            break
        # The loop will go through a million iterations, but if there are not more comments archived it the loop will end.
        # This will occur at some select number after 1,000, or a lot sooner if the products have very few comments. 
    
        rev = []
        ratings = []
        for d in json: 
            for val in d.values(): 
                if type(val) == list: 
                    for key in val: 
                        rev.append(key)
                if type(val) == float:
                    ratings.append(val)
    

        for info, rate in (list(zip(rev, ratings))): 
            info['ratings'] = rate
        
        mat = []
        for d in rev:
            inp = list(d.values())[1:6]
            if 'ratings' in list(d.keys()): 
                mat.append(inp + [d['ratings']])
            else: 
                mat.append(inp + [np.nan])

        indexing = 0
        for d in rev: 
            if 'genderAnswer' in list(d.keys()): 
                mat[indexing].insert(-1, d['genderAnswer']['value'])
            else: 
                mat[indexing].insert(-1, np.nan)
            indexing += 1

        indexing = 0
        for d in rev: 
            if 'ageAnswer' in list(d.keys()): 
                mat[indexing].insert(-1, d['ageAnswer']['value'])
            else: 
                mat[indexing].insert(-1, np.nan)
            indexing += 1

        indexing = 0
        for d in rev: 
            if 'skinToneAnswer' in list(d.keys()): 
                mat[indexing].insert(-1, d['skinToneAnswer']['value'])
            else: 
                mat[indexing].insert(-1, np.nan)
            indexing += 1

        indexing = 0
        for d in rev: 
            if 'skinTypeAnswer' in list(d.keys()): 
                mat[indexing].insert(-1, d['skinTypeAnswer']['value'])
            else: 
                mat[indexing].insert(-1, np.nan)
        
            indexing += 1
        
        indexing = 0
        for d in rev:
            if 'countryAnswer' in d.keys(): 
                flag_url = (d['countryAnswer']['remarkValue'])
                code = flag_url.split('/')[-1].split('-')[0]
                mat[indexing].insert(-1, d_id[code])
                # This is where that dictionary comes into play from earlier, since the dictionary had no country attribute; only
                # the flag. 
            else: 
                mat[indexing].insert(-1, np.nan)
        
            indexing += 1
        
        for i in range(len(mat)):
            mat[i][2] = (str(mat[i][2])[1:-1])
    
    
        df = pd.DataFrame(mat)
        # We get a matrix of the infomation, which we store into a dataframe. We then append that dataframe into a list, so we have
        # a list of dataframes. 
        dfs.append(df)
    count += 1

    print(count)
# To get the final comment dataframe, we concatenate a list of all the individual product comment dataframes and push it to a csv
# file. 
comm = pd.concat(dfs).reset_index().iloc[:, 1:]

comm.columns = ['Product_ID', 'Title', 'Comment', 'Date', 'Extra', 'Gender',
                'Age', 'Skin_Tone', 'Skin_Type', 'Country', 'Rating']

comm.to_csv(OUT_PATH)
