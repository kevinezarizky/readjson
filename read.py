import json

print('Read JSON file')

def getJSON(filepath):
    with open(filepath, 'r') as fp:
        return json.load(fp)

myObj = getJSON('./latih.json')

print(myObj.get("mahasiswa"))

