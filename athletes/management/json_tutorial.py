# loads() takes in a string and returns a json object. 
# json. dumps() takes in a json object and returns a string.

import json


file = "athletes\data.json"
with open(file) as f:
    data = json.load(f)

print(data)

# print(data)
print(data['Athletes'][-1])
data['test'] = True

new_json = json.dumps(data, indent=4, sort_keys=True)
# print(new_json)

with open("data2.json", "w") as f:
    json.dump(data, f, indent=4)
