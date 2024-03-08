import pandas as pd
import csv

from pathNames import cleanDataPath, facPerYrPath

data = pd.read_csv(cleanDataPath)
data.sort_values(['Title'], axis=0, inplace=True)
articles = data[['Author', 'Manual Tags', 'Publication Year']].dropna()
faculty_names = [
  "Biology",
  "Chemistry",
  "Computer Science",
  "Data Science",
  "Earth, Ocean and Atmospheric Sciences",
  "Geoscience",
  "Institute for Oceans and Fisheries",
  "Institute for Resources, Environment and Sustainability",
  "Mathematics",
  "Michael Smith Laboratories",
  "Microbiology",
  "Physics and Astronomy",
  "Science Centre for Learning and Teaching (Skylight)",
  "Statistics"
]

years = range(2000, 2025) #update end year

faculty_counts = {}

for index, row in articles.iterrows():
    tags = row['Manual Tags']
    pub_tags = tags.split("; ")
    for pub_tag in pub_tags: 
        if pub_tag in faculty_names:
            faculty = pub_tag  # Store the matched faculty name (as-is)
            if faculty not in faculty_counts:
                faculty_counts[faculty] = {year: 0 for year in years}  # Initialize dictionary for faculty
            faculty_counts[faculty][row['Publication Year']] += 1  # Increment count for publication year
#print(faculty_counts)


with open(facPerYrPath, 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Faculty", "Year", "Count"]
    writer.writerow(field)

    # Iterate through faculty and year-count dictionaries:
    for faculty, year_counts in faculty_counts.items():
        for year, count in year_counts.items():
            writer.writerow([faculty, year, count])

print("File generated")
