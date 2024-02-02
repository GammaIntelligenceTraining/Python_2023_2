import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='12345678',
    database='python_test'
)
conn.autocommit = True

my_cursor = conn.cursor()

# try:
#     my_cursor.execute('CREATE DATABASE python_test')
#     print('Database was created!')
# except:
#     print('Database exists!')
# try:
#     my_cursor.execute('CREATE TABLE person (name VARCHAR(100), age INTEGER)')
#     print('Table was created!')
# except:
#     print('Table exists!')
#
# n = 'Jack'
# a = 30
# print(f'INSERT INTO person (name, age) VALUES ("{n}", {a});')

# my_cursor.execute(f'INSERT INTO person (name, age) VALUES ("Sarah", 25);')
# my_cursor.execute(f'INSERT INTO person (name, age) VALUES ("Mary", 20);')
# my_cursor.execute(f'INSERT INTO person (name, age) VALUES ("Bob", 18);')
# conn.commit()
# my_cursor.execute(f'INSERT INTO person (name, age) VALUES ("Jack", 30);')

# person = ('Max', 28)
# sql_formula = 'INSERT INTO person (name, age) VALUES (%s, %s);'
# my_cursor.execute(sql_formula, person)
#
# people = [('John', 17), ('Jessica', 23), ('George', 40)]
# # my_cursor.executemany(sql_formula, people)
# for p in people:
#     my_cursor.execute(f'INSERT INTO person (name, age) VALUES ("{p[0]}", {p[1]});')
# my_cursor.execute('SELECT * FROM person;')

# result = my_cursor.fetchall()
# print(result)

# for person in result:
#     print(f'Hello {person[0]}')

# result = my_cursor.fetchone()
# result2 = my_cursor.fetchone()
# print(result, result2)

# result = my_cursor.fetchmany(4)
# result2 = my_cursor.fetchmany(4)
# print(result, result2)

my_cursor.execute('DROP SCHEMA python_test')