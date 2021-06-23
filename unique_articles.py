from more_itertools import unique_everseen


with open('scraped_articles_SABC_2_SA_pages_491.tsv','r', errors="ignore") as f, open('1_unique.tsv','w') as out_file:
    out_file.writelines(unique_everseen(f))