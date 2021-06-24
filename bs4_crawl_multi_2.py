from bs4 import BeautifulSoup as soup
import requests

import pandas as pd
import csv


final_df = pd.DataFrame()

# sections = ["south-africa", "africa", "world", "lifestyle", "sport","sci-tech","politics","business"]

sections = ["sci-tech","politics","business"]


current_section = sections[0]


link = "https://www.sabcnews.com/sabcnews/category/south-africa/"

count = 2
limit = 100
pages = 1
for sec in sections:
    current_section = sec
    pages = 1
    while pages<15:
        pages +=1
        nbc_url="https://www.sabcnews.com/sabcnews/category/"+current_section+"/page/"+str(pages)+"/"



        r = requests.get(nbc_url)

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

            temp_dictionary = {
                'Authors' : author,
                'Title' : titles[i],
                'Text' : article_text,
                'Summary' : summaries[i],
                'published_date' : date_issued,
                'source_URL':  link 
            }
            # print(temp_dictionary)

            final_df = final_df.append(temp_dictionary, ignore_index = True)
            
            # Update count
            i +=1
            print("scraped = ",i)


        final_df = final_df.drop_duplicates(subset=['source_URL'])
        # print(final_df.size)
    final_df.to_csv('final3/scraped_'+current_section+'_SABC_'+str(pages)+'.tsv', sep='\t')


print("done scraping..........")   