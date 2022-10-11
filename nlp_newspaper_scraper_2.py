import newspaper
from newspaper import Article
from newspaper import Source
import pandas as pd
import csv

import nltk


# Let's say we wanted to download articles from SABC (which is a web site for South African broadcaster)
# Link of the publication (SABC). include category of news
link = "https://www.sabcnews.com/sabcnews/category/south-africa/"
gamespot = newspaper.build("https://www.sabcnews.com/sabcnews/category/south-africa/", memoize_articles = False) 

# I set memoize_articles to False, because I don't want it to cache and save the articles to memory, run after run.


# Fresh run, everytime we run execute this script essentially

final_df = pd.DataFrame()

limit = 2000
# limit = 5
count = 0
count_no_section =0
i = 1
while i<600:
    gamespot = newspaper.build(link, memoize_articles = False)
    for each_article in gamespot.articles:
        if count > limit: # Lets have a limit, so it doesnt take too long when you're
                break         # running the code. NOTE: You may not want to use a limit

        try:
            each_article.download()
            each_article.parse()
            each_article.nlp()
        except:
            final_df.to_csv('scraped_articles_SABC_final_interrupt_SA_pages.tsv', sep='\t')
            print("interrupted scraping..........",count_no_section)
            break
        

        temp_df = pd.DataFrame(columns = ['source_URL','Title',  'Text',
                                        'Summary', 'published_date', 'Authors','Section'])

        temp_df['Authors'] = each_article.authors
        temp_df['Title'] = each_article.title
        temp_df['Text'] = each_article.text
        temp_df['Summary'] = each_article.summary
        temp_df['published_date'] = each_article.publish_date
        temp_df['source_URL'] = each_article.url
        # temp_df['Source'] = each_article.source_url
        try:
            temp_df['Section'] = each_article.meta_data['article']['section']
            print(each_article.meta_data['article']['section'])
        except:
            temp_df['Section'] = "Undefined"
            count_no_section += 1

        #Unique articles

        # if temp_df in final_df.values:
        #     print(temp_df,"found")
        # else:
        #     final_df = final_df.append(temp_df, ignore_index = True)
        final_df = final_df.append(temp_df, ignore_index = True)    
        # Update count
        count +=1
        print("scraped = ",count) 

    print("df size ==",len(final_df))
    i +=1
    link = "https://www.sabcnews.com/sabcnews/category/south-africa/page/"+str(i)+"/"
    final_df = final_df.drop_duplicates(subset=['source_URL'])
    final_df.to_csv('output/articles_SABC_SA_pages_'+str(i)+'.tsv', sep='\t')
    print("done scraping..........",i)


# From here you can export this Pandas DataFrame to a csv file
# final_df.to_csv('my_scraped_articles_SABC6.csv')
final_df = final_df.drop_duplicates(subset=['source_URL'])
final_df.to_csv('output/articles_SABC_final_SA_pages.tsv', sep='\t')
print("done scraping..........",count_no_section)

# csv.writer(open('scraped_articles_SABC_7.tsv', 'w+'), delimiter='\t').writerows(csv.reader(open("my_scraped_articles_SABC6.csv", encoding="utf8",errors="ignore")))
# print("DONE.....")