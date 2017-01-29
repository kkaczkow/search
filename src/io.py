import json
import sys, os

ELASTICSEARCH_HOST = "localhost"
ELASTICSEARCH_PORT = "9200"

def extract(db_path):
    print "Extracting..."
    try:
        db = open(db_path)
    except IOError:
        print "ERROR: No such file or directory: " + db_path
        exit(1)

    if db:
        return json.loads(db.read());