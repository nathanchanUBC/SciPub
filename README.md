# Science Publications Scripts
This repository contains a collection of small Python scripts that manipulates an exported Zotero library (in CSV format)
into CSV's that can be used for data analysis and creating visualizations in Flourish and Tableau.

# Description
The scripts that we have are:
1. clean_data.py: Cleans the Zotero import and puts it in clean_data.csv
2. authors.py: Creates a file of authors and number of publications
3. tags.py: Creates a file of tags and number of occurences
4. network_graph.py: Creates a file of nodes and edges to create a [network graph](https://public.flourish.studio/visualisation/16796700/)
5. ubc_faculty.py: Contains a list of UBC faculty, their departments, and some helper functions
6. conf.py: Creates a file of conference papers and number of occurences
7. journ.py: Creates a file of contributions by each science faculty per year of journal articles and number of occurences
8. facPerYr.py: Creates a file of contributions by each science faculty per year
9. pathNames.py: Contains the absolute paths of all files used
10. runAll.py: Running this file generates all files listed above
   

# Getting Started
## Computer Setup
- Please have [VSCode](https://code.visualstudio.com/) and the [Python Extension](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites) installed
- Please have [Git](https://git-scm.com/downloads) installed
- Have the following packages installed: [Pandas](https://pypi.org/project/pandas/), [Unidecode](https://pypi.org/project/Unidecode/)
- We recommend using the Rainbow CSV VSCode Extension for CSV readability (*optional*)
## Program Setup
1. [Clone this project](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)
 ```
git clone https://github.com/scienceltrs/SciPub.git
```  
2. Replace the SciPub/input/data.csv with your personalized exported Zotero library (in CSV). This is the raw data
3. Rename the replaced file to data.csv

## Executing Program Using VSCode
1. Open clean_data.py in VSCode then execute the script by pressing the arrow icon, "Run Python File"
2. In SciPub/input, check that clean_data.csv has been updated
3. Depending on the data you require, run the respective scripts listed above. All generated files can be found in SciPub/output
4. Alternatively, you can run "SciPub/runAll.py" to clean then generate all files

## Execute Program Using Terminal
1. Open terminal. Using ```cd```, change the directory to the cloned SciPub folder
2. Use ```pwd``` to verify your current directory
3. Once in the SciPub folder, type in terminal ```python scripts/fileName.py``` to execute the desired script

## Tableau Files
The following files are used in Tableau:
- conf.csv
- facPerYr.csv
- journ.csv
- pubTags.csv
  
## Flourish Files
The following files are uesd in Flourish:
- author_edges.csv
- author_nodes.csv

## Closing Remarks
- If there are conflicitng name formats (excluding accents) in the cleaned_data.csv, standardize them in the dictionary, standardizedNames, in SciPub/ubc_faculty.py
- Make sure that the key doesn't include any accents otherwise they won't appear in the generated csvs!
- If there are new authors, you must add their (standardized) name to their respective faculty list in "SciPub/ubc_faculty.py" 


