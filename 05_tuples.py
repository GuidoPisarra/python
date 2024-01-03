### tuplas

# Es similar a una lista pero es inmutable

my_tuple = tuple()
my_other_tuple = (1, 2, 3)

my_tuple = (37, 1.7, "Guido", "Pisarra", "Guido")

print(my_tuple)
print(type(my_tuple))
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple.count("Guido"))
print(my_tuple.index("Guido"))  # devuelve el primer elemento que encuentra
print(my_tuple + my_other_tuple)  #  se pueden sumar las tuplas

print(my_tuple[1:3])  # se puede seleccionar por rangos

my_tuple = list(my_tuple)  # se cambia el tipo a lista
print(type(my_tuple))
my_tuple[1] = 1.73
print(my_tuple)

# si quiero borrar la tupla debo hacer del para borrar la variable --> del my_tuple
