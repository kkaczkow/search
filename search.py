# example invocation: python search.py "basketball with aliens"
import requests
import json
import sys, os

path = "/Users/kkaczkow/development/workspace/relevant-search-book/ipython/tmdb.json"
ELASTICSEARCH_HOST = "localhost"
ELASTICSEARCH_PORT = "9200"

def extract():
    try:
        f = open(path)
    except IOError:
        print "ERROR: No such file or directory: "+path
        exit(1)

    if f:
        return json.loads(f.read());

def reindex(analysisSettings={}, mappingSettings={}, movieDict={}):
    settings = {
        "settings": {
            "number_of_shards": 1,
            "index": {
                "analysis" : analysisSettings,
            }}}
    if mappingSettings:
       settings['mappings'] = mappingSettings
    
    "Deleting the old index..."
    try:
        resp = requests.delete("http://localhost:9200/tmdb")
    except requests.exceptions.ConnectionError: 
        handle_connection_error("tmdb")

    print "Creating the index..."
    try:
        resp = requests.put("http://localhost:9200/tmdb",
                    data=json.dumps(settings))
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

def reindex_with_english_analyzer():    
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
    movieDict = extract()
    reindex(mappingSettings=mappingSettings, movieDict=movieDict)

def search(query):
    print "Searching...\n"
    url = 'http://localhost:9200/tmdb/movie/_search'
    httpResp = requests.get(url, data=json.dumps(query))
    searchHits = json.loads(httpResp.text)['hits']
    print "Num\tRelevance Score\t\tMovie Title"
    for idx, hit in enumerate(searchHits['hits']):
        print "%s\t%s\t\t%s" % (idx + 1, hit['_score'], hit['_source']['title'])

def validate_query(query):
    print "Validating..."
    httpResp = requests.get('http://localhost:9200' +
                   '/tmdb/movie/_validate/query?explain',
                    data=json.dumps(query))
    print json.loads(httpResp.text)

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
    print "Searching phrase: "+usersSearch
    return query

def main():
    movieDict = extract()
    reindex_with_english_analyzer()
    query = get_query()
    search(query)
    #validate_query(query)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print ("Interrupted by user.")
