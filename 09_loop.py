### loops

# while
my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
    if my_condition == 5:
        print("llego a 5")
        break  # corta el flujo del while
else:
    print("finalizo")

# for

my_list = [23, 25, 30, 37]
my_tuple = (37, 1.7, "Guido", "Pisarra", "Guido")
my_other_set = {37, 1.7, "Guido", "Pisarra"}
my_other_dict = {
    "Nombre": "Guido",
    "Apellido": "Pisarra",
    "Edad": 37,
    "Altura": 1.72,
    1: "Azul",
}

for element in my_list:
    print(element)
for element in my_tuple:
    print(element)
for element in my_other_set:
    print(element)

# imprime las claves
for element in my_other_dict:
    print(element)
# imprime los valores
for element in my_other_dict.values():
    print(element)
    if element == "Azul":
        break  # si pongo continue, la ejecucion continua sin importar nada
else:
    print("finalizo bucle for para my_other_dict")
