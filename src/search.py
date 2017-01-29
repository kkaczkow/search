import requests
import json

ELASTICSEARCH_HOST = "localhost"
ELASTICSEARCH_PORT = "9200"

def handle_connection_error(context):
    print "ERROR: Connection refused: " + "http://"+ELASTICSEARCH_HOST + "/" + ELASTICSEARCH_PORT + "/" + context
    exit(1)

def run(query):
    print "Searching...\n"
    url = 'http://localhost:9200/tmdb/movie/_search'
    try:
        httpResp = requests.get(url, data=json.dumps(query))
    except requests.exceptions.ConnectionError:
        handle_connection_error("tmdb/movie/_search")

    searchHits = json.loads(httpResp.text)['hits']
    print "Num\tRelevance Score\t\tMovie Title"
    for idx, hit in enumerate(searchHits['hits']):
        print "%s\t%s\t\t%s" % (idx + 1, hit['_score'], hit['_source']['title'])

def validate(query):
    print "Validating..."
    httpResp = requests.get('http://localhost:9200' +
                   '/tmdb/movie/_validate/query?explain',
                    data=json.dumps(query))
    print json.loads(httpResp.text)