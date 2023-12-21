# string_sample1 = 'Hello world world'
# string_sample2 = 'first lEtteR is lOwerCase. My name is'
# string_sample3 = '  **extra whitespace and stars***       '
# german_sample = 'DER fluß'
#
# # text = "that's"
# # text = 'My favourite book is "Metro 2033"'
# # text = 'that\'s'
# # text = """Hello ' "
# # people
# # of
# #         planet
# #                     Earth"""
# # print(text)
# # print(len('hello\''))
# # # [START:END:STEP]
# # text = string_sample1[:11:2]
# # print(string_sample1[:11:2])
# # print(string_sample1[-3:])
# # print(string_sample1[::-1] + 'Hello world')
# # a = 5
# # A = 10
# # print(a)
# # print(A)
#
# # print(string_sample2.upper())
# # print(string_sample2.isupper())
# #
# # print(german_sample.lower())
# # print(german_sample.casefold())
# # print(german_sample.islower())
# #
# # print(string_sample2.capitalize())
# # print(string_sample2.title())
# # print(string_sample2.istitle())
# #
# # print('hello world'.upper())
# # print(string_sample1[:11].upper()[5:7].isupper())
#
# print(string_sample3.strip('* '))
# print(string_sample3.rstrip())
# print(string_sample3.lstrip())
#
# print(string_sample1.replace('world', 'planet', 1))
# print(string_sample2.replace(' ', ''))
#
# print(string_sample1.count('world', 8, 14))
# print(string_sample1.find('world', 8, 14))
#
#

# print('\tHel\nlo')
print('Hello', end='***')
print('World', end='###')
print('common')

print('Year', 2023, True, None, sep='')

name = 'Mary'
salary = 3000
text = '{0}s salary is {1}. {0} is writing {2} code.'
print(text.format(name, salary, 'Python'))

product = 'Computer'
message = 'This {product} costs {cost:.2f}$.'
print(message.format(cost=1000, product=product))


print(f'Hello {name.upper()}. {name}s salary is {salary + 20:.2f}.')

byte_sting = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
print(byte_sting.decode('utf-8'))

text = 'Hello world'
print(text.encode('utf-16'))

print(b'\xff\xfeH\x00e\x00l\x00l\x00o\x00 \x00w\x00o\x00r\x00l\x00d\x00'.decode('utf-16'))