import json

def importKeys(path):
    # import keys from file specified in path
    keys = []
    with open(path, 'r') as f:
        for line in f:
            line = line[:-1]
            keys.append(line)
    return keys