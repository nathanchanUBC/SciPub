import pandas as pd
import csv
from pathNames import cleanDataPath, journAuthPath
from ubc_dept import isUBC, standard_name

data = pd.read_csv(cleanDataPath)
data.sort_values(['Title'], axis=0, inplace=True)
articles = data[['Author', 'Manual Tags', 'Item Type', 'Publication Title']].dropna()

journ_authDict = {}

for index, row in articles.iterrows():
    pubTitle = row['Publication Title'].title()
    authors = row['Author']
    pubTitles = pubTitle.split("; ")
    pub_authors = authors.split('; ')
    for x in range(len(pub_authors)):
        pub_authors[x] = standard_name(pub_authors[x])
    type = row['Item Type']

    isJourn = True if type == 'journalArticle' else False
    
    if isJourn:
        for title in pubTitles:
            if title not in journ_authDict:
                journ_authDict[title] = pub_authors
            else:
                journ_authDict[title].extend(pub_authors)

authCount = {}
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
        print(authCount)        
        for authorPrint in authCount:
            writer.writerow([journ,authorPrint, authCount[authorPrint]])
        
        authCount = {}

