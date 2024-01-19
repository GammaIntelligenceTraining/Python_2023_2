# Student management system

# add_student (name, age, grade) 1-5
# display_students
# find_student (name) => student data
# update_student (name, age=None, grade=None) => if parameter passed, updates, else, leaves old value
# calculate_average_grade


students = []

def add_student(name, age, grade):
    student = {
        'name': name,
        'age': age,
        'grade': grade
    }
    # for person in students:
    #     if person['name'] != name:
    #         students.append(student)
    students.append(student)
    print(f'Student {name} was added to the system.')

add_student('Jack Smith', 17, 4)
add_student('Mary Gold', 18, 5)
add_student('Simon Bruno', 16, 3)
add_student('Sarah Jones', 17, 2)


def display_students():
    for person in students:
        print(f'Name: {person["name"]}, Age: {person["age"]}, Grade: {person["grade"]}')


def find_student(name):
    for person in students:
        if person['name'] == name:
            print(f'Name: {person["name"]}')
            print(f'Age: {person["age"]}')
            print(f'Grade: {person["grade"]}')
            return person
    print(f'Student {name} was not found!')
    return None

print(find_student('John'))


def update_student(name, age=None, grade=None):
    # for person in students:
    #     if person['name'] == name:
    #         if age:
    #             person['age'] = age
    #         if grade:
    #             person['grade'] = grade
    #         print('Student details updated')
    #         return
    # print(f'Student {name} was not found!')

    student = find_student(name)
    if student:
        student_index = students.index(student)
        if age:
            student['age'] = age
        if grade:
            student['grade'] = grade
        students.pop(student_index)
        students.insert(student_index, student)
        print('Student details updated.')
    else:
        print(f'Student {name} was not found!')

update_student('Simon Brun', age=10)


def calculate_avg_grade():
    if students:
        total_grade = 0
        for person in students:
            total_grade += person['grade']
        average = total_grade / len(students)
        print(f'Average grade is {average:.2f}')
    else:
        print('There are no students inside system!')

calculate_avg_grade()
print(students)

