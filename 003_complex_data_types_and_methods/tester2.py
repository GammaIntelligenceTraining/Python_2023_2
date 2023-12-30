# empty = {}
# empty = dict()
# print(type(empty))
# print(bool(empty))

mix = {
    'name': 'Roman',
    'age': 35,
    'courses': ['Art', 'Math'],
    'personal_data': {'height': 179, 'weight': 95},
    1: 'Hello world!',
    True: 'Hello planet!',
    'age2': 35
}

# print(mix)
# print(len(mix))
# print(mix['surname'])
# print(mix.get('name', False))

# mix['name'] = 'Jack'
# mix['phone'] = '555-555-5555'
# # print(mix.get('name'), mix.get('phone'))
# new = {'name': 'Simon', 'age': 25, 'address': 'Tartu mnt. 18'}
# mix.update(new)
# print(mix)

# print(mix.get('courses')[1].upper())

# del mix['name']
# age = mix.pop('age')
# age2 = mix.popitem()
# mix[age2[1]] = age2[0]
# print(mix)
# print(age)
# print(age2)
#
# # print(list(mix))
# print(mix.keys())
# print(mix.values())
# print(mix.items())
