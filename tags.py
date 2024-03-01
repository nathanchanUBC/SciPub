import pandas as pd
import csv

dataPath = 'SciPub/input/clean_data.csv' #change this to personal file path
data = pd.read_csv(dataPath)
data.sort_values(['Title'], axis=0, inplace=True)
articles = data[['Author', 'Manual Tags', 'Item Type']].dropna()

tags_dict = {}
for index, row in articles.iterrows():
    tags = row['Manual Tags']
    pub_tags = tags.split("; ")
    for i in pub_tags:
        if i in tags_dict:
            tags_dict[i] +=1
        else:
            tags_dict[i] = 1

writePath = 'SciPub/output/pubTags.csv' #change this to personal file path
with open(writePath, 'w', newline='' ) as file:
    writer = csv.writer(file)
    field = ["Tag", "Size"]
    writer.writerow(field)
    for i in tags_dict:
        writer.writerow([i, tags_dict[i]])