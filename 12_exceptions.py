### exception handling ###

number_one = 5
number_two = 5
number_three = "5"


try:
    result = number_one + number_two - int(number_three)
    print(result)
except:
    print("error al calcular")
# esto puede no estar, el else solo se ejecuta si no hay excepción
else:
    print(number_one)
# esto puede no estar, se ejecuta siempre
finally:
    print("FIN")


try:
    print(number_one + number_two - number_three)
except TypeError as error:  # error de tipo
    print("se produjo un Type Error " + str(error))  # se tiene que pasar error a str
except ValueError:  # error de valor
    print("se produjo un Value Error")
except Exception as excep:  # cualquier error
    print("Otro error " + str(excep))
