import pandas as pd
import csv

import spacy

nlp = spacy.load('en_core_web_sm')

final_df = pd.DataFrame()
dataset_df_1 = pd.read_csv('final6extension/articles_SABC_decoded_2_.tsv', sep='\t', header=0)

print(dataset_df_1.size)
print(dataset_df_1.shape[0])
print(dataset_df_1.shape[1])

col_texts_list = dataset_df_1['Text'].tolist()

print(len(col_texts_list))

sentences = []
sentences_1D = []

limit = 2000000
i = 0
for article_text in col_texts_list:
    if limit<i:
        break
    i +=1
    try:
        encoded_string = article_text.encode("ascii", "ignore")
        decode_string = encoded_string.decode()
    except:
        encoded_string = "N/A"
        decode_string = "N/A"
    tokens = nlp(decode_string)
    for t in tokens.sents:
        print (t.text.strip() , "\n")
        final_sentence = t.text.strip()
        arr_words = final_sentence.split()
        if len(arr_words)>2:
            sentences.append([final_sentence ,""])
            sentences_1D.append(final_sentence)

final_df = pd.DataFrame(columns=['Sentence', 'Translation'], data=sentences)
final_1D_df = pd.DataFrame(sentences_1D)

final_df = final_df.drop_duplicates(subset=['Sentence'])

final_1D_df = final_1D_df.drop_duplicates()

final_df.to_csv('final6extension/sentences/sentences_SABC_STACY_1.tsv', sep='\t')

final_1D_df.to_csv('final6extension/sentences/sentences_SABC_STACY_1D.tsv', sep='\t')
print("done list of sentences..........",i)
