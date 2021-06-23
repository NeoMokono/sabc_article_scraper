import csv


csv.writer(open('scraped_articles_SABC_4.tsv', 'w+'), delimiter='\t').writerows(csv.reader(open("my_scraped_articles4_SABC.csv",errors="ignore")))
print("DONE.....")