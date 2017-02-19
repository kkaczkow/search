# example invocation: python search.py "basketball with aliens"
import sys, os
from src import crawler
from src import io
from src import indexer
from src import analyzer
from src import common
from src import utils

def reindex():
    movieDict = io.extract(common.DB_PATH)
    mappingSettings = analyzer.get_mapping()
    analysisSettings = analyzer.get_analysis_chain()
    indexer.reindex(analysisSettings = analysisSettings, mappingSettings = mappingSettings, movieDict = movieDict)

def search(userSearch):
    query = crawler.get_query(userSearch, explain = common.EXPLAIN)
    crawler.run(query)

# primitive CLI
def main():
    try:
        command = sys.argv[1]
    except IndexError:
        print utils.get_red_print("ERROR: ")+"Invalid number of arguments."
        sys.exit(1)

    if command == "reindex":
        reindex()
    else:
        search(sys.argv[1])

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ("Interrupted by user.")
