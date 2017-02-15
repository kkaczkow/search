# rest client - requests library wrapper

import requests
from requests.auth import HTTPBasicAuth
import common

def post(url, data):
    try:
        return requests.post(url, data, auth=HTTPBasicAuth(common.ELASTICSEARCH_U, common.ELASTICSEARCH_P))
    except requests.exceptions.ConnectionError:
        handle_connection_error(url)

def put(url, data):
    try:
        r = requests.put(url, data, auth=HTTPBasicAuth(common.ELASTICSEARCH_U, common.ELASTICSEARCH_P))
        r.raise_for_status()
    except requests.exceptions.ConnectionError:
        handle_connection_error(url)
    except requests.exceptions.HTTPError as http_error:
        print str(http_error)
        exit(1)

def delete(url):
    try:
        r = requests.delete(url, auth=HTTPBasicAuth(common.ELASTICSEARCH_U, common.ELASTICSEARCH_P))
        r.raise_for_status()
    except requests.exceptions.ConnectionError:
        handle_connection_error(url)
    except requests.exceptions.HTTPError as http_error:
        print "No resource to delete: "+url

def get(url, data):
    try:
        return requests.get(url, data, auth=HTTPBasicAuth(common.ELASTICSEARCH_U, common.ELASTICSEARCH_P))
    except requests.exceptions.ConnectionError:
        handle_connection_error(url)

def handle_connection_error(url):
    print "ERROR: Connection refused: " + url
    exit(1)