import json

def importKeys(path):
    keys = []
    with open(path, 'r') as f:
        for line in f:
            line = line[:-1]
            keys.append(line)
    return keys