import re

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

# tokenizing makes easier to find words in the tweets
def __tokenize(s):
    tokens_re = re.compile(r'('+'|'.join(__regex_str)+')', re.VERBOSE | re.IGNORECASE)
    return tokens_re.findall(s)                             # looks for all strings with this

def preprocess(s, lowercase=True):                         # gets tokens of text
    tokens = __tokenize(s)
    if lowercase:
        emoticon_re = re.compile(r'^'+__emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens