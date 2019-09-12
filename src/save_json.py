
import json
import os

def json_update(link):
    check = os.path.exists("./config/weblink.json")
    if check:
        pass
    else:
        data = {}
        with open('./config/weblink.json', 'w') as outfile:
            json.dump(data, outfile)

    with open('./config/weblink.json', "r+") as jsonFile:
        new_data = json.load(jsonFile)
        web=link
        new_data['website'] = web
        jsonFile.seek(0)  # rewind
        json.dump(new_data, jsonFile)
        jsonFile.truncate()