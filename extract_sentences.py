import pandas as pd
import csv
import nltk

final_df = pd.DataFrame()
dataset_df_1 = pd.read_csv('final3/articles_SABC_final_SA2.tsv', sep='\t', header=0)

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
    encoded_string = article_text.encode("ascii", "ignore")
    decode_string = encoded_string.decode()
    tokens = nltk.sent_tokenize(decode_string)
    for t in tokens:
        print (t, "\n")
        
        sentences.append([t,""])

final_df = pd.DataFrame(columns=['Sentence', 'Translation'], data=sentences)

final_df = final_df.drop_duplicates(subset=['Sentence'])

final_df.to_csv('final3/sentences_SABC_v2_1.tsv', sep='\t')
print("done list of sentences..........",i)

# dataset_df_2 = pd.read_csv('final3/scraped_business_SABC_15.tsv', sep='\t', header=0)


# print("2...",dataset_df_2.size)
# print("2...",dataset_df_2.shape[0])
# print("2...",dataset_df_2.shape[1])


# frames = [dataset_df_1, dataset_df_2]

# result_df = pd.concat(frames)


# print("3...",result_df.size)
# print("3...",result_df.shape[0])
# print("3...",result_df.shape[1])


# final_df = result_df.drop_duplicates(subset=['source_URL'])

# # final_df = result_df.drop(columns=[''])

# print("4...",final_df.size)
# print("4...",final_df.shape[0])
# print("4...",final_df.shape[1])

# arr = final_df.columns[0]
# final_df.drop(final_df.columns[0], axis=1, inplace=True)
# print("4...",final_df.shape[0])
# print("4...",final_df.shape[1])

# final_df.to_csv('final3/articles_SABC_final_SA2.tsv', sep='\t')
# print("done conc..........")