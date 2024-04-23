import pandas as pd
import csv

from ubc_dept import isUBC, get_dept, standard_name
from pathNames import cleanDataPath, UBCAuthorWritePath

data = pd.read_csv(cleanDataPath)
data.sort_values(['Author'], axis=0, inplace=True)
authors = data['Author'].dropna()

authors_dict = {}

for item in authors:
    pub_authors = item.split('; ')
    for i in pub_authors:
        name = standard_name(i)
        if name in authors_dict:
            authors_dict[name] += 1
        else:
            authors_dict[name] = 1

with open(UBCAuthorWritePath, 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Author", "Count", "Department"]    
    writer.writerow(field)
    for author in authors_dict:
        if isUBC(author):
            writer.writerow([author, authors_dict[author], get_dept(author)])