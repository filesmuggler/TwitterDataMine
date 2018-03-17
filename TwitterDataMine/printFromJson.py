import json

# prints json in readable form
def printFromJson(data):
    print(json.dumps(data, sort_keys=True, indent=2))
