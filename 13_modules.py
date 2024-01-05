### modules
# es una especie de libreria en el cual

import module

# no se puede importar ficheros  que tengan este nombre 10_fichero
from module import print_values, sumValue

module.sumValue(1, 3)

print_values({"a", "b", "c"})
sumValue(5, 6)

import math
import random
from math import pi as PI

print("PI " + str(math.pi))
print(math.pow(2, 4))
print(random.random())
print(PI)
