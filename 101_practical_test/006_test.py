test_lst = [1, 2, 3, 4, 4, 5, 5, 5, 7, 8, 8, 8, 10, 10, 10]

result = {}

for num in test_lst:
    result[num] = test_lst.count(num)
print(result.values())

result_lst = []
for num in result:
    if result[num] == max(result.values()):
        result_lst.append(num)

print(result_lst)
# max_count = 0
# result = []
#
# for num in test_lst:
#     if test_lst.count(num) > max_count:
#         max_count = test_lst.count(num)
#
# for num in test_lst:
#     if test_lst.count(num) == max_count:
#         if num not in result:
#             result.append(num)
#
# print(result)
# print(list(set(result)))

x = {'name': 'Jack', 'surname': 'Smith', 'age': 25}

print(x.keys())
print(x.values())
print(x.items())