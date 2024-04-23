import pandas as pd
import csv
from pathNames import cleanDataPath, journPath, jounrOtherPath
from ubc_dept import groupOther, otherDict

data = pd.read_csv(cleanDataPath)
data.sort_values(['Title'], axis=0, inplace=True)
articles = data[['Author', 'Manual Tags', 'Item Type', 'Publication Title']].dropna()

journ_dict = {}


for index, row in articles.iterrows():
    pubTitle = row['Publication Title'].title()
    pubTitles = pubTitle.split("; ")
    type = row['Item Type']

    isConf = True if type == 'journalArticle' else False
    
    if isConf:
        for title in pubTitles:
            if title in journ_dict:
                journ_dict[title] +=1
            else:
                journ_dict[title] =1
                
jounrOtherDict = otherDict(journ_dict)
#Uncomment if want to group single count under "Other"
journ_dict = groupOther(journ_dict)

with open(journPath, 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Journal Title", "Count of Publication Title"]
    writer.writerow(field)
    for title, count in journ_dict.items():
        writer.writerow([title, count])

with open(jounrOtherPath, 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Journal Title", "Count of Publication Title"]
    writer.writerow(field)
    for title, count in jounrOtherDict.items():
        writer.writerow([title, count])

print("Journal count generated")