import pandas as pd
import csv
from pathNames import cleanDataPath, confPath, confOtherPath, confAuthPath
from ubc_dept import groupOther, otherDict, standard_name

data = pd.read_csv(cleanDataPath)
data.sort_values(['Title'], axis=0, inplace=True)
articles = data[['Author', 'Manual Tags', 'Item Type', 'Publication Title']].dropna()

conf_dict = {}
conf_authDict = {}
authCount = {}

for index, row in articles.iterrows():
    pubTitle = row['Publication Title'].title()
    pubTitles = pubTitle.split("; ")
    authors = row['Author']
    pub_authors = authors.split("; ")
    type = row['Item Type']
    for x in range(len(pub_authors)):
        pub_authors[x] = standard_name(pub_authors[x])
    isConf = True if type == 'conferencePaper' else False
    
    if isConf:
        for title in pubTitles:
            if title not in conf_dict:
                conf_dict[title] =1
                conf_authDict[title] = pub_authors
            else:
                conf_dict[title] +=1
                conf_authDict[title].extend(pub_authors)

otherConfdict = otherDict(conf_dict)

conf_dict = groupOther(conf_dict)



with open(confPath, 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Conference Title", "Number of Publications"]
    writer.writerow(field)
    for title, count in conf_dict.items():
        writer.writerow([title,count])


with open(confOtherPath, 'w', newline = '') as file:
    writer = csv.writer(file)
    field = ["Conference Title", "Number of Publications"]
    writer.writerow(field)
    for title, count in otherConfdict.items():
        writer.writerow([title,count])

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
        #print(authCount)        
        for authorPrint in authCount:
            writer.writerow([conf,authorPrint, authCount[authorPrint]])
        
        authCount = {}
print("Conference file generated!")