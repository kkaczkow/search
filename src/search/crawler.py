# example: userSearch = 'basketball with cartoon aliens'

import src.rest
import sys
import json
from src import common
import requests
import src.utils
from requests.auth import HTTPBasicAuth
from strategy import query_strategy

def run(query):
    if query['explain'] is True:
         return explain(query)
    return search(query)

def get_query(userSearch, explain):
    strategy_query = query_strategy[common.SEARCH_STRATEGY](userSearch)

    query = {
        "explain": explain,
        "query": strategy_query
    }
    print "Searching phrase: \"" + src.utils.get_yellow_print(userSearch) + "\""
    return query

# searches the TMDB Elasticsearch index with the provided Elasticsearch Query DSL query
def search(query):
    print "Searching...\n"
    url = 'http://localhost:9200/tmdb/movie/_search'
    #httpResp = rest.get(url, data=query)
    try:
        httpResp = requests.get(url, data=json.dumps(query),
                                auth=HTTPBasicAuth(common.ELASTICSEARCH_U, common.ELASTICSEARCH_P))
    except requests.exceptions.ChunkedEncodingError as error:
        src.rest.handle_error(error)

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
    httpResp = src.rest.get('http://localhost:9200' + '/tmdb/movie/_validate/query?explain',
                            data=json.dumps(query))
    print json.dumps(json.loads(httpResp.text), indent=4, sort_keys=True)
