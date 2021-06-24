import pandas as pd
import csv

dataset_df_1 = pd.read_csv('final3/scraped_sport_SABC_15.tsv', sep='\t', header=0)

print(dataset_df_1.size)
print(dataset_df_1.shape[0])
print(dataset_df_1.shape[1])

dataset_df_2 = pd.read_csv('final3/scraped_business_SABC_15.tsv', sep='\t', header=0)


print("2...",dataset_df_2.size)
print("2...",dataset_df_2.shape[0])
print("2...",dataset_df_2.shape[1])


frames = [dataset_df_1, dataset_df_2]

result_df = pd.concat(frames)


print("3...",result_df.size)
print("3...",result_df.shape[0])
print("3...",result_df.shape[1])


final_df = result_df.drop_duplicates(subset=['source_URL'])

# final_df = result_df.drop(columns=[''])

print("4...",final_df.size)
print("4...",final_df.shape[0])
print("4...",final_df.shape[1])

arr = final_df.columns[0]
final_df.drop(final_df.columns[0], axis=1, inplace=True)
print("4...",final_df.shape[0])
print("4...",final_df.shape[1])

final_df.to_csv('final3/articles_SABC_final_SA2.tsv', sep='\t')
print("done conc..........")