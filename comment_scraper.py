import requests
import pandas as pd
import numpy as np 
dfs = []
count = 0
# The count is there for my own sanity: to make sure everything is working and running fine, as the scraper goes
# through multiple product pages. 

# Since YesStyle is very restrictive on webscraping, even using their own internal API, this code might get 
# blocked with a "401" error by the time anyone tries to run it. 
# In that case you may need to go to an API formatter like Insomnia and format the internal API link again. 
url = "https://www.yesstyle.com/rest/customer-review/v1/reviewer-reviews"
for product in link_df.Links:
    product_id = (product.split('/')[-1].split('.')[1])
    print(product)
    for page in range(1, 10**6):

        querystring = {"pageNum":str(page),"reviewProductId":str(product_id),"reviewerRatingFilterOptionId":"8","sortByOptionId":"130"}

        payload = ""
        headers = {
    'cookie': "WTPERSIST=; ss_fix_1_c3RvcmVmcm9udA_w_s_w_s=MTcyLjMxLjIuMzM_w_s; ysv2_cookie=""; ysesn=true; ysesnd=1651003979553; tcurrency=19; orderChannel=2; yshsdb=true; yshccmfg=true; yscmds=false; yscmda=false; yscmdp=false; coid=226; locale=en; _gcl_au=1.1.608521574.1651003982; wtstp_nv=0; miCookieOptOut=1; ORA_FPC=id=185a6e98-84e8-4b40-bef3-eb2a331c8c3a; yshspbnsi=true; yssabnot=3; yshsabt=true; wtstp_ttv2_e_737859735586197=Mid-Season%20Sale%20-%202*Women_PA01**Mid-Season%20Sale%20-%202(en)*2022%2Fweek17******1*0*100; wtstp_ttv2_c_737859735586197=Mid-Season%20Sale%20-%202*Women_PA01**Mid-Season%20Sale%20-%202(en)*2022%2Fweek17******1*0*100; _gid=GA1.2.1968229496.1651107695; AssocLinkCode=1YBGMF7K; _dy_csc_ses=t; _dy_c_exps=; _dycnst=dg; _dyid=1567252878134553283; _dyjsession=c6213024a32ddb4cebe4c5a99318446e; _dyid_server=1567252878134553283; _dy_c_att_exps=; LPVID=I0NTk1MDZhODNiM2RmYjRm; _dyfs=1651191241606; yssuf=false; yssle=false; _dy_geo=US.NA.US_TX.US_TX_Austin; _dy_df_geo=United%20States.Texas.Austin; __cfruid=92666da79f147e5c7763134fe9da2e2a23973bd8-1651345221; ysbasket=; ysbci=; yswishlist=; ysmipu=false; yshspbsi=true; srlasod=""; ss_fix_1_Y2hlY2tvdXQ_w_s=MTcyLjMxLjEuMjM_w_s; ysso=false; yssid=3Ic3Gld1lw0ObLn5zU8%2B%2BlBZvsQccMt5toB217AAK7tljjHl3Sp3wg%3D%3D; ysat=0fec29dbe4f74707a1b7448d4760b3a2; lvni=69; _fbp=fb.1.1651352072631.1443248586; ysgeln=Sunscreens; dy_fs_page=www.yesstyle.com%2Fen%2Fscinic-enjoy-all-round-airy-sun-stick-spf50-pa-25g-25g%2Finfo.html%2Fpid.1069644188; _clck=suyntw|1|f13|0; LPSID-31371127=uYd-s2s4T2yYLjfMp5_T2w; preMaCo=ref:https://localhost:8892; wt_mcp_sid=4283738074; __cf_bm=iIRwP.Wk4Z06LU8Vb5VZZpcYaOtYZN5VlFs4gwExaSU-1651365832-0-AYfhDtU3Pr45pUT9CEWAhqLjppe7Kldfm6yTwPC0K9/IrP0T/kR990SVlS3GZYo+ImD+P4TVlqATNh7S/kVeUq0=; ysbph=1052684630_1077701949_1068351701_1048875972_1094424964_1055581849_1094981352_1066131843_1071931173_1091552237_1103394129_1063056887_1074422962_1058331261_1111620592_1065719343_1069644188_1107744417_1067313175_1110189296_1106584439_1105364416_1063578220_1096470322_1099798067_1086222946_1098919248_1060114186_1094424963_1089312147; yslasturl=https%3A%2F%2Fwww.yesstyle.com%2Fen%2Fcosrx-aloe-soothing-sun-cream-50ml%2Finfo.html%2Fpid.1052684630; _dy_ses_load_seq=39560%3A1651366535714; _dy_soct=531342.1016628.1651366535*517704.976733.1651366535; _dy_lu_ses=c6213024a32ddb4cebe4c5a99318446e%3A1651366538219; _dycst=dk.m.c.ss.; _dy_toffset=-3; _ga=GA1.2.852685801.1651003983; _ga_YM4H18NKQM=GS1.1.1651363227.25.1.1651366539.55; _uetsid=794d16e0c74f11eca7784df1448f9b07; _uetvid=794dbfe0c74f11ecaac191e97868e5e2; _gat_UA-428450-19=1; wtstp_ttv2_s_737859735586197=9808; _clsk=x4ka26|1651366541392|22|1|b.clarity.ms/collect; wtstp_rla=737859735586197%2C24%2C1651365084090",
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
    'y-authorization': "4b916d7e54a11972261d33bf9aa1b185e253291c1d01234a050502d1d8bdb44b:3e04ad9e53d73f9ee56b853bec793622ac91b1e13a6a32cf60b5b427e524208c",
    'y-expiration': "1651368332406",
    'y-string': "qloGsS8MyYu4tNnAcrU4G1F%2Bjb7JLeYUxDPtbgDgjEyzeCgZ5Ffx8GHuljw5q7tovZPNs3DvyhkqboTTUKxq%2B9ea8Y%2FJaSU558ng35xq6VppX37lZXkhFw%3D%3D"
            }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        
        r = response.json()
        store = []
        for d in r.values(): 
            if type(d) != int:
                store.append(d)
        json = store[0]
        
        if not json:
            break
    
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
        
        for i in range(len(mat)):
            mat[i][2] = (str(mat[i][2])[1:-1])
    
    
        df = pd.DataFrame(mat)
    
        dfs.append(df)
    count += 1

    print(count)
    
comm = pd.concat(dfs).reset_index().iloc[:, 1:]
comm.columns = ['Product_ID', 'Title', 'Comment', 'Date', 'Extra', 'Gender', 'Age', 'Skin_Tone', 
               'Skin_Type', 'Rating']

comm.to_csv('Sunscreen_Comments.csv')
