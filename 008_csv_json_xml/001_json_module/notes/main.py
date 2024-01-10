import datetime
import json
with open('storage.json', 'r', encoding='utf8') as file:
    data = json.load(file)


while True:
    note = input('Enter ToDo or "exit": ')
    if note.lower() == 'exit':
        break
    data.append({'note': note, 'date_added': datetime.datetime.now().timestamp()})
    with open('storage.json', 'w', encoding='utf8') as file:
        json.dump(data, file, indent=2)