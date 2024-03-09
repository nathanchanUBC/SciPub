import pandas as pd
import csv
import string
from pathNames import cleanDataPath, journPath
from ubc_faculty import groupOther

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
        for i in pubTitles:
            if i in journ_dict:
                journ_dict[i] +=1
            else:
                journ_dict[i] =1
                
#Uncomment if want to group single count under "Other"
journ_dict = groupOther(journ_dict)

with open(journPath, 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Title", "Count"]
    writer.writerow(field)
    for i in journ_dict:
        writer.writerow([i,journ_dict[i]])

print("Journal count generated")