import pandas as pd
import csv

from ubc_faculty import isUBC, standard_name
from pathNames import cleanDataPath, UBCAuthorWritePath, journalAuthorWritePath


data = pd.read_csv(cleanDataPath)
data.sort_values(['Title'], axis=0, inplace=True)
articles = data[['Author', 'Manual Tags', 'Item Type']].dropna()

# AUTHORS PUBLISHED (ANY TYPE) AT UBC
authors_dict = {}

for index, row in articles.iterrows():
    authors = row['Author']
    pub_authors = authors.split("; ")

    tags = row['Manual Tags']
    splitTags = tags.split("; ")
    atUBC = False if 'Pre-UBC Tenure' in splitTags else True

    if atUBC:
        for author in pub_authors:
            name = standard_name(author)
            if isUBC(name):
                if name in authors_dict:
                    authors_dict[name] += 1
                else:
                    authors_dict[name] = 1
                    

with open(UBCAuthorWritePath, 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Name", "Count"]    
    writer.writerow(field)
    for name, count in authors_dict.items():
        writer.writerow([name, count])

# AUTHORS PUBLISHED JOURNAL AT UBC
authors_dict = {}

for index, row in articles.iterrows():
    writtenBy = row['Author']
    pub_authors = writtenBy.split("; ")

    tags = row['Manual Tags']
    splitTags = tags.split("; ")
    atUBC = False if 'Pre-UBC Tenure' in splitTags else True

    type = row['Item Type']
    isJournal = True if type == 'journalArticle' else False

    if atUBC and isJournal:
        for author in pub_authors:
            name = standard_name(author)
            if isUBC(name):
                if name in authors_dict:
                    authors_dict[name] += 1
                else:
                    authors_dict[name] = 1

with open(journalAuthorWritePath, 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Name", "Count"]    
    writer.writerow(field)
    for name, count in authors_dict.items():
        writer.writerow([name, count])

print("Author file generated!")