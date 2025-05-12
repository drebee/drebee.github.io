import json

with open("test.json", "r") as f:
  d = json.load(f)
  key = input("key: ")
  value = input("value: ")
  d[key] =  value

with open("test.json", "w") as f:
  json.dump(d, f)

with open("test.json", "r") as f:
  new_d = json.load(f)

print(new_d)