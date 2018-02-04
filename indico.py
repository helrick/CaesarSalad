import operator
import os

import indicoio
indicoio.config.api_key = os.environ['indicioio']

# extract keywords from string s
def keyword(s):
    result = indicoio.keywords(s)
    keys = [key.encode("utf-8") for key in result]
    return keys

def rankResults(results, key1, key2):
    rank1 = indicoio.relevance(results, key1)
    print rank1
    rank2 = indicoio.relevance(results, key2)
    print rank2
    total = {}
    for key in rank1:
        total[key] = rank1[key] + rank2[key]
    return dict(sorted(total.iteritems(), key=operator.itemgetter(1), reverse=True)[:1])

def relevant(s, keys):
    scores = indicoio.relevance(s, keys)
    result = dict(zip(keys, scores))
    result = dict(sorted(result.iteritems(), key=operator.itemgetter(1), reverse=True)[:2])
    return result

def analyzeImpression(msg, data):
    data['count'] += 1
    emotions = indicoio.emotion(msg)
    personality = indicoio.personality(msg)
    sentimentVal = indicoio.sentiment_hq(msg)
    for e in emotions:
        data['emotion'][e] += emotions[e]
    for p in personality:
        data['personality'][p] += personality[p]
    data['sentiment'] += sentimentVal
    return data

