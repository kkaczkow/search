import os
from search.strategy import Strategy

ELASTICSEARCH_HOST = "localhost"
ELASTICSEARCH_PORT = "9200"
ELASTICSEARCH_U = "elastic"
ELASTICSEARCH_P = "changeme"
DB_PATH = os.path.abspath(os.path.dirname(__file__)) + "/../db/tmdb.json"

EXPLAIN = False
SEARCH_STRATEGY = Strategy.COMBINED

