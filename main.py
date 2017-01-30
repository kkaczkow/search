# example invocation: python search.py "basketball with aliens"
import sys, os
from src import search
from src import io
from src import indexer
from src import analyzer

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

def get_analysis_chain():
    analysisSettings = {
        "filter": {
            "acronyms": {
                "type": "word_delimiter",
                "catenate_all": true,
                "generate_word_parts": false,
                "generate_number_parts": false }
        },
        "analyzer": {
            "standard_with_acronyms": {
                "tokenizer": "standard",
                "filter": ["standard","lowercase","acronyms"]
            }
        }
    }
    return analysisSettings

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
    movieDict = io.extract(DB_PATH)
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
