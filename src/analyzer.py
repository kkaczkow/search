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
            "retail_syn_filter_index": {
                "type": "synonym",
                "synonyms_path" : "analysis/synonym.txt"
            },
            "retail_syn_filter_search": {
                "type": "synonym",
                "synonyms_path" : "analysis/synonym.txt"
            }
        },
        "analyzer": {
            "retail_analyzer_index": {
                "tokenizer": "standard",
                "filter": [
                    "lowercase",
                    "retail_syn_filter_index"]
            },
            "retail_analyzer_search": {
                "tokenizer": "standard",
                "filter": [
                    "lowercase",
                    "retail_syn_filter_search"]
            }
        }
    }
    return analysisSettings