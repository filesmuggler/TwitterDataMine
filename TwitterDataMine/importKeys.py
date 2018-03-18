import json

def importKeys(path_p):
    # import keys from file specified in path
    keys = []
    path_f = ''
    with open(path_p,'r') as f:
        for line in f:
            for letter in line:
                path_f = path_f + letter
                if letter == '\\':
                    path_f = path_f + '\\'
        

    with open(path_f, 'r') as g:
        for line in g:
            line = line[:-1]
            keys.append(line)
    return keys