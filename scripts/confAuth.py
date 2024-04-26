import pandas as pd
import csv
from pathNames import cleanDataPath, confAuthPath
from ubc_dept import standard_name

data = pd.read_csv(cleanDataPath)
data.sort_values(['Title'], axis=0, inplace=True)
articles = data[['Author', 'Manual Tags', 'Item Type', 'Publication Title']].dropna()

conf_authDict = {}

for index, row in articles.iterrows():
    pubTitle = row['Publication Title'].title()
    authors = row['Author']
    pubTitles = pubTitle.split("; ")
    pub_authors = authors.split('; ')
    for x in range(len(pub_authors)):
        pub_authors[x] = standard_name(pub_authors[x])
    type = row['Item Type']

    isConf = True if type == 'conferencePaper' else False
    
    if isConf:
        for title in pubTitles:
            if title not in conf_authDict:
                conf_authDict[title] = pub_authors
            else:
                conf_authDict[title].extend(pub_authors)

authCount = {}
with open(confAuthPath, 'w', newline='' ) as file:
    writer = csv.writer(file)
    field = ["Conference Title", "Author", "Count"]
    writer.writerow(field)
    for conf, auths in conf_authDict.items():
        for auth in auths:
            if auth not in authCount:
                authCount[auth] = 1
            else:
                authCount[auth] +=1
        print(authCount)        
        for authorPrint in authCount:
            writer.writerow([conf,authorPrint, authCount[authorPrint]])
        
        authCount = {}

