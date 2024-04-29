import pandas as pd
import csv
from pathNames import cleanDataPath, itemTypePath

data = pd.read_csv(cleanDataPath)
data.sort_values(['Title'], axis=0, inplace=True)
articles = data[['Item Type','Publication Year']].dropna()

itemTypeCountDict = {}
years = range(2000,2025) # Update end year as needed
for index, row in articles.iterrows():
    type = row['Item Type']
    itemsSplit = type.split("; ")
    for type in itemsSplit:
        if type not in itemTypeCountDict:
            itemTypeCountDict[type] = {year:0 for year in years}
        itemTypeCountDict[type][row['Publication Year']] +=1

modifiedTypeName = {
    "book": "Book",
    "bookSection": "Book Section",
    "conferencePaper": "Conference Paper/Proceeding",
    "journalArticle": "Journal Article",
    "preprint": "Preprint",
    "thesis": "Thesis",
    "webpage": "Webpage",
    "presentation": "Presentation"
    }
with open(itemTypePath, 'w', newline='' ) as file:
    writer = csv.writer(file)
    field = ["Publication Type", "Publication Year", "Number of Publications"]
    writer.writerow(field)

    for pubItem, year_counts in itemTypeCountDict.items():
        dispType = modifiedTypeName.get(pubItem, pubItem)
        for year, count in year_counts.items():
            writer.writerow([dispType,year, count])

print("Item Type file generated")
