### funciones


def my_function():
    print("llamado a funcion")


def my_second_function(first_number, second_number):
    print(first_number + second_number)


# llamada de la función, los parametros no se pueden tipar, si los tipamos es solo a modo explicativo
# de querer hacerlo, hay que comprobar adentro
def my_third_function(first_number, second_number):
    return first_number + second_number


my_function()
my_second_function(1, 2)

my_result = my_third_function(1, 7)
print(my_result)


def print_name(name, surname):
    print(f"{name} {surname}")


print_name("Guido", "Pisarra")
# se puede invertir el orden, pero se deben declarar TODOS los parametros
print_name(surname="Guido", name="Pisarra")


# parametros por defecto
def print_name_with_default(name, surname, alias="Sin alias"):
    print(f"{name} {surname} {alias}")


print_name_with_default(surname="Guido", name="Pisarra", alias="Guidito")


# con el asterisco recorre todos los textos y/o valores
# esta funcion se llama funcion con parámetros arbitrarios
def print_texts(*texts):
    for texto in texts:
        print(texto.upper())


print_texts("hola", "como", "estas")
