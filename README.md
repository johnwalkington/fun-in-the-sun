# Project Report

## Goal of analysis
Sunscreens manufactured for the American market are substantially lacking in both appeal and protection. Because of the strict regulations the FDA places on sunscreen filters (the active ingredients in sunscreens), the United States has a limited offerings in terms of sun protection. Many of these approved ingredients cannot obtain the level of protection offered by foreign sunscreens. In fact, a study conducted Environmental Working Group of 446 American sunscreens found that close to two-thirds of them would fail to meet European Union standards for adaquate UVA protection. 


Sunscreens on the Korean and Japanese market are noted for both their high protection and their cosmetic elegance, attracting skincare fanatics around the world. Because of the difficulty associated with importing these sunscreens, many companies have been created just to cater to individuals wishing to have a reliable way to obtain Japanese and Korean skincare. This project focuses on the Hong Kong-based [yesstyle.com](yesstyle.com).


As a group that regularly uses foreign sunscreens, we were interested in investigating this site for a number of reasons: 

1. Scraping sunscreen ingredients.
    - We wanted to do a simple statistical analysis of the filters lsited in the best selling sunscreens on [yesstyle.com](yesstyle.com).
    - This gives us answers to a couple of questions: What sunscreen filters are attracting foreign consumers? What are the most popular
    filters used in Korean and Japanese formulas? 

2. Scraping customer reviews.
    - YesStyle has a robust review system, with some products getting thousands of reviews; even allowing users to list their age and 
    skin-type (Dry, Oily, Combination). We wanted to scrape these reviews to gain insight on common complaints and praises used by the
    skincare community. We wanted to assess the frequency of such phrases like: "drying", "moisturizing", "emollient", etc. 
    - We used the text of the scraped reviews to perform sentiment analysis. We constructed a classification of reviews into categories
    depending on how positive our algorithm perceived them as being. We were then able to correlate the positive sentiment of reviews with
    customer and product attributes to get an idea of what customers valued what attributes the most.

This project gives us a harder challenge than our midterm project, not only in terms of webscraping, but also in terms of our statistical analysis. We're interested consumer behavior and sentiments, looking at a niche and picky market segment that heavily relies on the opinions of fellow skincare enthusiasts to make purchasing decisions.


## Methodology
**data collection methods - documentation of data (all relevant columns/features) & what isn't in data**
Steps to find the word frequency: 
- We used the NLTK package
- We filtered out common stopwords in the comments
- We filtered out punctuation 

Through Lemmatization, we normalized the text so that words signifying the same action wouldn't be counted differently. For example, “walk”, “walking”, “walked” would all be casted to a verb part of speech, so that you would have the word “walk” counted three times. 
We then created a counting dictionary of single words, bigrams, and trigrams, organized by count in descending order and took the top 30 most used words to plot in a barplot.
For the single word count dictionary and bigrams word count dictionary, we also created a text cloud, for other visualization purposes.  

We used a hidden API on the Yesstyle site to scrape our product data and customer reviews.  We collected info on each product's nation of origin, importing nation, cruelty-free and vegan characteristics, price, and selling popularity.  We also were able to collect an ingredient list for every sunscreen, and built our own dictionary to classify which of these ingredients were active ingredients.

We also scraped thousands of reviews and used Textblob and NLTK's sentiment analysis features to calculate their positive or negative polarity.  We were able to split words into commonly-occuring bigrams and tabulate their frequency to create wordclouds.

After scraping, we used Tableau, pulling our data from a Postgres database, to query our data and find valuable insights.  We were able to make maps of customer location and charts of product popularity.


## Description of project and findings/lack of findings:
clearly documented
supported by analysis

## Limitations of analysis
Sentiment analysis is hard to fine-tune, so we encountered errors where our Textblob algorithm could not understand the context of some customer reviews. For example, customer reviews that had double negatives were falsely flagged as being negative. If a reviewer were to say something like, "this product does not make me break out with acne," which is a positive review, our Textblob would see the "not" and classify it as negative. We were able to mitigate this problem by simplifying our review classes to three levels of sentiment where before we had five, and our classification became more accurate. However, we are likely missing some nuance in our classification of language.

We also don't have complete information about customers--only a subset of customers leave reviews, and on those reviews only some leave information about their skin type or where they're from.  If we had more complete data, we could have perhaps trained our sentiment analysis algorithm better and had more data to present about Yesstyle's customer base.

## Extensions of analysis/areas for more research
If we had been able to scrape more comments and provide supervision for our sentiment analysis program, we could have perhaps trained its classification to be more accurate. Instead, we were limited to a built-in sentiment analysis feature in an NLP package.

Additionally, if we had more complete data on product sales, we could have mined valuable insights into what makes certain products sell more. We also could have constructed a regression to find how much different features contribute to price.

## Source of datasets
We scraped the top rated sunscreens from [yesstyle.com](yesstyle.com), including product information and customer reviews.


## Reproducibility
In order to rerun the analysis, you will need to install the requirements which contains all the necessary packages, and then run the files in a certain order.

In order to install the requirements, you will need to run "pip3 install -r requirements.txt"

Once these pacakges are installed, the order of running the files is as follows:

These first two scripts are used to scrape the initial data from YesStyle for product listings and reviews. These scripts are not neccessary to reproduce our analysis as the final dataset is included in the data folder. The Selenium scraper may run into fake user issues and Google Vertex AI issues, YesStyle has a chance to detect the scraper, and reject the scraper's request for data. Because the Google Vertex AI may or may not have a browser, the Selenium Scraper may not open Chrome properly.
1. Run comment_scraper.py
2. Run get_comments.py

These scripts are meant to clean the reviews and ingredients for product listings and create our plots
3. Run skin_wreviews.py
4. Run skin_analysis.py
5. Run comment_w_rating.py
6. Run Skin_plot_and_nltk.ipynb
7. Run Skin_plot_and_nltk_regroup.ipynb
8. Run Type_and_ingredient.ipynb

9. Run the ingredients code

