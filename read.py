import json

print('Read JSON file')

def getJSON(filepath):
    with open(filepath, 'r') as fp:
        return json.load(fp)

myObj = getJSON('./latih.json')
tes2 = json.dumps(myObj)
tes3 = json.loads(tes2)
print("------------------------------------------------")
print("print all")
print(myObj.get("mahasiswa"))
print(tes3['mahasiswa'][0]['nama'])
print(tes3['mahasiswa'][0]['nrp'])
print(tes3['mahasiswa'][1]['nama'])
print(tes3['mahasiswa'][1]['nrp'])
