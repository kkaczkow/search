import requests
import json

ELASTICSEARCH_HOST = "localhost"
ELASTICSEARCH_PORT = "9200"

def reindex(analysisSettings = {}, mappingSettings = {}, movieDict = {}):
    settings = {
        "settings": {
            "number_of_shards": 1,
            "index": {
                "analysis" : analysisSettings,
            }}}
    if mappingSettings:
       settings['mappings'] = mappingSettings
    
    print "Deleting the old index..."
    try:
        resp = requests.delete("http://localhost:9200/tmdb")
    except requests.exceptions.ConnectionError: 
        handle_connection_error("tmdb")

    print "Creating the index..."
    try:
        resp = requests.put("http://localhost:9200/tmdb",
                    data = json.dumps(settings))
    except requests.exceptions.ConnectionError:
        handle_connection_error("tmdb")

    print "Inserting data into the index..."
    bulkMovies = ""
    for id, movie in movieDict.iteritems():
        addCmd = {"index": {"_index": "tmdb",
                        "_type": "movie",
                               "_id": movie["id"]}}
        bulkMovies += json.dumps(addCmd) + "\n" + json.dumps(movie) + "\n"
    resp = requests.post("http://localhost:9200/_bulk", data=bulkMovies)

def handle_connection_error(context):
    print "ERROR: Connection refused: " + "http://"+ELASTICSEARCH_HOST + "/" + ELASTICSEARCH_PORT + "/" + context
    exit(1)
