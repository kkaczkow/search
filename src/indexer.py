import requests
import json

# reindexes into Elasticsearch with the passed-in TMDB movie dictionary, analysis set- tings, and field mappings
def reindex(analysisSettings = {}, mappingSettings = {}, movieDict = {}):
    settings = {
        "settings": {
            "number_of_shards": 1,
            "index": {
                "analysis" : analysisSettings,
            }}}
    if mappingSettings:
       settings['mappings'] = mappingSettings

    delete_index()
    create_index(settings)
    insert_data(movieDict)

def delete_index():
    print "Deleting the old index..."
    try:
        resp = requests.delete("http://localhost:9200/tmdb")
    except requests.exceptions.ConnectionError:
        handle_connection_error("tmdb")

def create_index(settings):
    print "Creating the index..."
    try:
        resp = requests.put("http://localhost:9200/tmdb",
                            data = json.dumps(settings))
    except requests.exceptions.ConnectionError:
        handle_connection_error("tmdb")

def insert_data(movieDict):
    print "Inserting data into the index..."
    bulkMovies = ""
    for id, movie in movieDict.iteritems():
        addCmd = {"index": {"_index": "tmdb",
                            "_type": "movie",
                            "_id": movie["id"]}}
        bulkMovies += json.dumps(addCmd) + "\n" + json.dumps(movie) + "\n"

    try:
        resp = requests.post("http://localhost:9200/_bulk", data = bulkMovies)
    except requests.exceptions.ConnectionError:
        handle_connection_error("_bulk")

def handle_connection_error(context):
    print "ERROR: Connection refused: " + "http://"+ELASTICSEARCH_HOST + "/" + ELASTICSEARCH_PORT + "/" + context
    exit(1)
