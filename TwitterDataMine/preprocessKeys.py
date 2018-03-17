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
        r'(?:[\w_]+)', # other words
    ]

# tokenizing makes easier to find words in the tweets
def __tokenize(s):
    tokens_re = re.compile(r'('+'|'.join(__regex_str)+')', re.VERBOSE | re.IGNORECASE)
    return tokens_re.findall(s)                             # looks for all strings with this

def preprocessKeys(s):                         # gets tokens of text
    tokens = __tokenize(s)
    return tokens
