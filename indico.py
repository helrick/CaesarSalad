import operator

import indicoio
indicoio.config.api_key = '3ccad861571b4040c5312e55d9884722'

# extract keywords from string s
def keyword(s):
    result = indicoio.keywords(s)
    keys = [key.encode("utf-8") for key in result]
    #print(keys)
    return relevant(s, keys)

def rankResults(results, key1, key2):
    rank1 = indicoio.relevance(results, key1)
    rank2 = indicoio.relevance(results, key2)
    total = {}
    for key in rank1:
        total[key] = rank1[key] + rank2[key]
    return dict(sorted(total.iteritems(), key=operator.itemgetter(1), reverse=True)[:1])

def relevant(s, keys):
    scores = indicoio.relevance(s, keys)
    result = dict(zip(keys, scores))
    result = dict(sorted(result.iteritems(), key=operator.itemgetter(1), reverse=True)[:2])
    print(result)
    return result
    # dbSearch(relevancy[0], relevancy[1])

print(keyword("I think capitalism is sustainable because it supports the economy"))
