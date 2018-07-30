import json

jsonpath="C:\\json111.json"

with open(jsonpath,'r',encoding='utf-8') as f:
    jsondata=json.load(f)
for data in jsondata['data']:
    print(data['username'])
