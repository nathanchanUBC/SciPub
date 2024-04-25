import pandas as pd
import csv
from pathNames import cleanDataPath, confAuthPath
from ubc_dept import isUBC, standard_name

data = pd.read_csv(cleanDataPath)
data.sort_values(['Title'], axis=0, inplace=True)
articles = data[['Author', 'Manual Tags', 'Item Type', 'Publication Title']].dropna()

conf_auth = {}

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
            if title not in conf_auth:
                conf_auth[title] = pub_authors
            else:
                conf_auth[title].extend(pub_authors)

with open(confAuthPath, 'w', newline='' ) as file:
    writer = csv.writer(file)
    field = ["Conference Title", "Author"]
    writer.writerow(field)
    for conf, auth in conf_auth.items():
        for a in auth:
            if isUBC(a):
                writer.writerow([conf,a])
        