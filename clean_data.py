import pandas as pd
import re

# Read the CSV file
df = pd.read_csv('SciPub/input/data.csv')
# df = df[['Title', 'Manual Tags']]

# Define a function to remove special characters from a string
def remove_special_characters(text):
    # Convert non-string values to strings
    if not isinstance(text, str):
        text = str(text)
    # Define a regular expression pattern to match special characters
    # pattern = r'[^\w\s;-,]'
    pattern = r'[^\w\s;\-,\']'

    # Remove special characters using regex substitution
    return re.sub(pattern, '', text)

# Apply the function to each cell in the dataframe
df = df.applymap(remove_special_characters)

# Save the modified dataframe to a new CSV file
df.to_csv('SciPub/input/clean_data.csv', index=False)

# need to manually take of ğ, ı, ć in clean_data.csv
# there may also be some nan in columns Authors or Manual Tags
