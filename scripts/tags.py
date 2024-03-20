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
    for tag in pub_tags:
        if tag in tags_dict:
            tags_dict[tag] +=1
        else:
            tags_dict[tag] = 1


with open(tagsPath, 'w', newline='' ) as file:
    writer = csv.writer(file)
    field = ["Tag", "Size"]
    writer.writerow(field)
    for tags, count in tags_dict.items():
        writer.writerow([tags,count])

print("Tags file generated")
