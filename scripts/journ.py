import pandas as pd
import csv
from pathNames import cleanDataPath, journPath, jounrOtherPath, journAuthPath
from ubc_dept import groupOther, otherDict, standard_name

data = pd.read_csv(cleanDataPath)
data.sort_values(['Title'], axis=0, inplace=True)
articles = data[['Author', 'Manual Tags', 'Item Type', 'Publication Title']].dropna()

journ_dict = {}
journ_authDict = {}
authCount = {}

for index, row in articles.iterrows():
    pubTitle = row['Publication Title'].title()
    pubTitles = pubTitle.split("; ")
    authors = row['Author']
    pub_authors = authors.split('; ')
    type = row['Item Type']
    for x in range(len(pub_authors)):
        pub_authors[x] = standard_name(pub_authors[x])
    isJourn = True if type == 'journalArticle' else False
    
    if isJourn:
        for title in pubTitles:
            if title not in journ_dict:
                journ_dict[title] =1
                journ_authDict[title] = pub_authors
            else:
                journ_dict[title] +=1
                journ_authDict[title].extend(pub_authors)
                
jounrOtherDict = otherDict(journ_dict)

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

with open(journAuthPath, 'w', newline='' ) as file:
    writer = csv.writer(file)
    field = ["Journal Title", "Author", "Count"]
    writer.writerow(field)
    for journ, auths in journ_authDict.items():
        for auth in auths:
            if auth not in authCount:
                authCount[auth] = 1
            else:
                authCount[auth] +=1
        #print(authCount)        
        for authorPrint in authCount:
            writer.writerow([journ,authorPrint, authCount[authorPrint]])
        
        authCount = {}
print("Journal count generated")