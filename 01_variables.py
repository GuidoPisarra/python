### variables ###

my_variable = 'HOLAAA'
my_int_variable = 1
my_int_to_str_variable = 123

print(my_variable, my_int_variable, sorted(my_variable), str(my_int_to_str_variable*2),str(my_int_to_str_variable) ,type(str(my_int_to_str_variable)))

name, surname, age = "guido", "pisarra", 37

print(9<<3)
print (name, surname, age)

print('ingrese edad')
#edad = float(input("Enter edad: "))
#print(edad)

first_name = 'Asabeneh'
last_name = 'Yetayeh'
language = 'Python'
formated_string = "I am %s %s. I teach %s " %(first_name, last_name, language)
print(formated_string)

a = 4
b = 3

print('{} + {} = {}'.format(a, b, a + b))

dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct['key1']) # value1
print(dct['key4']) # value4


person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street


person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

print (person)