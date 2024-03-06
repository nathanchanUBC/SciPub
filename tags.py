import pandas as pd
import csv
from pathNames import cleanDataPath, tagsPath

data = pd.read_csv(cleanDataPath)
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


with open(tagsPath, 'w', newline='' ) as file:
    writer = csv.writer(file)
    field = ["Tag", "Size"]
    writer.writerow(field)
    for i in tags_dict:
        writer.writerow([i, tags_dict[i]])