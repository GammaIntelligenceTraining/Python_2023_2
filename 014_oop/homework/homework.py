class Animal:

    def __init__(self, name, species):
        self.__name = name
        self.__species = species

    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species


class Mammal(Animal):
    def __init__(self, name, species, fur_color):
        super().__init__(name, species)
        self.__fur_color = fur_color

    @property
    def fur_color(self):
        return self.__fur_color


class Bird(Animal):
    def __init__(self, name, species, wing_span):
        super().__init__(name, species)
        self.__wing_span = wing_span

    @property
    def wing_span(self):
        return self.__wing_span


class Reptile(Animal):
    def __init__(self, name, species, scale_type):
        super().__init__(name, species)
        self.__scale_type = scale_type

    @property
    def scale_type(self):
        return self.__scale_type


class Zoo:

    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def list_animals(self):
        for animal in self.__animals:
            print(f'{animal.name} ({animal.species})')

    def remove_animal(self, name):
        for animal in self.__animals:
            if animal.name == name:
                self.__animals.remove(animal)
                return
        print(f'{name} is not in the zoo')

    def get_animal_by_species(self, species):
        species_list = []
        for animal in self.__animals:
            if animal.species == species:
                species_list.append(animal)
        return species_list

    def count_animals(self):
        return len(self.__animals)

    def feed_animals(self):
        for animal in self.__animals:
            if isinstance(animal, Mammal):
                print(f'Feeding {animal.name} with {animal.fur_color} fur.')
            elif isinstance(animal, Bird):
                print(f'Feeding {animal.name} with {animal.wing_span} wing span.')
            elif isinstance(animal, Reptile):
                print(f'Feeding {animal.name} with {animal.scale_type} scales.')

zoo = Zoo()

lion = Mammal('Simba', 'lion', 'ornge')
eagle = Bird('Baldy', 'eagle', 6.2)
python = Reptile('Monty', 'python', 'diamond')

zoo.add_animal(lion)
zoo.add_animal(eagle)
zoo.add_animal(python)
print(zoo.count_animals())
# zoo.remove_animal('Monty')
zoo.list_animals()
# print(zoo.get_animal_by_species('lion')[0].fur_color)
print(zoo.count_animals())

zoo.feed_animals()