def get_mapping():
    # mappings:
    mappingSettings = {
        "movie": {
            "properties": {
                "title": {
                    "type": "string",
                    "analyzer": "retail_analyzer_index",
                    "search_analyzer": "retail_analyzer_search"
                },
                "overview": {
                    "type": "string",
                    "analyzer": "retail_analyzer_index",
                    "search_analyzer": "retail_analyzer_search"
                }
            }
        }
    }
    return mappingSettings

# returns an analysis chain that will create suitable tokens
def get_analysis_chain():
    # analysis:
    analysisSettings = {
        "filter": {
            "index_filter": {
                "type": "synonym",
                "synonyms_path" : "analysis/synonym.txt"
            },
            "search_filter": {
                "type": "synonym",
                "synonyms_path" : "analysis/synonym.txt"
            },
            "english_stop": {
                "type":       "stop",
                "stopwords":  "_english_"
            },
            "english_stemmer": {
                "type":       "stemmer",
                "language":   "english"
            },
            "english_possessive_stemmer": {
                "type":       "stemmer",
                "language":   "possessive_english"
            }
        },
        "analyzer": {
            "retail_analyzer_index": {
                "tokenizer": "standard",
                "filter": [
                    "english_possessive_stemmer",
                    "lowercase",
                    "english_stop",
                    "english_stemmer",
                    "index_filter"]
            },
            "retail_analyzer_search": {
                "tokenizer": "standard",
                "filter": [
                    "english_possessive_stemmer",
                    "lowercase",
                    "english_stop",
                    "english_stemmer",
                    "search_filter"]
            }
        }
    }
    return analysisSettings