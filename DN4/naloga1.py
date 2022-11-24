import json

podatki = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

pretvorba = json.dumps(podatki)

print(pretvorba)
print(type(pretvorba))