# example invocation: python search.py "basketball with aliens"
import sys, os
from src import search
from src import io
from src import indexer

DB_PATH = os.path.abspath(os.path.dirname(__file__)) + "/db/tmdb.json"

def reindex_with_english_analyzer(movieDict):
    mappingSettings = {
        "movie": {
            "properties": {
                "title": {
                    "type": "string",
                    "analyzer": "english"
                },
                "overview": {
                    "type": "string",
                    "analyzer": "english"
                }
            }
        }
    }
    indexer.reindex(mappingSettings = mappingSettings, movieDict = movieDict)

def get_query():
    if len(sys.argv) > 1:
        usersSearch = str(sys.argv[1])
    else:
        usersSearch = 'basketball with cartoon aliens'
    query = {
        "query": {
            "multi_match": {
                "query": usersSearch,
                "fields": ["title^10", "overview"],
            }
        }
    }
    print "Searching phrase: " + usersSearch
    return query

def main():
    movieDict = io.extract(DB_PATH)
    reindex_with_english_analyzer(movieDict)
    query = get_query()
    search.run(query)
    #search.validate(query)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ("Interrupted by user.")
