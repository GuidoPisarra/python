### condicionales

my_condition = False

if my_condition:
    print("La condición es verdadera")
else:
    print("La condición es falsa")
    print("false")

my_condition = 5 - 1

if my_condition > 5:
    print("La condición es mayor a 5")
elif my_condition == 5:
    print("La condición es IGUAL 5")
else:
    print("La condición es menor 5")


my_condition = 5 * 3

if my_condition > 10 and my_condition < 20:
    print("La condición es verdadera")
else:
    print("La condición es falsa")

if my_condition > 10 or my_condition < 20:
    print("La condición es verdadera")
else:
    print("La condición es falsa")

if not my_condition > 10:
    print("La condición es verdadera")
else:
    print("La condición es falsa")

my_string = ""

if my_string:
    print("La cadena NO está vacía")
else:
    print("La cadena está vacía")

my_string = "Si"

if my_string == "si":
    print("La cadena es igual")
else:
    print("La cadena NO es igual")

print("FIN")
