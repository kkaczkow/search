import rest
import sys
import json
import common
import requests
from requests.auth import HTTPBasicAuth

def run(query):
    if query['explain'] is True:
         return explain(query)
    return search(query)

# searches the TMDB Elasticsearch index with the provided Elasticsearch Query DSL query
def search(query):
    print "Searching...\n"
    url = 'http://localhost:9200/tmdb/movie/_search'
    httpResp = requests.get(url, data=json.dumps(query),
                            auth=HTTPBasicAuth(common.ELASTICSEARCH_U, common.ELASTICSEARCH_P))
    try:
        searchHits = json.loads(httpResp.text)['hits']
    except KeyError:
        print "ERROR: " + str(json.loads(httpResp.text)['error']['reason'])
        sys.exit(1)

    print "Num\tRelevance Score\t\tMovie Title"
    for idx, hit in enumerate(searchHits['hits']):
        print "%s\t%s\t\t%s" % (idx + 1, hit['_score'], hit['_source']['title'])

def explain(query):
    print "Score computation...\n"
    url = 'http://localhost:9200/tmdb/movie/_search'
    httpResp = requests.get(url, data=json.dumps(query),
                            auth=HTTPBasicAuth(common.ELASTICSEARCH_U, common.ELASTICSEARCH_P))
    jsonResp = json.loads(httpResp.text)

    print "Explain for %s" % jsonResp['hits']['hits'][0]['_source']['title']
    print json.dumps(jsonResp['hits']['hits'][0]['_explanation'], indent=True)

# debugs matching
def validate(query):
    print "Validating..."
    query.pop('explain', None)
    httpResp = rest.get('http://localhost:9200' + '/tmdb/movie/_validate/query?explain',
                        data=json.dumps(query))
    print json.dumps(json.loads(httpResp.text), indent=4, sort_keys=True)
