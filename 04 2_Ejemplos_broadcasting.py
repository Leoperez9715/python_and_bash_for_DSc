#04 2_Ejemplos_broadcasting.py

import numpy as np
A1 = np.array([[1,2,3],
               [4,5,6],
               [7,8,9]])
A2 = np.ones(9,dtype=np.int64).reshape(3,3)
print(A1,A2)
A_12 = A1 + A2 # se realiza la suma de las dos matrices, pero estas deben tener la misma forma
print(A_12, A_12.dtype)

# Otra opcion para sumar valores a las matrices, es solo adicionar un numero unicamente 
print(A1+3)

A3 = np.array([1,1,1])
#Tambien se pueden sumar matrices que no sean simetricas entre ellas en el numero de filas
# Si tuviera un arreglo de (4,) [1,1,1,1] no serviria porque no tiene el mismo tamaño
# Entonces para hacer A(i,j) + B(a,b)  i,a deben tener el mismo tamaño
print(A1+A3)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
A4 = np.arange(10).reshape(2,1,5)
print(A4) # Es un arreglo 3D: 2 matrices de 1x5
#[[[0 1 2 3 4]]
#
# [[5 6 7 8 9]]]
A5 = np.arange(14).reshape(2,7,1)
print(A5)
#En este caso, se tiene otro caso 3D: 2 matrices de 7x1 

A6 = A4 + A5 #En el caso de las matrices 3D, la matriz resultante tendra el tamaño de los valores
# mas grandes en cada caso, toma el maximo, lo unico que debe coincidir es el numero de matrices
print(A6,A6.shape) #(2,1,5) + (2,7,1) = (2,7,5)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#MATRIX OPERATIONS 
M1 = np.arange(9).reshape(3,3)
M2 = np.arange(2,20,2).reshape(3,3)

#Transponer
M1_T = M1.transpose()
print(M1_T)

#Obtener la diagonal 
M1_Diag = M1.diagonal()
print(M1_Diag)

#Multiplicación de matrices
M3 = M1 * M2 # Esta es producto punto, cada valor se multiplica en la misma posición 
M4 = M1 @ M2 # multiplicación de matrices normal 
print(M1)
print(M2)
print(M3)
print(M4)