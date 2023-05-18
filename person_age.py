# class InvalidAge(Exception):
#     pass


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_birth_year(self, year):
#         name = self.name
#         age = (2023-year)
#         return cls(name, age)


# p = Person('Amy', 32)
# p.from_birth_year(1990)
# class Animal:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     @classmethod
#     def choose_color(cls, name):
#         color = input("Enter the color : ")
#         return cls(name, color)

#     def print_info(self, chosen_color):
#         print(chosen_color.name, chosen_color.color)


# p = Animal.choose_color('Dog')
# p.print_info(p)

class Ann:
    def __init__(self, name):
        self.name = name

    @classmethod
    def info(cls, name):
        name = 'Harry' + name
        return cls(name)


def print_info(person):
    print(person)


p = Ann.print_info('Brook')
print_info(p)
