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
        return requests.put(url, data, auth=HTTPBasicAuth(common.ELASTICSEARCH_U, common.ELASTICSEARCH_P))
    except requests.exceptions.ConnectionError:
        handle_connection_error(url)

def delete(url):
    try:
        return requests.delete(url, auth=HTTPBasicAuth(common.ELASTICSEARCH_U, common.ELASTICSEARCH_P))
    except requests.exceptions.ConnectionError:
        handle_connection_error(url)

def get(url, data):
    try:
        return requests.get(url, data, auth=HTTPBasicAuth(common.ELASTICSEARCH_U, common.ELASTICSEARCH_P))
    except requests.exceptions.ConnectionError:
        handle_connection_error(url)

def handle_connection_error(url):
    print "ERROR: Connection refused: " + url
    exit(1)