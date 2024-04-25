import pandas as pd
import re
from pathNames import rawDataPath, cleanDataPath
# Read the CSV file

df = pd.read_csv(rawDataPath)

# Define a function to remove special characters from a string
def remove_special_characters(text):
    # Convert non-string values to strings
    if not isinstance(text, str):
        text = str(text)
    # Define a regular expression pattern to match special characters
    pattern = r'[^\w\s;\-,\']'

    # Remove special characters using regex substitution
    return re.sub(pattern, '', text)

# Apply the function to each cell in the dataframe
df = df.map(remove_special_characters)
#df = df.map(removeAccents)
# Save the modified dataframe to a new CSV file

df.to_csv(cleanDataPath, index=False)

print("Data cleaned!")

# there may also be some nan in columns Authors or Manual Tags
