import tweepy
import vincent
import json
import re
from tweepy import OAuthHandler


class Analyzer():
    __slots__=['TwitterApi']
    # emoticons regular expressions
    __emoticons_str = r"""
        (?:
            [:=;] # Eyes
            [oO\-]? # Nose (optional)
            [D\)\]\(\]/\\OpP] # Mouth
        )"""
 

    # other features regular expressions
    __regex_str = [
        __emoticons_str,
        r'<[^>]+>', # HTML tags
        r'(?:@[\w_]+)', # @-mentions
        r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
        r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
        r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
        r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
        r'(?:[\w_]+)', # other words
        r'(?:\S)' # anything else
    ]

    def __init__(self, api):
        self.TwitterApi = api

    def __del__(self):
        print("Analyzer destroyed!")

        # writes json to file
    def __save_to_file(self,data, name):
        try:
            with open(name, 'w') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e)) 
        return True

    def __process_to_string(self,in_data, fndt):
        temp = str(json.dumps(in_data, sort_keys=True))
        s = fndt + temp + '\n'
        return s

    def __printFromJson(data):
        print(json.dumps(data, sort_keys=True, indent=2))

    def __tokenize(self,s):
        tokens_re = re.compile(r'('+'|'.join(self.__regex_str)+')', re.VERBOSE | re.IGNORECASE)
        return tokens_re.findall(s)                             # looks for all strings with this
 
    def __preprocess(self, s, lowercase=True):                         # gets tokens of text
        tokens = self.__tokenize(s)
        if lowercase:
            emoticon_re = re.compile(r'^'+self.__emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
            tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
        return tokens

    def getData(self,target):
        print("Getting data for " + target)
        item = self.TwitterApi.get_user(target)
        print("name: " + item.name)
        print("screen_name: " + item.screen_name)
        print("description: " + item.description)
        print("statuses_count: " + str(item.statuses_count))
        print("friends_count: " + str(item.friends_count))
        print("followers_count: " + str(item.followers_count))

    def getTweets(self, target, number, save=False):
        if(not save):
            for twt in tweepy.Cursor(self.TwitterApi.user_timeline, id=target).items(number):
                self.__printFromJson(twt._json)
        else:
            final_data = ""
            for twt in tweepy.Cursor(self.TwitterApi.user_timeline, id=target).items(number):
                final_data = self.__process_to_string(twt._json, final_data)

            self.__save_to_file(final_data,"tweets.json")


    def filterByTerm(self, term, filename):
        with open(filename,'r') as f:
            for line in f:
                tweet = json.loads(line)
                tokens = self.__preprocess(tweet[term])
                print(tokens)



    def mostFrequent(number=10, save=False):
        return True

    

    

    