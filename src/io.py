import json
import sys, os

ELASTICSEARCH_HOST = "localhost"
ELASTICSEARCH_PORT = "9200"

# returns a dictionary mapping movie ID to movie details from tmdb.json, reflecting the TMDB source data model
def extract(db_path):
    print "Extracting..."
    try:
        db = open(db_path)
    except IOError:
        print "ERROR: No such file or directory: " + db_path
        exit(1)

    if db:
        return json.loads(db.read());