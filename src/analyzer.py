def get_mapping():
    mappingSettings = {
        "movie": {
            "properties": {
                "title": {
                    "type": "string",
                    "analyzer": "english"
                },
                "overview": {
                    "type": "string",
                    "analyzer": "english"
                }
            }
        }
    }
    return mappingSettings

# returns an analysis chain that will create suitable tokens
def get_analysis_chain():
    analysisSettings = {
        "filter": {
            "acronyms": {
                "type": "word_delimiter",
                "catenate_all": True,
                "generate_word_parts": False,
                "generate_number_parts": False }
        },
        "analyzer": {
            "standard_with_acronyms": {
                "tokenizer": "standard",
                "filter": ["standard","lowercase","acronyms"]
            }
        }
    }
    return analysisSettings