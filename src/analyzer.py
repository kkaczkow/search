#def get_mapping():
#    mappingSettings = {
#        "movie": {
#            "properties": {
#                "title": {
#                    "type": "string",
#                    "analyzer": "english"
#                },
#                "overview": {
#                    "type": "string",
#                    "analyzer": "english"
#                }
#            }
#        }
#    }
#    return mappingSettings


def get_mapping():
    # mappings:
    mappingSettings = {
        "movie": {
            "properties": {
                "title": {
                    "type": "string",
                    # two-sided analysis
                    "analyzer": "retail_analyzer_index",
                    "search_analyzer": "retail_analyzer_search"
                },
                "overview": {
                    "type": "string",
                    # two-sided analysis
                    "analyzer": "retail_analyzer_index",
                    "search_analyzer": "retail_analyzer_search"
                }
            }
        }
    }
    return mappingSettings

#def get_analysis_chain():
#    analysisSettings = {
#        "filter": {
#           "acronyms": {
#                "type": "word_delimiter",
#                "catenate_all": True,
#                "generate_word_parts": False,
#                "generate_number_parts": False,
#                "preserve_original": True
#            }
#        },
#        "analyzer": {
#            "standard_with_acronyms": {
#                "tokenizer": "standard",
#                "filter": ["standard","lowercase","acronyms"]
#            }
#        }
#    }
#    return analysisSettings

# returns an analysis chain that will create suitable tokens
def get_analysis_chain():
    # analysis:
    analysisSettings = {
        "filter": {
            "retail_syn_filter_index": {
                "type": "synonym",
                "synonyms": ["abc => fbi"]
            },
            "retail_syn_filter_search": {
                "type": "synonym",
                "synonyms": ["abc => fbi"]
            }
        },
        "analyzer": {
            "retail_analyzer_index": {
                "tokenizer": "standard",
                "filter": [
                    "english_possessive_stemmer",
                    "lowercase",
                    "retail_syn_filter_index",
                    "english_stop",
                    "english_keywords",
                    "english_stemmer"]
            },
            "retail_analyzer_search": {
                "tokenizer": "standard",
                "filter": [
                    "english_possessive_stemmer",
                    "lowercase",
                    "retail_syn_filter_search",
                    "english_stop",
                    "english_keywords",
                    "english_stemmer"]
            }
        }
    }
    return analysisSettings