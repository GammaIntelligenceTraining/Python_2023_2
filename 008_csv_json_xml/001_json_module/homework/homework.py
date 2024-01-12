# Write a Python script that reads "data.json" representing employee information.
# Implement a function that calculates and returns the average salary of all employees.
# Create a new JSON entry for a new employee with your own information (name, role, gender, date of birth, phone, and salary).
# Add the new employee entry to the existing JSON data.
# Save the modified JSON data to a new file.
import json

with open('data.json', 'r', encoding='utf8') as file:
    data = json.load(file)

def average_salary():
    # total_salaries = 0
    # for person in data['employees']:
    #     total_salaries += person['salary']
    # return total_salaries / len(data['employees'])
    total_salaries = []
    for person in data['employees']:
        total_salaries.append(person['salary'])
    return sum(total_salaries) / len(data['employees'])

new_person = '''{
      "name": "Roman Kutselepa",
      "role": "teacher",
      "gender": "male",
      "info": {
        "date_of_birth": "16.03.1988",
        "phone": "84 231 123"
      },
      "salary": 1500
    }'''
print(type(new_person))

new_person_dict = json.loads(new_person)
data['employees'].append(new_person_dict)

with open('new_data.json', 'w', encoding='utf8') as file:
    json.dump(data, file, indent=2, sort_keys=True)

print(average_salary())