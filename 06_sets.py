### set
# tiene de base un array, es similar a una lista pero desordenada
# los sets utilizan un hash para insertar elementos, por eso no tienen orden
# tampoco admiten repetidos ni acceder por indice

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set))  # inicialmente es un diccionario

my_other_set = {37, 1.7, "Guido", "Pisarra"}

print(type(my_other_set))  # luego de agregar elementos se transforma en un set

print(len(my_other_set))

my_other_set.add(23)  # inserta en cualquier lado
my_other_set.add(23)  # NO ADMITE repetidos
print(my_other_set)

print("Guido" in my_other_set)
print("Guiso" in my_other_set)

my_other_set.remove(23)
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))

my_other_set = {37, 1.7, "Guido", "Pisarra"}
print(my_other_set)
del my_other_set  # borro la variable

my_set = {37, 1.7, "Guido", "Pisarra", "Java"}

# se puede asignar a una lista, y ésta lo ordena automaticamente (no es muy recomendable)
my_list = list(my_set)
print(my_list)

my_other_set = {"Java", "Javascript", "Python", "PHP"}
my_other_set_languages = {"Java", "Javascript"}

# une ambos sets, pero desordenados y sin repetir
my_new_set = my_set.union(my_other_set)
print(my_new_set)
my_new_set = my_new_set.union({"go", "c#", "c++"})
print(my_new_set)

print(my_other_set.difference(my_other_set_languages))
