import pandas as pd
import csv
from pathNames import cleanDataPath, confPath

data = pd.read_csv(cleanDataPath)
data.sort_values(['Title'], axis=0, inplace=True)
articles = data[['Author', 'Manual Tags', 'Item Type', 'Publication Title']].dropna()

conf_dict = {}


for index, row in articles.iterrows():
    pubTitle = row['Publication Title']
    pubTitles = pubTitle.split("; ")
    type = row['Item Type']

    isConf = True if type == 'conferencePaper' else False
    
    if isConf:
        for i in pubTitles:
            if i in conf_dict:
                conf_dict[i] +=1
            else:
                conf_dict[i] =1


### Uncomment lines 28-38 if want to group single counts under "Other"
# other_count = 0

# for title, count in conf_dict.items():
#     if count == 1:
#         other_count+=1

# conf_dict["Other"] = other_count

# for title, count in list(conf_dict.items()):  
#     if count == 1 and title != "Other":
#         del conf_dict[title]


with open(confPath, 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Title", "Count"]
    writer.writerow(field)
    for i in conf_dict:
        writer.writerow([i,conf_dict[i]])


print("Conference file generated!")