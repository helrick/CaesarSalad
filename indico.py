# coding=utf-8
from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1

import indicoio
indicoio.config.api_key = '3ccad861571b4040c5312e55d9884722'

# extract keywords from string s
def keyword(s):
    result = indicoio.keywords(s)
    keys = [key.encode("utf-8") for key in result]
    relevancy = relevant(s, keys)

def relevant(s, keys):
    scores = indicoio.relevance(s, keys)
    result = dict(zip(keys, scores))
    return result
