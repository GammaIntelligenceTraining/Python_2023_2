import json

json_string = '''
{
    "people" : [
        {
            "name": "Jack Smith",
            "phone": "555-555-5555",
            "has_licence": true,
            "email": null
        },
        {
            "name": "Mary Gold",
            "phone": "555-222-5225",
            "has_licence": false,
            "email": "mary@example.com"
        }
    ]
}
'''
data = json.loads(json_string)
print(data['people'])
print(type(data))

for person in data['people']:
    person['greeting'] = 'Hello ' + person.get('name')
    print(person['greeting'])

json_result = json.dumps(data)
print(json_result)
print(type(json_result))

with open('temp.json', 'w', encoding='utf8') as file:
    json.dump(data, file, indent=2)

with open('temp.json', 'r', encoding='utf8') as file:
    new_data = json.load(file)
print(new_data)

