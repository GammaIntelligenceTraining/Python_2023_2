import csv

# with open('csv_files/test.csv', 'r', encoding='utf8') as file:
#     csv_list = csv.reader(file)
#     # print(csv_list)  # iterator
#     with open('csv_files/test_copy.csv', 'w', encoding='utf8') as wfile:
#         csv_writer = csv.writer(wfile, delimiter=',', lineterminator='\n')
#         # columns = next(csv_list)
#         # for line in csv_list:
#         #     # print(f'Hello *** {line[0]}')
#         #     csv_writer.writerow(line)
#         csv_writer.writerows(csv_list)
#
# with open('csv_files/test_copy.csv', 'r', encoding='utf8') as file:
#     csv_data = list(csv.reader(file, delimiter=','))
#     print(csv_data)
#     for line in file:
#         print(line)

# with open('csv_files/test.csv', 'r', encoding='utf8') as file:
#     csv_list = csv.DictReader(file, fieldnames=['B', 'D', 'T'])
#     next(csv_list)
#     # print(list(csv_list))
#     with open('csv_files/test_copy.csv', 'w', encoding='utf8') as wfile:
#         csv_writer = csv.DictWriter(wfile, delimiter=',', lineterminator='\n', fieldnames=['B', 'D', 'T'])
#         # columns = next(csv_list)
#         csv_writer.writeheader()
#         for line in csv_list:
#             # print(f'Hello *** {line[0]}')
#             csv_writer.writerow(line)
#         # csv_writer.writerows(csv_list)
#
# with open('csv_files/test_copy.csv', 'r', encoding='utf8') as file:
#     csv_data = list(csv.reader(file, delimiter=','))
#     print(csv_data)
#     for line in file:
#         print(line)

cars = [
    {
        'make': 'Honda',
        'model': 'Civic',
        'mileage': 10000,
        'color': 'red'
    },
    {
        'make': 'BMW',
        'model': '320i',
        'mileage': 45000,
        'color': 'black'
    },
    {
        'make': 'Audi',
        'model': 'A6',
        'mileage': 24000,
        'color': 'blue'
    },
]
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# squares = map(lambda x: [x, x ** 2, x ** 3], numbers)
# print(list(squares))

def change_cars(car):
    return {
        f"{car['make']} {car['model']}": {
            'mileage': car['mileage'],
            'color': car['color']
        }
    }
# new_cars = []
# for car in cars:
#     new_cars.append(change_cars(car))
#
# new_cars = map(change_cars, cars)
# print(list(new_cars))

def evens(num):
    return not num % 2

even_numbers = filter(evens, numbers)
print(list(even_numbers))
