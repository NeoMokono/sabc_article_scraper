from bs4 import BeautifulSoup as soup
import requests

import pandas as pd
import csv

sections = ["south-africa", "africa", "world", "lifestyle", "sport","sci-tech","politics","business"]


temp_df = pd.DataFrame(columns = ['source_URL','Title',  'Text',
                                    'Summary', 'published_date', 'Authors','Section'])



nbc_url='https://www.sabcnews.com/sabcnews/category/south-africa/page/2/'
r = requests.get('https://www.sabcnews.com/sabcnews/category/south-africa/page/2/')

b = soup(r.content,'lxml')


# for news in b.findAll('h2'):
#     print(news.text)



links = []
titles = []
summaries = []


# for news in b.findAll('span',{'class':'sabc_cat_list_item_title'}):
for news in b.findAll('div',{'class':'sabc_cat_list_item'}):
    links.append(news.a['href'])
    print(news.a.text)
    titles.append(news.a.text)
    print(news.p.text)
    summaries.append(news.p.text)
    
print(links)

author = ""
date_issued = ""
article_text = ""
i = 0
for link in links:
    page = requests.get(link)
    bsobj = soup(page.content)

    date_issued = bsobj.find('span',{'class':'create'})
    author = bsobj.find('span',{'class':'author'})
    print("date =",date_issued.text.strip())
    print("auth =",author.text.strip())
    for news in bsobj.findAll('div',{'class':'post-content'}):
        print(news.text.strip())
        article_text = news.text.strip()



    temp_df['Authors'] = author
    temp_df['Title'] = titles[i]
    temp_df['Text'] = article_text
    temp_df['Summary'] = each_article.summary
    temp_df['published_date'] = date_issued
    temp_df['source_URL'] = link 