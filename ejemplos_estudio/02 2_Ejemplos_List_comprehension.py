import numpy as np
import time
numbers = [1,2,3,4,5,6]
doubles = [x*2 for x in numbers]

for y in numbers: 
    y = y*2
    print (y)

print(doubles)

hola = lambda x: x**3

a = hola(5)
print (a)

# Se pueden crear arrays con numpy y estan optimizadas para los calculos matematicos
list_a = list(range(10000000))
list_b = list(range(10000000))

# Se suman los elementos de la lista (normal y se calcula el tiempo)

star_time_exA = time.time # se usar time para calcular el tiempo en el que se comienza la iteración
result_A = [a + b for a,b in zip(list_a,list_b)] # zip() se usa para combinar las listas como un tuple. 

#----------------------------------------------------------------------------------#
### Uso funcion zip()

## Para emparerjas - Las listas deben tener el mismo tamaño, sino se queda con el tamaño de la lista mas corta
nombres = ['Alice', 'Bob', 'Charlie']
edades = [25, 30, 35]

emparejados = zip(nombres, edades)
print(list(emparejados)) #Crea un tuple donde junta los elementos de cada lista 
# Salida: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# la función zip(*pares) separa en dos listas separadas un conjunto, debe establecerse las dos variables
# A, B = zip(*Tuples)
pares = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
nombres, edades = zip(*pares)
print(nombres)  # Salida: ('Alice', 'Bob', 'Charlie')
print(edades)   # Salida: (25, 30, 35)

##Para iterar 
nombres = ['Alice', 'Bob', 'Charlie']
edades = [25, 30, 35]

for nombre, edad in zip(nombres, edades):
    print(f'{nombre} tiene {edad} años')
# Salida:
# Alice tiene 25 años
# Bob tiene 30 años
# Charlie tiene 35 años

#/////////////////////////////////////////////////////////////////////////////////////////
# uso de los f-strings
nombre = "Charlie"
edad = 25
altura = 1.75

texto = f"Mi nombre es {nombre}, tengo {edad} años y mido {altura:.2f} metros."
print(texto)
# Salida: Mi nombre es Charlie, tengo 25 años y mido 1.75 metros.