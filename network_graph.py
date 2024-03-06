import pandas as pd
import csv

from ubc_faculty import isUBC, get_faculty, standard_name
from pathNames import cleanDataPath, nodeWritePath, edgeWritePath

## Network graph here: https://public.flourish.studio/visualisation/16796700/
data = pd.read_csv(cleanDataPath)
data.sort_values(['Author'], axis=0, inplace=True)
authors = data['Author'].dropna()

## List of Nodes and Sizes
authors_dict = {}

for item in authors:
    pub_authors = item.split('; ')
    for i in pub_authors:
        name = standard_name(i)
        if name in authors_dict:
            authors_dict[name] += 1
        else:
            authors_dict[name] = 1


with open(nodeWritePath, 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["name", "size", "faculty"]    
    writer.writerow(field)
    for i in authors_dict:
        writer.writerow([i, authors_dict[i], get_faculty(i)])
print("Nodes list created")

## List of Edges (weights done by graphing software)
authors_list = []

for item in authors:
    names = item.split('; ')
    n = len(names)
    for i in range(n-1):
        for j in range(i+1, n):
            name1 = standard_name(names[i])
            name2 = standard_name(names[j])
            if (isUBC(name1) or isUBC(name2)):
                edge = [name1, name2]
                authors_list.append(edge)
                
with open(edgeWritePath, 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["source", "target"]    
    writer.writerow(field)
    for i in authors_list:
        writer.writerow([i[0], i[1]])
print("Edge list created")
