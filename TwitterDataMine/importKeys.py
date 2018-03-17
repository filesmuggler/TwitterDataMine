from preprocessKeys import preprocessKeys
import json

def __importConsumerKey(path):
    consumer_key = ''
    with open(path,'r') as f:
        for line in f:
            nline = json.loads(line)
            consumer_key = preprocessKeys(nline['consumer_key'])
    return consumer_key

def __importConsumerSecret(path):
    consumer_secret = ''
    with open(path,'r') as f:
        for line in f:
            nline = json.loads(line)
            consumer_secret = preprocessKeys(nline['consumer_secret'])
    return consumer_secret

def __importAccessToken(path):
    consumer_token = ''
    with open(path,'r') as f:
        for line in f:
            nline = json.loads(line)
            consumer_token = preprocessKeys(nline['access_token'])
    return consumer_token

def __importAccessSecret(path):
    consumer_asecret = ''
    with open(path,'r') as f:
        for line in f:
            nline = json.loads(line)
            consumer_asecret = preprocessKeys(nline['access_token_secret'])
    return consumer_asecret

def importKeys(path):
    keys = list()
    keys.append( __importConsumerKey(path))
    keys.append(__importConsumerSecret(path))
    keys.append(__importAccessToken(path))
    keys.append(__importAccessSecret(path))
    return keys