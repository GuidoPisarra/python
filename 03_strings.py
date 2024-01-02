### strings ###

my_string = "My sring"
my_other_string = "My sring"

print(len(my_string))
print(len(my_other_string))
print(my_string+' '+my_other_string)

my_new_line_string= "string \ncon salto de linea"
my_new_line_string_con_tab= "string \tcon tabulacion"
my_scape_string= "string \\t escapado \\n linea "

print(my_new_line_string)
print(my_new_line_string_con_tab)
print(my_scape_string)

# Formato

name, surname, age = "Guido", "Pisarra", 37

print("Mi nombre es %s %s y mi edad es %s" %(name, surname, age))
print("Mi nombre es {} {} y mi edad es {}". format(name, surname, age)) 
print(f"Mi nombre es {name} {surname} y mi edad es {age}") # Es la mejor forma

### desempaquetado de caracteres ###

language = "python"
a, b, c, d, e, f = language

print (a)
print (e)


### division ###

language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[-1]
print(language_slice)

language_slice = language[1:2:4]
print(language_slice)

language_slice = language[0:6:2] ### los dos primeros son el rango y el ultimo numero es la cantidad que va a satear
print(language_slice)

### reversa

reverse_languaje = language[::-1]
print(reverse_languaje)

### funciones del sistema

print(language.capitalize())
print(language.upper())
print(language.lower())
print(language.count('t'))
print(language.isnumeric())
print('1'.isnumeric())
print(language.upper().isupper())
print(language.lower().isupper())
