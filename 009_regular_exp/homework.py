import re

# text1 = '#121212, #NNGGSS, #0099562213, #AA0012'
# pattern1 = re.compile(r'#[0-9A-Fa-f]{6}\b')
#
# matches1 = pattern1.finditer(text1)
# for match in matches1:
#     print(match)
#
# text2 = '23:12, 234:40, 25:39, 15:61, 00:00, 23:59, 01:43, 20:99'
# pattern2 = re.compile(r'\b([01]\d|2[0-3]):[0-5][0-9]\b')
#
# matches2 = pattern2.finditer(text2)
# for match in matches2:
#     print(match)
#

# with open('people.txt', 'r', encoding='utf8') as file:
#     data = file.read()
#
# address_ptrn = re.compile(r'\d{3} [A-Za-z\d]+ St\., [A-Za-z- \']+ [A-Z]{2} \d{5}')
#
# address_matches = list(address_ptrn.finditer(data))
# print(len(address_matches))
# for address in address_matches:
#     print(address)

# people_ptrn = re.compile(r'([A-Za-z-]+ [A-Za-z-]+)\n')
#
# people_matches = list(people_ptrn.finditer(data))
# print(len(people_matches))
# for person in people_matches:
#     print(person.group(1))

text3 = 'Hello people!'

# pattern3 = re.compile(r'[A-Za-z0-9]')
#
# matches3 = list(pattern3.finditer(text3))
#
# if len(matches3) != len(text3):
#     print('false')
# else:
#     print('true')

# pattern3 = re.compile(r'[^A-Za-z0-9]')
#
# matches3 = list(pattern3.finditer(text3))
# if len(matches3):
#     print('false')
# else:
#     print('true')

pattern4 = re.compile(r'\b[1-8]\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{4}\b')

