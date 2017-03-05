class Strategy:
    FIELD_CENTRIC = 1
    COMBINED = 2

def field_centric(userSearch):
    query = {
        "multi_match": {
            "query": userSearch,
            "fields": ["title", "overview", "cast.name.bigrammed", "directors.name.bigrammed"],
            "type": "most_fields"
        }
    }
    return query

def combined(userSearch):
    query = {
        "multi_match": {
            "query": userSearch,
            "fields": ["title", "overview", "people.name"],
            "type": "most_fields"
        }
    }
    return query

query_strategy = { Strategy.FIELD_CENTRIC : field_centric,
                              Strategy.COMBINED : combined }





