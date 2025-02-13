from random import randint as ran
#  List comprehension with for loop to cube numbers
nums = [1, 2, 3, 4]
cubes = [num**3 for num in nums] 
print(cubes) # [1, 8, 27, 64]

# Generator function yields numbers one by one 
def num_sequence(n):
    for i in range(n): 
       yield i

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#Creacion de una lista de valores random 
scores = []
for i in range (10): #itera en 10 posiciones [1 - 10]
    scores.append(ran(i,10)) #se usa la funcion randinit de random (named as ran) pide dos argumentos
        #se pone (i, 10) porque la funcion pone en la lista (a, b) si pongo i en el inicio no hay valor inicial solo desde 0
print(scores)

# Esto se puede expresar en una sola linea, como una list comprehencion
print([ran(i,10) for i in range(10)]) 
# Formato -> Variable_name = [funcion for i in rango(puede ser cualquier tipo)]

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

#creacion de filtros con for
CAPS_u = []
caps_l = []

for letter in "Honey Capital DAyyyY":
    if letter.isupper(): #funcion de boolean que pregunta is upper? 
        CAPS_u.append(letter)
    elif letter.islower(): #funcion boolenana que pregunta "is lowwer?"
        caps_l.append(letter) #Lista.append(variable)

print(CAPS_u, "mayusculas", caps_l, "minusculas")

#misma expresion en listcomprehension
print([letter for letter in "Henrry Honey BuBU" if letter.isupper])
# formato -> Variable a ejecutar "Print(letter)" -- for variable in "string" if condicion (is letter upper?)
 
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Nest
lista_de_listas = [["a","b","c"],["d", "e", "f"], ["g","h","i"]]
flat = []

for sub_list in lista_de_listas: #Toma cada parametro de lista_de_listas, es decir cada lista pequeña
    for i in sub_list: # revisa los elementos de cada lista pequeña "a,b,c"...
        flat.append(i) #agrega cada elemento a la lista "flat"

print(flat)

# como hacer todo en una expresion
    # se inicia por la variable del for mas pequeño, el ultimo elemento a adicionar

Variable = [item for sub_list in lista_de_listas for item in sub_list] #item for inner loop in outter loop
# Variable = ['Var salida' - 'primer for (for list in list_of_lists) - 'segundo for' (Var salida in list)]
# Variable = [(Var_salida) (for listB in listA) (for var_salida in listB)]
# ListA = ["ListB", "listB", "ListB"]
# ListB = ["var","var","Var"]
print(Variable)

print(list(range(16, 0, -5)))
print('string' == "String")
a = 'string'
print(type(a),type("str"))