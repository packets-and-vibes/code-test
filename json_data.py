import json

with open('r1.json') as file:
    data = json.load(file)

#print(data)
print(data['router']['interfaces'][0])
