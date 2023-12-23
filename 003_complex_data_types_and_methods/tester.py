# empty_list = []
# print(type(empty_list))
# empty_list = list()  # Can be used to convert types to list.
# print(type(empty_list))
# print(bool(empty_list))
#
# print(bool(''))
#
# word = 'World'
# filled_list = [123, 0.32423, 'Hello', word, [1, 2, [9, 9, 9, 8], 3, 4, 5], None]
# print(len(filled_list))
# # print(filled_list[1:2])
# print(filled_list[4][2][-1])
# courses = ['History', 'Math', 'Literature', 'Physics', 'Programming', 'art', 'english', '1231', '2352']
# numbers = [1, 5, 6, 8, 3, 4, 2]
# print(courses)
# print(id(courses))
# courses[1] = 'Art'
# print(id(courses))
# print(courses)
# courses.append('Art')
# print(courses[0])
# courses.insert(1, 'English')
# print(courses[0])
# courses.extend(['Art', 'English'])
# courses.remove('Math')
# removed = courses.pop(2)
# print(removed)

# courses.reverse()
# courses.sort(reverse=True)

# print(min(courses))
# print(max(courses))
# print(sum(courses))

# a = [[1, 2], [3, 4], [1, 6]]
# a.sort()
# print(a)
# print('World' in 'Hello world!')
# print('Math' in courses)
# print(1 in numbers)
# print(list('hello world'))
# words = 'hello world, planet'.split(', ')
# print(words)
# print(courses)
# # print(str(courses))
# print(', '.join(courses))

# print(courses + numbers)
# print(courses[:3] + courses[6:])

# courses2 = courses.copy()
# courses.append('Art')
# courses2.append('Economics')
#
# print(courses)
# print(courses2)

# courses = ('History', 'Math', 'Math', 'Math', 'Literature', 'Physics', 'Programming', 'art', 'english', '1231', '2352')
# print(id(courses))
# print(courses.count('Math'))
# print(courses.index('Math'))
# print(courses[6])
# print(min(courses))
# courses = list(courses)
# courses[1] = 'Economics'
# courses = tuple(courses)
# print(courses)
#
# print((1, 2, 3) + (4, 5, 6))

# courses = {'History', 'Math', 'Math', 'Math', 'Literature', 'Physics', 'Programming', 'art', 'english', '1231', '2352'}
# print(type(courses))
# print(courses)

# courses.add('Economics')
# courses.remove('Math')
# courses.pop()
# courses.update([1, 2, 3])
# print(courses)

# set1 = {'Math', 'Physics', 'History', 'Economics'}
# set2 = {'Physics', 'Economics', 'Art', 'Programming'}
#
# print(set2.intersection(set1))
#
# print(set1.difference(set2))
# print(set2.difference(set1))

# x = ['One', 'One', 'Two', 'Three', 'Three', 'Four']
# x = list(set(x))
# print(x)

# x = 1
# if x == 5:
#     print('X is equal to 5')
# elif x > 5:
#     print('X is greater than 5')
# else:
#     print('X is less than 5')
#
# print('Good bye!')

# x = 5
# if x > 0:
#     print('X is larger than ZERO')
# if x > 3:
#     print('X is larger than THREE')

x = 0
if x > 0 and x < 10:
    print('Hooray!')
if x > 0 or x < 0:
    print('Not a Zero')