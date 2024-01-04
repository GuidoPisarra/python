### clases


# Las clases comienzan con mayúsculas y camel case
class MyEmptyPerson:
    pass


class Person:
    def __init__(self, name, surname, edad=0):
        self.name = name
        self.surname = surname
        self.alias = "Guidin"
        self.__edad = edad  # con __ los declaro como privados

    def walk(self):
        print(f"{self.alias} " "camina")

    def set_name(self, name):
        self.name = name

    def get_edad(self):
        return self.__edad


# print(MyEmptyPerson)
# print(MyEmptyPerson())

my_person = Person("Guido", "Pisarra", 37)
print(my_person)
print(my_person.name)
print(my_person.surname)
print(f"{my_person.name} {my_person.surname} {my_person.alias} {my_person.get_edad()}")
my_person.walk()
my_person.set_name("Otro")
print(f"{my_person.name} {my_person.surname} {my_person.alias} {my_person.get_edad()}")
