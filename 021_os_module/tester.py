import os
import time

# print(os.getcwd())
# # os.chdir('C:\\dev_cave\\')
# # print(os.getcwd())
# print(os.listdir())
#
# # os.mkdir('new_folder/another')
# os.makedirs('new/new1/new2')
#
# time.sleep(10)
#
# # os.rmdir('new')
# os.removedirs('new/new1')

# os.rename('sample.txt', 'unsorted/sample.txt')

# print(os.stat('sample.txt').st_ctime)

# data = os.walk(r'C:\Users\User\PycharmProjects\Python_2023_2\021_os_module\unsorted')
#
# for dirpath, dirnames, filenames in data:
#     print('Directory', dirpath)
#     print('Directories', dirnames)
#     print('Files', filenames)
#     for file in filenames:
#         print(file)
#     print()
# login = os.environ.get('database_username')
# password = os.environ.get('database_password')
#
# print(os.environ.get('HOMEPATH'))
# file = 'something.png'
# print(os.environ.get('HOMEPATH') + '\\' + file)

# print(os.path.join('C:\casdas\\', 'something.png'))
# print(os.path.basename('/somedir/dir2/sample.txt'))
# print(os.path.dirname('/somedir/dir2/sample.txt'))
# print(os.path.split('/somedir/dir2/sample.txt'))
# print(os.path.splitext('/somedir/dir2/sample.txt'))

print(os.path.isdir('sample'))
print(os.path.isfile('new'))
