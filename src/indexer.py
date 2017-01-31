import rest
import json
import common

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
    rest.delete("http://localhost:9200/tmdb")

def create_index(settings):
    print "Creating the index..."
    rest.put("http://localhost:9200/tmdb", data = json.dumps(settings))

def insert_data(movieDict):
    print "Inserting data into the index..."
    bulkMovies = ""
    for id, movie in movieDict.iteritems():
        addCmd = {"index": {"_index": "tmdb",
                            "_type": "movie",
                            "_id": movie["id"]}}
        bulkMovies += json.dumps(addCmd) + "\n" + json.dumps(movie) + "\n"

    rest.post("http://localhost:9200/_bulk", data = bulkMovies)
