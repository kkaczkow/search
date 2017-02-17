# rest client - requests library wrapper

import requests
from requests.auth import HTTPBasicAuth
import common
import utils

def post(url, data):
    try:
        return requests.post(url, data, auth=HTTPBasicAuth(common.ELASTICSEARCH_U, common.ELASTICSEARCH_P))
    except requests.exceptions.ConnectionError as error:
        handle_error(error)

def put(url, data):
    try:
        r = requests.put(url, data, auth=HTTPBasicAuth(common.ELASTICSEARCH_U, common.ELASTICSEARCH_P))
        r.raise_for_status()
    except requests.exceptions.ConnectionError as error:
        handle_error(error)
    except requests.exceptions.HTTPError as http_error:
        handle_error(http_error)
    except requests.exceptions.ChunkedEncodingError as error:
        handle_error(error)

def delete(url):
    try:
        r = requests.delete(url, auth=HTTPBasicAuth(common.ELASTICSEARCH_U, common.ELASTICSEARCH_P))
        r.raise_for_status()
    except requests.exceptions.ConnectionError as error:
        handle_error(error)
    except requests.exceptions.HTTPError as http_error:
        print "No resource to delete: "+url

def get(url, data):
    try:
        return requests.get(url, data, auth=HTTPBasicAuth(common.ELASTICSEARCH_U, common.ELASTICSEARCH_P))
    except requests.exceptions.ConnectionError as error:
        handle_error(error)

def handle_error(error):
    utils.print_error(str(error))
    exit(1)