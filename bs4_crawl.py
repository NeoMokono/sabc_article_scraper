from bs4 import BeautifulSoup as soup
import requests

import pandas as pd
import csv


final_df = pd.DataFrame()

sections = ["sci-tech","politics","business"]


current_section = sections[0]





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
    # print(news.a.text)
    titles.append(news.a.text)
    # print(news.p.text)
    summaries.append(news.p.text)
    
# print(links)

author = ""
date_issued = ""
article_text = ""
i = 0


for link in links:
    page = requests.get(link)
    bsobj = soup(page.content)

    date_issued = bsobj.find('span',{'class':'create'})
    author = bsobj.find('span',{'class':'author'})
    # print("date =",date_issued.text.strip())
    # print("auth =",author.text.strip())
    author = author.text.strip()
    date_issued = date_issued.text.strip()

    temp_text = ""
    for news in bsobj.findAll('div',{'class':'post-content'}):
        # print(news.text.strip())
        temp_text = temp_text + news.text.strip()+"\n"
       
    article_text = temp_text

    temp_df = pd.DataFrame(columns = ['source_URL','Title',  'Text',
                                        'Summary', 'published_date', 'Authors','Section'])
    temp_df['Authors'] = author
    temp_df['Title'] = titles[i]
    temp_df['Text'] = article_text
    temp_df['Summary'] = summaries[i]
    temp_df['published_date'] = date_issued
    temp_df['source_URL'] = link 

    temp_df['Section'] = current_section

    print(temp_df)

    temp_dictionary = {
        'Authors' : author,
        'Title' : titles[i],
        'Text' : article_text,
        'Summary' : summaries[i],
        'published_date' : date_issued,
        'source_URL':  link 
    }
    print(temp_dictionary)

    final_df = final_df.append(temp_dictionary, ignore_index = True)
    
    # Update count
    i +=1
    print("scraped = ",i)


final_df = final_df.drop_duplicates(subset=['source_URL'])
print(final_df.size)
final_df.to_csv('final2/scraped_articles_SABC_0.tsv', sep='\t')
print("done scraping..........")   