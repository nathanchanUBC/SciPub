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
  "Science Centre for Learning and Teaching Skylight",
  "Statistics"
]

years = range(2000, 2025)  # Update end year

faculty_counts = {}

for index, row in articles.iterrows():
    tags = row['Manual Tags']
    pub_tags = tags.split("; ")
    for pub_tag in pub_tags: 
        if pub_tag in faculty_names:
            faculty = pub_tag
            if faculty not in faculty_counts:
                faculty_counts[faculty] = {year: 0 for year in years} 
            faculty_counts[faculty][row['Publication Year']] += 1  

#print(faculty_counts)  # Optional: uncomment to see internal faculty names


with open(facPerYrPath, 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Faculty", "Year", "Count"]
    writer.writerow(field)

    modified_faculty_names = {
        "Science Centre for Learning and Teaching Skylight": "Science Centre for Learning and Teaching (Skylight)"
    }

    for faculty, year_counts in faculty_counts.items():
        display_faculty = modified_faculty_names.get(faculty, faculty)
        for year, count in year_counts.items():
            writer.writerow([display_faculty, year, count])

print("Faculty Per Year file generated!")
