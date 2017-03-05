class Strategy:
    FIELD_CENTRIC = 1
    TERM_CENTRIC = 2
    COMBINED = 3
    ALL = 4
    GREEDY_TERM_CENTRIC = 5

def field_centric(userSearch):
    print "Using field centric strategy"
    return {
        "multi_match": {
            "query": userSearch,
            "fields": ["title", "overview", "cast.name.bigrammed", "directors.name.bigrammed"],
            "type": "most_fields"
        }
    }

def term_centric(userSearch):
    print "Using term centric strategy"
    return {
        "query_string": {
            "query": userSearch,
            "fields": ["title", "overview", "cast.name.bigrammed", "directors.name.bigrammed"]
        }
    }

def combined(userSearch):
    print "Using combined (term + field centric) strategy"
    return {
        "multi_match": {
            "query": userSearch,
            "fields": ["title", "overview", "people.name"],
            "type": "most_fields"
        }
    }

def all(userSearch):
    print "Using strategy _all"
    return {
        "match": {
            "_all": userSearch,
        }
    }

def greedy_term_centric(userSearch):
    print "Using greedy term-centric strategy paired with highly discriminating like fields"
    return {
        "bool": {
            "should": [ {
                "multi_match": {
                    "query": userSearch,
                    "fields": ["directors.name.bigrammed", "cast.name.bigrammed"],
                    "type": "cross_fields"
                } },
                {
                    "multi_match": {
                        "query": userSearch,
                        "fields": ["overview", "title", "directors.name", "cast.name"],
                        "type": "cross_fields"
                    }
                }
            ]
        }
    }

# strategy dispatcher
query_strategy = { Strategy.FIELD_CENTRIC: field_centric,
                   Strategy.TERM_CENTRIC: term_centric,
                   Strategy.COMBINED: combined,
                   Strategy.ALL: all,
                   Strategy.GREEDY_TERM_CENTRIC: greedy_term_centric}





