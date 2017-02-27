def get_mapping():
    # mappings:
    mappingSettings = {
        "movie": {
            "properties": {
                "title": {
                    "type": "string",
                    "analyzer": "index_analyzer",
                    "search_analyzer": "query_analyzer"
                },
                "overview": {
                    "type": "string",
                    "analyzer": "index_analyzer",
                    "search_analyzer": "query_analyzer"
                },
                "cast": {
                    "properties": {
                        "name": {
                            "type": "string",
                            "analyzer": "english",
                            "copy_to": "people.name",
                            "fields": {
                                "bigrammed": {
                                    "type": "string",
                                    "analyzer": "english_bigrams"
                                }
                            }
                        }
                    }
                },
                "directors": {
                    "properties": {
                        "name": {
                            "type": "string",
                            "analyzer": "english",
                            "copy_to": "people.name",
                            "fields": {
                                "bigrammed": {
                                    "type": "string",
                                    "analyzer": "english_bigrams"
                                }
                            }
                        }
                    }
                },
                "people": {
                    "properties": {
                        "name": {
                            "type": "string",
                            "analyzer": "english",
                            "fields": {
                                "bigrammed": {
                                    "type": "string",
                                    "analyzer": "english_bigrams"
                                }
                            }
                        }
                    }
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
            "query_filter": {
                "type": "synonym",
                "synonyms_path" : "analysis/synonym.txt"
            },
            "bigram_filter": {
                "type": "shingle",
                "max_shingle_size":2,
                "min_shingle_size":2,
                "output_unigrams":"true"
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
            "index_analyzer": {
                "tokenizer": "standard",
                "filter": [
                    "english_possessive_stemmer",
                    "lowercase",
                    "index_filter",
                    "english_stop",
                    "english_stemmer"]
            },
            "query_analyzer": {
                "tokenizer": "standard",
                "filter": [
                    "english_possessive_stemmer",
                    "lowercase",
                    "query_filter",
                    "english_stop",
                    "english_stemmer"]
            },
            "english_bigrams": {
                "type": "custom",
                "tokenizer": "standard",
                "filter": [
                    "standard",
                    "lowercase",
                    "porter_stem",
                    "bigram_filter"
                ]
            }
        }
    }
    return analysisSettings