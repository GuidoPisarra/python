### listas ###

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [23, 25, 30, 37]


print(my_list)
print(len(my_list))

my_other_list = [37, 1.70, "Guido", 37, "Pisarra"]
print(my_other_list)
print(type(my_other_list))

print(my_other_list[0])
my_other_list.append("a")
print(my_other_list)
my_other_list.remove("a")  # elimina el primer elemento que encuentra, no todos

print(my_other_list)
# print(my_other_list.pop()) #pop elimina el último elemnto por defecto
# print(my_other_list)
print(my_other_list[-1])

# cuenta que cantidad de elementos iguales a 37 (en el ejemplo) tiene la lista
print(my_other_list.count(37))

age, height, name, other_age, surname = my_other_list

# concatenar listas
print(my_list + my_other_list)

my_list.insert(1, "Azul")
print(my_list)

my_list.remove("Azul")
print(my_list)

my_list.pop(2)  # puedo eliminar un elemento en concreto
print(my_list)

del my_list[1]
print(my_list)

my_new_list = my_list.copy()
print(my_list.clear())
print(my_new_list)
my_new_list.reverse()
print(my_new_list)
my_new_list.sort()
print(my_new_list)


my_new_list = [37, 1.70, "Guido", 37, "Pisarra"]
print(my_new_list[1:4])


my_list = "Hola pyhton"
print(my_list)
print(type(my_list))

### NO hay constantes, pero si se escribe una variable en mayúscula
### se considera constante
