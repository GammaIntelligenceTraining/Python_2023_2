import itertools
import itertools as it

# counter = it.count(1.5, -0.5)
# counter = it.cycle(['Hello', 'World'])
# counter = it.repeat([])

# for i in range(10):
#     print(next(counter))

#
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
#
# data1 = [100, 200, 300, 400]
# data2 = ['abc', 'def', 'ghi', 'jkl', 'mno', 'prs']
#
# data = list(zip(data2, counter))
# print(data)


# letters = ['a', 'b', 'c', 'd']
# numbers = [0, 1, 2, 3]

# order = false, reuse_value = false
# result = it.combinations(letters, 3)

# order = true, reuse_value = false
# result = it.permutations(letters, 4)

# order = true, reuse_value = true
# result = it.product(letters, numbers, repeat=2)

# order = false, reuse_value = true
# result = it.combinations_with_replacement(letters, 4)

# for line in result:
#     print(line)

#
# letters = ['a', 'b', 'c', 'd']
# numbers = [0, 1, 2, 3]
# numbers2 = [4, 5, 4, 3, 2, 1, 0, 4]
# selectors = [True, False, False, True]
#
# # result = it.compress(letters, numbers)
# # print(list(result))
# #
# # result = filter(lambda x: x % 2, numbers2)
# # print(list(result))
# #
# # result = it.filterfalse(lambda x: x % 2, numbers2)
# # print(list(result))
# #
# # result = it.dropwhile(lambda x: x > 2, numbers2)
# # print(list(result))
# #
# # result = it.takewhile(lambda x: x > 2, numbers2)
# # print(list(result))
#
# result = it.accumulate(numbers2)
# print(list(result))


def get_city(person):
    return person['city']

people = [
    {
        'name': 'Jack',
        'city': 'Tallinn'
    },
    {
        'name': 'Sarah',
        'city': 'Tallinn'
    },
    {
        'name': 'Bob',
        'city': 'Tallinn'
    },
    {
        'name': 'Sarah',
        'city': 'London'
    },
    {
        'name': 'Mary',
        'city': 'London'
    },
    {
        'name': 'Jane',
        'city': 'Tallinn'
    },
]
people.sort(key=lambda x: x['city'])
result = itertools.groupby(people, get_city)

copy1, copy2, copy3 = it.tee(result, 3)
print(list(copy2))
print(list(copy1))
print(list(copy3))