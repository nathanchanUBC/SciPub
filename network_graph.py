import pandas as pd
import csv

from ubc_faculty import isUBC, get_faculty, standard_name

## Network graph here: https://public.flourish.studio/visualisation/16796700/

data = pd.read_csv('SciPub/input/clean_data.csv')
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


with open('SciPub/output/author_nodes.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["name", "size", "faculty"]    
    writer.writerow(field)
    for i in authors_dict:
        writer.writerow([i, authors_dict[i], get_faculty(i)])

## List of Edges (weights done by graphing software)
authors_list = []

for item in authors:
    names = item.split('; ')
    print(names)
#     for i in range(1, len(names)):
#         if names[i][0] == ' ':
#             names[i] = names[i][1:]
#     for i in range(len(names)-1):
#         for j in range(i+1, len(names)):
#             if isUBC(standard_name(names[i])) or isUBC(standard_name(names[j])):
#                 edge = [standard_name(names[i]), standard_name(names[j])]
#                 authors_list.append(edge)

# with open('SciPub/output/author_edges.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     field = ["source", "target"]    
#     writer.writerow(field)
#     for i in authors_list:
#         writer.writerow([i[0], i[1]])
