## FUNCIONES GENERADORAS EN PYTHON

def return_num():
    for x in range(5):
        print(x) #no se detiene hasta que se completa todo el recorrido del for
     
return_num()

def gen_num():
    for x in range(5):
        yield x #Ahora en lugar de return, se usa yield, para guardar la posicion en todo momento y la función 
                #y el for se van a ejecutar cada vez que se llame 

gen = gen_num() #Debo asignar la funcion a una variable para comenzar a llamarla
print(next(gen)) # >>> 0 

print("segunda vez", next(gen)) #>>>> 1 entrega el valor, pero no reinicia la función

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def counter(x): #si uso un argumento de entrada tipo x = 12 el contador va a iniciar en 12 y de ahí sigue
    #x = 0
    while True:
        yield x
        x += 1 #Este es un loop infinito, sin embargo, no se ejecuta de manera infinita porque el yield 
               #hace que se ejecute el loop una vez cada que se llame

count = counter(12) #importante asignar la funcion a una variable 
print ("El conteo inicia en:" ,next(count))
print ("la cuenta en este moment va en", next(count)) #y siempre que lo requiera, llamo la función con next
print ("ahora la cuenta va en", next(count))

## Ejemplo de fibonacci
def fib():
    for cur in (0,1): #(0,1) es un tuple con los primeros dos numeros de la secuencia
        #print (cur)
        last = cur # en este caso inicia siento cur el primer valor 
        #en este caso, se esta inicializando la función primero recorre el 0 y 1 antes de pasar al while
        # Es por eso que se hacen los dos primeros llamados de la funcion
        # 1: (0,0)
        # 2: (1,1)
        yield cur
    while True:
        yield cur
        # 3: (1,1) Esta es la tercera llamada, para antes de serguir con la suma del last
        last, cur = cur, last + cur 
        # 4: (1, 2)
        # 5: (2, 3)
        # 6: (3, 5)
        print("last",last,"cur",cur)


fibonacci = fib()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))


# Generator function demonstrating yield

def num_sequence(n):
    """
    Generate sequence of numbers 
    up to n yielding one at a time
    """
    i = 0
    while i < n:
        yield i 
        i += 1

# Test generator function        
seq = num_sequence(5) 

print(next(seq)) # Print next number 
print(list(seq)) # en lugar de mostrar uno por uno, la funcion list(fun) muestra todo el contenido restante
                 # del generado 