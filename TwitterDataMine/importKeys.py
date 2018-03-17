from .preprocess import preprocess
import json

def __importConsumerKey(path):
    consumer_key = ''
    with open(path,'r') as f:
        for line in f:
            nline = json.loads(line)
            consumer_key = preprocess(nline['consumer_key'], False)
    return consumer_key

def __importConsumerSecret(path):
    consumer_secret = ''
    with open(path,'r') as f:
        for line in f:
            nline = json.loads(line)
            consumer_secret = preprocess(nline['consumer_secret'], False)
    return consumer_secret

def __importAccessToken(path):
    consumer_token = ''
    with open(path,'r') as f:
        for line in f:
            nline = json.loads(line)
            consumer_token = preprocess(nline['access_token'], False)
    return consumer_token

def __importAccessSecret(path):
    consumer_asecret = ''
    with open(path,'r') as f:
        for line in f:
            nline = json.loads(line)
            consumer_asecret = preprocess(nline['access_token_secret'], False)
    return consumer_asecret

def importKeys(importFileName):
    path = ''
    with open(importFileName, 'r') as f:
        for line in f:
            path = line
    keys = [4]
    keys[0] = __importConsumerKey(path)
    keys[1] = __importConsumerSecret(path)
    keys[2] = __importAccessToken(path)
    keys[3] = __importAccessSecret(path)
    return keys