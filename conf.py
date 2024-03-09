import pandas as pd
import csv
from pathNames import cleanDataPath, confPath
from ubc_faculty import groupOther

data = pd.read_csv(cleanDataPath)
data.sort_values(['Title'], axis=0, inplace=True)
articles = data[['Author', 'Manual Tags', 'Item Type', 'Publication Title']].dropna()

conf_dict = {}


for index, row in articles.iterrows():
    pubTitle = row['Publication Title'].title()
    pubTitles = pubTitle.split("; ")
    type = row['Item Type']

    isConf = True if type == 'conferencePaper' else False
    
    if isConf:
        for i in pubTitles:
            if i in conf_dict:
                conf_dict[i] +=1
            else:
                conf_dict[i] =1


#Uncomment if want to group single count under "Other"
conf_dict = groupOther(conf_dict)



with open(confPath, 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Title", "Count"]
    writer.writerow(field)
    for i in conf_dict:
        writer.writerow([i,conf_dict[i]])


print("Conference file generated!")