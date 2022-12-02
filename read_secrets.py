import json
def get_secrets():
    with open('secrets.json') as json_file:
        data = json.load(json_file)
        return data