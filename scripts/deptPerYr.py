import pandas as pd
import csv

from pathNames import cleanDataPath, deptPerYrPath

data = pd.read_csv(cleanDataPath)
data.sort_values(['Title'], axis=0, inplace=True)
articles = data[['Author', 'Manual Tags', 'Publication Year']].dropna()

dept_names = [
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
  "Microbiology and Immunology",
  "Physics and Astronomy",
  "Science Centre for Learning and Teaching Skylight",
  "Statistics"
]

years = range(2000, 2025)  # Update end year as needed

dept_counts = {}

for index, row in articles.iterrows():
    tags = row['Manual Tags']
    pub_tags = tags.split("; ")
    for tag in pub_tags: 
        if tag in dept_names:
            dept = tag
            if dept not in dept_counts:
                dept_counts[dept] = {year: 0 for year in years} 
            dept_counts[dept][row['Publication Year']] += 1  

#print(faculty_counts)  # Optional: uncomment to see internal faculty names


with open(deptPerYrPath, 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["Department", "Publication Year", "Number of Publications"]
    writer.writerow(field)

    modified_faculty_names = {
        "Science Centre for Learning and Teaching Skylight": "Science Centre for Learning and Teaching (Skylight)"
    }

    for dept, year_counts in dept_counts.items():
        display_faculty = modified_faculty_names.get(dept, dept)
        for year, count in year_counts.items():
            writer.writerow([display_faculty, year, count])

print("Department Per Year file generated!")
