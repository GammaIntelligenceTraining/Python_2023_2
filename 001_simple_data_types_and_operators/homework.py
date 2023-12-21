# Write a program that:
# 1. Calculates age from the given data (current_year - year of birth)
# 2. Find the missing part of the code (code_2)
#     a. Find the remainder of x divided by y
#     b. Multiply the obtained result by 13
#     c. Take the square root of the result
#     d. Take the integer part of the result
# 3. Combine the code into a separate variable
#     Example:
#         475-12-967
# 4. Print the string:
#     Example:
#         Hello Mary Gold. You are 26 years old. Your secret code is 475-12-967.


# years
current_year = 2023
year_of_birth = 1988
# code parts
code_1 = '354'
code_3 = 132
# name
user_name = 'John'
user_surname = 'Smith'
# code 2 data
x = 152
y = 132

age = current_year - year_of_birth

code_2 = int((x % y * 13) ** 0.5)

code = code_1 + '-' + str(code_2) + '-' + str(code_3)

print('Hello ' + user_name + ' ' + user_surname + '. You are ' + str(age) + ' years old. Your secret code is ' + code + '.')