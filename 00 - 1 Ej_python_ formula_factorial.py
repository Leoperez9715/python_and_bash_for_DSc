# Ejercicios_python

#Crear una función para la formula factorial
#Forma normal, de menor a mayor
def factorial(n):
  resp = 1
  for i in range(1,n+1):
    resp = resp * i 
  return resp

print (factorial(5))

#Forma con recursividad
def fact_rec(n):
  if n == 0: #para el caso de "0! = 1"  
    return 1
  else:
    return n * fact_rec(n-1) 
  
print(fact_rec(5))
  
