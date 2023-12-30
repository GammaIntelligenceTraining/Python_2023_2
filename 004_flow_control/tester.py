# id_code = input('Please enter your id: ')

# if len(id_code) == 11:
#     print('Correct!', id_code)
# elif len(id_code) > 11:
#     print('ID is too long!')
# else:
#     print('ID is too short!')

# if len(id_code) == 11:
#     print('Correct!', id_code)
# else:
#     if len(id_code) > 11:
#         print('ID is too long!')
#     else:
#         print('ID is too short!')

# x = {'name': 'Roman'}
# if x.isupper():
#     print(x.lower())
# else:
#     print(x.upper())
# x = input('Enter your name: ')
# y = input('Enter your surname: ')
# if x and not y:
#     print('Hello', x)
# elif x and y:
#     print('Hello', x, y)
# else:
#     print('You didn\'t enter a name!')

# people = ['Jack', 'Mary', 'Sarah', 'Bob']
#
# for person in people:
#     print(f'Hello {person}!')
#
# x = list(range(1, 11, 2))
# print(x)

# for number in range(100):
#     if number ** 2 % 2 == 0:
#         print(f'{number ** 2} EVEN')
#     else:
#         print(f'{number ** 2} ODD')

# for num1 in range(10):  # 10 loops
#     for num2 in range(10):  # 100 loops
#         for num3 in range(10):  # 1000 loops
#             for num4 in range(10):  # 10000 loops
#                 print(num1, num2, num3, num4)

# people = [('Jack', 'Smith', 25, 'male'), ('Mary', 'Gold', 20, 'female'), ('Sarah', 'Summers', 30, None), ('Bob', 'Green', 40, None)]
# for name, surname, age, gender in people:
#     if gender is None:
#         print(f'Hello {name} {surname}. You are {age} years old. Please update your gender!')
#     else:
#         print(f'Hello {name} {surname}. You are {age} years old. You are {gender}.')
# for name, surname, age, gender in people:
#     if gender is None:
#         print(f'Hello {name} {surname}. You are {age} years old.')
#     elif gender == 'male':
#         print(f'Hello {name} {surname}. You are {age} years old. You are male.')
#     elif gender == 'female':
#         print(f'Hello {name} {surname}. You are {age} years old. You are female.')

# for person in people:
#     # print(person)
#     print(f'Hello {person[0]} {person[1]}. You are {person[2]} years old.')

# for name, surname, age in people:
#     print(f'Hello {name} {surname}. You are {age} years old.')

# x = 0
# while x < 100:
#     print(x)
#     x += 1

colors = []

# condition = True
# while condition:
#     user_input = input('Enter color or type "exit" to quit: ')
#     if user_input.lower() == 'exit':
#         condition = False
#     else:
#         colors.append(user_input)
#         print(colors)

# while True:
#     user_input = input('Enter color or type "exit" to quit: ')
#     if user_input.lower() == 'exit':
#         break
#     elif user_input.lower() == 'print':
#         print(f'Colors: {", ".join(colors)}.')
#         continue
#     else:
#         colors.append(user_input)
#     print(f'{user_input} was added!')
#
# print('Good bye!')

while True:
    user_choice = input('Enter a number: ')
    if user_choice == '1':
        user_name = input('Enter your name: ')
        print(f'Hello {user_name}')
    elif user_choice == '2':
        print('You chose 2')
    elif user_choice == '3':
        print('You chose 3')
    elif user_choice == '4':
        print('You chose 4')
    elif user_choice.lower() == 'exit':
        print('Good bye!')
        break
    else:
        print('Out of range!')