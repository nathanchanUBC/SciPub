import os

rawDataPath = 'input/data.csv'
cleanDataPath = 'input/clean_data.csv'

nodeWritePath = 'output/author_nodes.csv'
edgeWritePath = 'output/author_edges.csv'

UBCAuthorWritePath     = 'output/pubUBC_authors.csv'

tagsPath = 'output/pubTags.csv'

confPath = 'output/conf.csv'
confOtherPath  = 'output/confOther.csv'

journPath = 'output/journ.csv'
jounrOtherPath = 'output/journOther.csv'

deptPerYrPath = 'output/deptPerYr.csv'
journAuthPath = 'output/journAuth.csv'
confAuthPath = 'output/confAuth.csv'

rawDataPath            = os.path.abspath(rawDataPath)
cleanDataPath          = os.path.abspath(cleanDataPath)
nodeWritePath          = os.path.abspath(nodeWritePath)
edgeWritePath          = os.path.abspath(edgeWritePath)
UBCAuthorWritePath     = os.path.abspath(UBCAuthorWritePath)
tagsPath               = os.path.abspath(tagsPath)
confPath               = os.path.abspath(confPath)
confOtherPath          = os.path.abspath(confOtherPath)
journPath              = os.path.abspath(journPath)
jounrOtherPath         = os.path.abspath(jounrOtherPath)
deptPerYrPath          = os.path.abspath(deptPerYrPath)
journAuthPath          = os.path.abspath(journAuthPath)
confAuthPath           = os.path.abspath(confAuthPath)