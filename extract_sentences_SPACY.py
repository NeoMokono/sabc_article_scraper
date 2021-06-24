import pandas as pd
import csv

import spacy

nlp = spacy.load('en_core_web_sm')

final_df = pd.DataFrame()
dataset_df_1 = pd.read_csv('final3/articles_SABC_final_SA2.tsv', sep='\t', header=0)

print(dataset_df_1.size)
print(dataset_df_1.shape[0])
print(dataset_df_1.shape[1])

col_texts_list = dataset_df_1['Text'].tolist()

print(len(col_texts_list))

sentences = []

limit = 2
i = 0
for article_text in col_texts_list:
    if limit<i:
        break
    i +=1
    encoded_string = article_text.encode("ascii", "ignore")
    decode_string = encoded_string.decode()
    tokens = nlp(decode_string)
    for t in tokens.sents:
        print (t.text.strip() , "\n")
        
        sentences.append([t.text.strip() ,""])

final_df = pd.DataFrame(columns=['Sentence', 'Translation'], data=sentences)

final_df = final_df.drop_duplicates(subset=['Sentence'])

final_df.to_csv('final3/sentences_SABC_STACY_1.tsv', sep='\t')
print("done list of sentences..........",i)
