## GENERATOR EXPRESSIONS
# Son alternativas para almacenar memoria empleando list comprehension
# cuando creo un generador, no estoy dando un valor puntual. para poder usar un generador o poder obtener un valor 
# de él, debo llamar la funcion dentro del generador con la funcion next()
import sys

large_num = 9999999
l_squares = [x**2 for x in range(large_num)] # x^2 para los numeros de 1 - large_num (9999)
    #print(l_squares) 
print (sys.getsizeof(l_squares)) 
    # >>> 85175 es el tamaño en bytes del objeto l_squares o la memoria ocupada por los atributos del objeto

#Ahora, si quiero crear un generador, que no almacene nada a menos que yo lo requiera
g_squares = (x**2 for x in range(large_num)) #se usa () para identificar que es un generador
print(sys.getsizeof(g_squares)) # >>> 200 no cambia por mas que cambie large_num porque no almacena nada 

#para poder usar el generador, debo usasr la funcion next()
print("posicion 1: 0",next(g_squares),"posicion 2: 1",next(g_squares),"posicion 3: 2",next(g_squares))

for x in g_squares:
    print(x) # aqui sigue con la secuencia porque ya se uso next antes entonces va con posicion 4, 5...
    if x > 150:
        break

#Encadenar generadores
pares = (x for x in range(0,100,2)) #generador que pasa numeros de 2 en 2 de 0 a 100
div_tres = (y for y in pares if y%3 == 0) #generador con output y en pares si y es divisible por 3

print([x for x in div_tres])

#print((x for x in range(20))[3]) esto es un error porque el generador como no almacena memoria, 
# entonces no tiene posiciones, no puedo pedir una posicion especifica porque no se ha creado. 