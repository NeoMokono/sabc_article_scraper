import pandas as pd
import csv
import nltk

final_df = pd.DataFrame()
dataset_df_1 = pd.read_csv('final6extension/articles_SABC_decoded_2_.tsv', sep='\t', header=0)

print(dataset_df_1.size)
print(dataset_df_1.shape[0])
print(dataset_df_1.shape[1])

col_texts_list = dataset_df_1['Text'].tolist()

print(len(col_texts_list))

sentences = []

limit = 20000000
i = 0
for article_text in col_texts_list:
    if limit<i:
        break
    i +=1
    try:

        encoded_string = article_text.encode("ascii", "ignore")
        decode_string = encoded_string.decode()
    except:
        decode_string = "N/A"    
    tokens = nltk.sent_tokenize(decode_string)
    for t in tokens:
        print (t, "\n")
        arr_words = t.split()
        if len(arr_words)>2:
        
            sentences.append([t,""])

final_df = pd.DataFrame(columns=['Sentence', 'Translation'], data=sentences)

final_df = final_df.drop_duplicates(subset=['Sentence'])

final_df.to_csv('final6extension/sentences/sentences_SABC_nltk_1.tsv', sep='\t')
print("done list of sentences..........",i)

