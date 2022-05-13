# JSON Derulo Project Report

## Goal of analysis
Sunscreens manufactured for the American market are substantially lacking in both appeal and protection. Because of the strict regulations the FDA places on sunscreen filters (the active ingredients in sunscreens), the United States has a limited offerings in terms of sun protection. Many of these approved ingredients cannot obtain the level of protection offered by foreign sunscreens. In fact, a study conducted Environmental Working Group of 446 American sunscreens found that close to two-thirds of them would fail to meet European Union standards for adaquate UVA protection. 

Sunscreens on the Korean and Japanese market are noted for both their high protection and their cosmetic elegance, attracting skincare fanatics around the world. Because of the difficulty associated with importing these sunscreens, many companies have been created just to cater to individuals wishing to have a reliable way to obtain Japanese and Korean skincare. This project focuses on the Hong Kong-based 🇭🇰 yesstyle.com. 

As a group that regularly uses foreign sunscreens, we were interested in investigating this site for a number of reasons: 

1. Scraping sunscreen ingredients.
    - We wanted to do a simple statistical analysis of the filters lsited in the best selling sunscreens on yesstyle.com. 
    - This gives us answers to a couple of questions: What sunscreen filters are attracting foreign consumers? What are the most popular
    filters used in Korean and Japanese formulas? 

2. Scraping customer reviews.
    - YesStyle has a robust review system, with some products getting thousands of reviews; even allowing users to list their age and 
    skin-type (Dry, Oily, Combination). We wanted to scrape these reviews to gain insight on common complaints and praises used by the
    skincare community. We wanted to assess the frequency of such phrases like: "drying", "moisturizing", "emollient", etc. 
    - Scraping reviews has another purpose for this project as well. We used the text of the scraped reviews to conduct a sentiment
    analysis.
    **(Need to fill in this section more).**

This project gives us a harder challenge than our midterm project, not only in terms of webscraping, but also in terms of our statistical analysis. We're interested consumer behavior and sentiments, looking at a niche and picky market segment that heavily relies on the opinions of fellow skincare enthusiasts to make purchasing decisions. 


## Methodology
data collection methods - documentation of data (all relevant columns/features) & what isn't in data

## Description of project and findings/lack of findings:
clearly documented
supported by analysis

## Limitations of analysis
Sentiment analysis is hard to fine-tune, so we encountered errors where our Textblob algorithm could not understand the context of some customer reviews.  For example, customer reviews that had double negatives were falsely flagged as being negative.  If a reviewer were to say something like, "this product does not make me break out with acne," which is a positive review, our Textblob would see the "not" and classify it as negative.  We were able to fix this problem by simplifying our review classes to three levels of sentiment where before we had five, and our classification became more accurate.  However, we are likely missing some nuance in our classification of language.

We also don't have complete information about customers--only a subset of customers leave reviews, and on those reviews only some leave information about their skin type or where they're from.  If we had more complete data, we could have perhaps trained our sentiment analysis algorithm better and had more data to present about Yesstyle's customer base.

## Extensions of analysis/areas for more research
If we had been able to scrape more comments and provide supervision for our sentiment analysis program, we could have perhaps trained its classification to be more accurate.  Instead, we were limited to a built-in sentiment analysis feature in an NLP package.

Needs more

## Source of datasets
We scraped the top rated sunscreens from yesstyle.com, including product information and customer reviews.  

## Reproducibility

