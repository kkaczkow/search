# rest client - requests library wrapper

import requests
from requests.auth import HTTPBasicAuth
import common
import utils

def post(url, data):
    try:
        r = requests.post(url, data, auth=HTTPBasicAuth(common.ELASTICSEARCH_U, common.ELASTICSEARCH_P))
        r.raise_for_status()
        check_status_code(r.status_code)

    except requests.exceptions.ConnectionError as error:
        handle_error(error)

def put(url, data):
    try:
        r = requests.put(url, data, auth=HTTPBasicAuth(common.ELASTICSEARCH_U, common.ELASTICSEARCH_P))
        r.raise_for_status()
        check_status_code(r.status_code)

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
        check_status_code(r.status_code)

    except requests.exceptions.ConnectionError as error:
        handle_error(error)
    except requests.exceptions.HTTPError as http_error:
        print "No resource to delete: "+url

def get(url, data):
    try:
        r = requests.get(url, data, auth=HTTPBasicAuth(common.ELASTICSEARCH_U, common.ELASTICSEARCH_P))
        r.raise_for_status()
        check_status_code(r.status_code)

    except requests.exceptions.ConnectionError as error:
        handle_error(error)

def check_status_code(status_code):
    if int(status_code) >= 200 and int(status_code) < 300:
        print utils.get_green_print("Success.")
    else:
        print utils.get_red_print("Failure.")

def handle_error(error):
    utils.print_error(str(error))
    exit(1)