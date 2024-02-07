import datetime
class Employee:

    def __init__(self, first, last, pay):
        self.__first = first
        self.__last = last
        self.__pay = pay

    @property
    def first(self):
        return self.__first

    @property
    def last(self):
        return self.__last

    @property
    def pay(self):
        return self.__pay

    @property
    def full_name(self):
        return f'{self.__first} {self.__last}'

    @full_name.setter
    def full_name(self, name):
        first, last = name.split()
        self.__first = first
        self.__last = last

    @full_name.deleter
    def full_name(self):
        self.__first = None
        self.__last = None

    @property
    def email(self):
        return f'{self.__first.lower()}.{self.__last.lower()}@example.com'


emp1 = Employee('Jack', 'Smith', 2000)
emp2 = Employee('Sarah', 'Gold', 3000)

print(emp1.full_name)
emp1.full_name = 'Sarah Brown'
print(emp1.full_name)

del emp1.full_name
print(emp1.last)
