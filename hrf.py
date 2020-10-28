import json
import requests
json_data = open("inter.json").read()
data = json.loads(json_data)

print(len(set(data)))