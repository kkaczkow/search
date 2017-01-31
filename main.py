# example invocation: python search.py "basketball with aliens"
import sys, os

from src import search
from src import io
from src import indexer
from src import analyzer
from src import common

def get_query(explain):
    if len(sys.argv) > 1:
        usersSearch = str(sys.argv[1])
    else:
        usersSearch = 'basketball with cartoon aliens'

    query = {
        "explain": explain,
        "query": {
            "multi_match": {
                "query": usersSearch,
                "fields": ["title^0.1", "overview"],
            }
        }
    }
    print "Searching phrase: " + usersSearch
    return query

# primitive CLI
def main():
    if len(sys.argv) == 2 and str(sys.argv[1]) == "reindex":
        movieDict = io.extract(common.DB_PATH)
        mappingSettings = analyzer.get_mapping()
        analysisSettings = analyzer.get_analysis_chain()
        indexer.reindex(analysisSettings = analysisSettings, mappingSettings = mappingSettings, movieDict = movieDict)
    elif len(sys.argv) in (1,2):
        query = get_query(explain = False)
        search.run(query)
        #search.validate(query)
    else:
        print "ERROR: Invalid number of arguments."

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ("Interrupted by user.")
