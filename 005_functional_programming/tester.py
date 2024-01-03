# def no_params():
#     # print('Hello world!')
#     return 'Hello planet!'
#
#
# def square_area(width, height):
#     result = width * height
#     return result
#
# def say_hello(name):
#     print(f'Hello {name}!')
#
# def say_hi():
#     name = input('Enter name: ')
#     print(f'Hi {name}!')
#
# say_hi()


# def something():
#     a = 10
#     b = 20
#     print('LOCAL', a, b, c)
#
#
# a = 1
# b = 2
# c = 3
# something()
#
# print('GLOBAL', a, b, c)

# names = []
# number = 1
#
# def add_name(name):
#     global number
#     names.append(name)
#     number += 1
#
# add_name('Jack')
# add_name('Mary')
# add_name('Sarah')
# add_name('Bob')
#
# print(names)
# print(number)

# def sample(a, b, c=0):
#     print(a + b + c)
#
# sample(1, 2, 3)

# print('Hello world!')


# def person_data(data):
#     name = data[0]
#     surname = data[1]
#     age = data[2]
#     print(f'Hello {name} {surname}.')
#
#
# person_data(['Jack', 'Smith', 25])


# def sum_many_numbers(num1, num2, **kwargs):
#
#     result = num1 + num2
#
#     print(kwargs)
#     return result
#
# print(sum_many_numbers(num2=20, num1=30, name='Jack', surname='Smith'))

# x = (1, 2, 3)
# y = (10, *x, 20, 30)
# print(y)


# def area(a, b):
#     return a * b
#
# def perimeter(a, b):
#     return (a + b) * 2
#
# def count_material(amount, a, b):
#     area_material = area(a, b) * amount
#     edge_material = perimeter(a, b) * amount
#     return {'total_area': area_material, 'total_edge': edge_material}
#
#
# print(count_material(10, 20, 40))