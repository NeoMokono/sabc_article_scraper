import pandas as pd
import csv

dataset_df_1 = pd.read_csv('final6extension/scraped_africa_SABC_150.tsv', sep='\t', header=0)

print(dataset_df_1.size)
print(dataset_df_1.shape[0])
print(dataset_df_1.shape[1])

dataset_df_2 = pd.read_csv('final6extension/scraped_business_SABC_150.tsv', sep='\t', header=0)


print("2...",dataset_df_2.size)
print("2...",dataset_df_2.shape[0])
print("2...",dataset_df_2.shape[1])


dataset_df_3 = pd.read_csv('final6extension/scraped_lifestyle_SABC_150.tsv', sep='\t', header=0)


print("3...",dataset_df_3.size)
print("3...",dataset_df_3.shape[0])
print("3...",dataset_df_3.shape[1])

dataset_df_4 = pd.read_csv('final6extension/scraped_politics_SABC_150.tsv', sep='\t', header=0)


print("4...",dataset_df_4.size)
print("4...",dataset_df_4.shape[0])
print("4...",dataset_df_4.shape[1])

dataset_df_5 = pd.read_csv('final6extension/scraped_sci-tech_SABC_150.tsv', sep='\t', header=0)


print("5...",dataset_df_5.size)
print("5...",dataset_df_5.shape[0])
print("5...",dataset_df_5.shape[1])

dataset_df_6 = pd.read_csv('final6extension/scraped_south-africa_SABC_150.tsv', sep='\t', header=0)


print("6...",dataset_df_6.size)
print("6...",dataset_df_6.shape[0])
print("6...",dataset_df_6.shape[1])

dataset_df_7 = pd.read_csv('final6extension/scraped_sport_SABC_150.tsv', sep='\t', header=0)


print("7...",dataset_df_7.size)
print("7...",dataset_df_7.shape[0])
print("7...",dataset_df_7.shape[1])

dataset_df_8 = pd.read_csv('final6extension/scraped_world_SABC_150.tsv', sep='\t', header=0)


print("8...",dataset_df_8.size)
print("8...",dataset_df_8.shape[0])
print("8...",dataset_df_8.shape[1])




frames = [dataset_df_1, dataset_df_2,dataset_df_3, dataset_df_4,dataset_df_5, dataset_df_6,dataset_df_7, dataset_df_8]

result_df = pd.concat(frames)


print("3...",result_df.size)
print("3...",result_df.shape[0])
print("3...",result_df.shape[1])


final_df = result_df.drop_duplicates(subset=['source_URL'])

# for index, row in final_df.iterrows():
#     print(row['Summary'], row['Text'])
#     article_text = row['Text']
#     article_summary = row['Summary']

#     encoded_string = article_text.encode("ascii", "ignore")
#     decode_string = encoded_string.decode()
#     final_df['Text'][index] = decode_string

#     encoded_string = article_summary.encode("ascii", "ignore")
#     decode_string = encoded_string.decode()
#     final_df['Summary'][index] = decode_string

for i, row in final_df.iterrows():
    article_text = row['Text']
    article_summary = row['Summary']
    # print(row['Summary'])
    # print(row['Text'])
    
    try:
        encoded_string = article_text.encode("ascii", "ignore")
        decode_string = encoded_string.decode() 
    except:
        encoded_string = "N/A"
        decode_string = "N/A"
     
    final_df.at[i,'Text'] = decode_string
    try:
        encoded_string = article_summary.encode("ascii", "ignore")
        decode_string = encoded_string.decode()
    except:
        encoded_string = "N/A"
        decode_string = "N/A" 
    final_df.at[i,'Summary'] = decode_string

# final_df = result_df.drop(columns=[''])

print("4...",final_df.size)
print("4...",final_df.shape[0])
print("4...",final_df.shape[1])

arr = final_df.columns[0]
final_df.drop(final_df.columns[0], axis=1, inplace=True)
print("4...",final_df.shape[0])
print("4...",final_df.shape[1])

final_df.to_csv('final6extension/articles_SABC_decoded_2_.tsv', sep='\t')
print("done conc..........")