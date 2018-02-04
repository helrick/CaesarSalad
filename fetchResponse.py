import sys
import random
import indico
import dbAccess

DBs = {
    'We should go vegan':'Freewill.db',
    'Cannabis should be legal':'ShouldCannabisBeLegal.db',
    'Humans have free will':'ShouldWeGoVegan.db',
}

input = str(sys.argv) # [scriptName, inputStr]
inputStr = str(input[1])
mapKey = str(input[2])
db = DBs[mapKey]
view = str(input[3])
sentiment = input[4]

def getResponse():
    keyList = keyword(inputStr)
    [key1, key2] = relevant(inputStr, keyList)
    dbCxn = create_connection(dbName)
    result = queryTableByKeywords(dbCxn, key1, key2, view)
    updatedImpression = analyzeImpression(inputStr, sentiment)
    if len(result) > 0:
        ranked = rankResults(result, key1, key2)
        response = [ranked[key] for key in ranked]
        return response[0], updatedImpression
    else:
        genericResp = ['Why do you say that?', 'I don\'t understand the validity of your argument', 'Please elaborate', 'What makes you think that?']
        idx = random.randint(0, len(genericResp) -1)
        return genericResp[idx], updatedImpression
getResponse()
