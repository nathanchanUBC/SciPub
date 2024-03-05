import pandas as pd
import re

# Read the CSV file
inputDataPath = 'SciPub/input/data.csv'
df = pd.read_csv(inputDataPath)

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
df = df.applymap(remove_special_characters)

# Save the modified dataframe to a new CSV file
cleanedDataPath = 'SciPub/input/clean_data.csv'
df.to_csv(cleanedDataPath, index=False)
print("Data cleaned")

# there may also be some nan in columns Authors or Manual Tags
