### diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {
    "Nombre": "Guido",
    "Apellido": "Pisarra",
    "Edad": 37,
    "Altura": 1.72,
    "lenguajes": {"Java", "PHP", "Go"},
    1: "Azul",
}

print(my_other_dict)

print(my_other_dict.get("Nombre"))

print(len(my_other_dict))
# se puede buscar el valor de una clave de estas dos formas
print(my_other_dict["Nombre"])
print(my_other_dict.get("Nombre"))

# asigno o modifico valor de la clave
my_other_dict["Altura"] = 1.70
print(my_other_dict["Altura"])

# agregando nueva key-value a un diccionario
my_other_dict["Ciudad"] = "Azul"
print(my_other_dict)

# se borra una clave-valor
del my_other_dict["Ciudad"]
print(my_other_dict)

# asi busca si la clave Guido existe
print("Guido" in my_other_dict)
# asi se busca si el nombre (valor) se encuentra en el diccionario
print("Guido" in my_other_dict["Nombre"])
print("Guiso" in my_other_dict)
print("Guiso" in my_other_dict["Nombre"])

# asi se busca si la clave se encuentra en el diccionario
print("Nombre" in my_other_dict)

print(my_other_dict.items())  # muestra todo
print(my_other_dict.keys())  # muestra las claves
print(my_other_dict.values())  # muestra los valores

# con esto se crea un nuevo diccionario pero sin valores
keys = ("Nombre", 1, "Departamento")
keys_new = ("Nombre", 1, "Departamento", "Piso")
my_new_dict = my_other_dict.fromkeys(keys)
my_new_dict_dict = dict.fromkeys(keys_new)
print(my_new_dict)
print(my_new_dict_dict)
# FIN crear un nuevo diccionario pero sin valores

# duplica un diccionario, pero sin los valores
my_new_dict_dict = dict.fromkeys(my_other_dict)
print(my_new_dict_dict)

# se le asignan valores a todas las claves del diccionario
my_new_dict = dict.fromkeys(my_new_dict, ["uno", "dos"])
print(my_new_dict)

# crea una lista de las claves
print(list(my_new_dict))
# crea una tuple de las claves
print(tuple(my_new_dict))
# crea una set de las claves
print(set(my_new_dict))


my_other_dict = {
    "Nombre": "Guido",
    "Apellido": "Pisarra",
    "Edad": 37,
    "Altura": 1.72,
    1: "Azul",
}
print(list(dict.fromkeys(list(my_other_dict.values()))))
