# number = input('Enter number: ')
# # print('DIGIT', number.isdigit())
# # print('DECIMAL', number.isdecimal())
# try:  # Check code for critical error
#     result = int(number) ** 2
#     # int(number) / 0
#
#     raise UserWarning
# except ValueError:  # Executes in case of error inside try:
#     print(number, 'is not an integer!')
# except ZeroDivisionError:
#     print('You are trying to divide by 0.')
# except Exception:
#     print('Hello')
# else:  # Executes in case of no error inside try:
#     print(result)
# finally:  # Executes no matter what
#     print('Good bye')

# print(10 / 0)
# print(int('asdasd'))

raise ValueError
