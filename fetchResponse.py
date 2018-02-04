#!/usr/bin/python
import sys
import random
import indicoio
execfile("indico.py")
indicoio.config.api_key = "129bf36b796984d3336a951fd28b29ad"
execfile("dbAccess.py")
import json
import base64

DBs = {
    'We should go vegan':'ShouldWeGoVegan.db',
    'Cannabis should be legal':'ShouldCannabisBeLegal.db',
    'Humans have free will':'ShouldWeGoVegan.db',
}



def getResponse():
    input = sys.argv # [scriptName, inputStr]
    print sys.argv
    print "'\n'"
    print sys.argv[4]
    data=json.loads(sys.argv[4])
    inputStr = str(input[1])
    mapKey = str(input[2])
    #print len(sys.argv)
    #print input
    
    #print mapKey
    db = DBs[mapKey]
    view = str(input[3])
    sentiment = input[4]
    keyList = keyword(inputStr)
    [key1, key2] = relevant(inputStr, keyList)
    dbCxn = create_connection(db)
    result = queryTableByKeywords(dbCxn, key1, key2, view)
    updatedImpression = analyzeImpression(inputStr, data)
    if len(result) > 0:
        ranked = rankResults(result, key1, key2)
        response = [ranked[key] for key in ranked]
        return response[0], updatedImpression
    else:
        genericResp = ['Why do you say that?', 'I don\'t understand the validity of your argument', 'Please elaborate', 'What makes you think that?']
        idx = random.randint(0, len(genericResp) -1)
        return genericResp[idx], updatedImpression
getResponse()
