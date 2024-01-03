user_lst = input('Enter list items, use "," as separator: ').split(', ')

for element in user_lst[::-1]:
    print(element)