import pandas as pd
import csv

from ubc_faculty import isUBC, standard_name, get_faculty, removeAccents
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
        for i in pub_authors:
            name = standard_name(i)
            if isUBC(name):
                if name in authors_dict:
                    authors_dict[name] += 1
                else:
                    authors_dict[name] = 1
                    

with open(UBCAuthorWritePath, 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["name", "size"]    
    writer.writerow(field)
    for i in authors_dict:
        writer.writerow([i, authors_dict[i]])

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
        for i in pub_authors:
            name = standard_name(i)
            if isUBC(name):
                if name in authors_dict:
                    authors_dict[name] += 1
                else:
                    authors_dict[name] = 1

with open(journalAuthorWritePath, 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["name", "size"]    
    writer.writerow(field)
    for i in authors_dict:
        writer.writerow([i, authors_dict[i]])

print("Author file generated!")