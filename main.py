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

def main():
    movieDict = io.extract(common.DB_PATH)
    mappingSettings = analyzer.get_mapping()
    analysisSettings = analyzer.get_analysis_chain()
    indexer.reindex(analysisSettings = analysisSettings, mappingSettings = mappingSettings, movieDict = movieDict)

    query = get_query(explain = False)
    search.run(query)
    #search.validate(query)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ("Interrupted by user.")
