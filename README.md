# Science Publications Scripts
This repository contains a collection of small Python scripts that manipulates an exported Zotero library (in CSV format)
into CSV's that can be used for data analysis and creating visualizations in Flourish and Tableau.

# Description
The scripts that we have are:
1. clean_data.py: Cleans the Zotero import and puts it in clean_data.csv
2. authors.py: Creates a list of authors and number of publications
3. tags.py: Creates a list of tags and number of occurences
4. network_graph.py: Creates a list of nodes and edges to create a [network graph](https://public.flourish.studio/visualisation/16796700/)
5. ubc_faculty.py: Contains a list of UBC faculty, their departments, and some helper functions
6. pathNames.py: Contains 

# Getting Started
## Computer Setup
- Please have [VSCode](https://code.visualstudio.com/) and the [Python Extension](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites) installed
- Please have Git 
- Would recommend using the Rainbow CSV VSCode Extension for easier to read CSV's
## Program Setup
1. Clone this project
2. Replace the SciPub/input/data.csv with your personalized exported Zotero library (in CSV)
3. Rename the replaced file to data.csv
## Executing Program Using VSCode
1. First, run clean_data.py in VSCode by pressing the arrow symbol, "Run Python File"
2. In the SciPub/input, check that clean_data.csv has been updated
3. Depending on the data you require, run the respective scripts listed above. All generated files can be found in SciPub/output

### TODO:
- Skylight GitHub account?
- Complete instructions on how execute code
