## creación de diferentes DF usando Pandas, Spark y Dask

## los ndarray son objetos los cuales tienen un tamaño de creación y solo un tipo de data dentro 
## se pueden crear con cualquier dimension (n-dimension) y se puede redimensionar

import numpy as np

data_1 = [1,2,3,4]
first_array = np.array(data_1) #El argumento es una lista, que vamos a volver un arreglo
print(first_array)

data_2 = [[1,2,3],[4,5,6],[7,8,9],[1,2,3]]
second_array = np.array(data_2) # se puede ingresar una lista de listas, con el mismo tamaño MXM 
print(second_array)

#podemos crear directamente una matriz de tamaño M con "1" o "0" en todas sus posiciones
M_ones = np.ones(12)    #[1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1. 1.] es un arreglo como una lista
M_zeros = np.zeros(12)  #[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] 
print(M_ones,"\n", M_zeros)

#tambien se pueden crear arreglos como si fuera un range
M_range = np.arange(10) #La función arange se toma como si fuera range() en listas
M_range_seq = np.arange(3,21,3) #igual que range (A,B,C) A = inicio B = Final C = Paso 
print(M_range,"\n",M_range_seq)  #[0 1 2 3 4 5 6 7 8 9] ; [ 3  6  9 12 15 18]

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#una vez creados los arreglos, se puede obtener información de dichos arreglos como la dimensión
forma_1 = first_array.shape 
dimension_1 = first_array.ndim
print(forma_1) #Cuenta los elementos que tiene (4,) osea que tiene 4 por ahora 
print(dimension_1) #cuenta la dimensión como es solo una lista es dimensión 1
print(first_array.size) #Cuenta el numero de elementos que tiene el arrego --> (4,) tiene solo 4
forma_2 = second_array.shape
dimension_2 = second_array.ndim
print(forma_2) #Cuenta los elementos que tiene (4,3) osea 4 listas con 3 elementos debe ser igual
print(dimension_2) # La dimensión en este caso es 2 porque hay filas o columnas
print(second_array.size) #Cuenta el numero de elementos que tiene el arreglo (4,3) 4x3  = 12 eleme

## NOTA: En el caso de tener una dimensión 3 seria varias matrices con filas y columnas. 

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#Cambio de forma de los arreglos.
doce = np.arange(12)
print(" Tamaño: ",doce.size,"\n Dimensiones: ",doce.ndim,"\n Forma: ",doce.shape)
# Tamaño:  12  
# Dimensiones:  1
# Forma:  (12,)
#con la función .reshape puedo usar el mismo numero de tamaño y distribuirlo de forma diferente
doce_new = doce.reshape(3,4)
print(doce_new)
print(" Tamaño: ",doce_new.size,"\n Dimensiones: ",doce_new.ndim,"\n Forma: ",doce_new.shape)
# Tamaño:  12 -> El tamaño permanece igual
# Dimensiones:  2 -> Las dimensiones cambian porque ahora hay filas y columnas
# Forma:  (3, 4) -> la estructura de la matriz cambio

# Este cambio tambien aplica para tener matrices de 3D, pero igual deben coincidir las multiplicaciones
array_3D_1 = doce.reshape(2,2,3) 
array_3D_2 = doce.reshape(4,3,1)
#Los arreglos se hacen de la forma (A,B,C) donde seria (N° de matrices, N° Listas, N°elementosxlista)
# En el primer caso seria 2 matrices de (2,3) donde 2 es filas y 3 columnas
# En el segundo caso seria 4 matrices de (3,1) donde 3 son filas y 1 columna
print(array_3D_1,array_3D_1.ndim,array_3D_1.shape)
print(array_3D_2,array_3D_2.ndim,array_3D_2.shape)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Se puede cambiar el tipo de elementos que se contienen, pero todos deben ser iguales. 
print(array_3D_1.dtype) #El tipo de los elementos sería int64 que es mas pesado que otros
#Pero se puede cambiar este elemento por otro tipo
darray = array_3D_1.astype(np.int8)# forma de  cambiar el tipo de un arreglo ya creado, se actualiza
print(darray.dtype)
print(darray)
#para cambiar el tipo de un arreglo cuando lo estoy creando, se establece con dtype= 
darray_new = np.arange(100,dtype=np.int64)
print(darray_new.nbytes)

darray_new [20] = 1