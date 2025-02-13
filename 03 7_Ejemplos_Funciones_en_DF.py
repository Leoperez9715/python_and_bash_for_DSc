##Aplicar funciones a pandas 
import pandas as pd 
import numpy as np  


data = { "par": range(20,0,-2),
        "impar": range(1,21,2)}
df = pd.DataFrame(data)
print(df)

#La funcion sum() toma todos los elementos en una lista y retorna un solo valor con el total de esa suma 
print(sum(range(12))) #1+2+3+4+...+12 = 66

## El metodo .apply(x) me permite aplicar cualquier funcion a mi df cambiando el nombre en x
print(df.apply(sum))
#En este caso, al no indicar nada mas que la función, por default se aplica a columnas con numeros
        #|par      110
        #|impar    100
        #|dtype: int64

#puedo cambiar el sentido en el cual se aplique la funcion, cambiando el eje de operacion 
print(df.apply(sum,axis=1)) #en este caso, axis=1 indica que se haga en filas y no columnas
    #|0    21
    #|1    21
    #|2    21
    #|3    21
    #|4    21
    #|5    21
    #|6    21
    #|7    21
    #|8    21
    #|9    21
    #|dtype: int64

#el apply() se puede aplicar con funciones predeterminadas (sum,min...) pero se pueden usar funciones
#creadas con anterioridad

def hundred_plus (col): #Col indica que toma columna como un argumento
    if sum(col) > 100:
        return "no es mayor a 100"
    return "Es mas grande que 100"

print(df.apply(hundred_plus))

def label (row): #Row indica que toma las filas una por una de todas las columnas
    if row["par"] % 3 == 0: #funcion que pregunta si row[par] es divisible por 3, osea 0 en residuo sin decimales
        return True
    elif row["impar"] % 3 == 0:
        return True
    return False
    
print(df.apply(label,axis=1))

## Se pueden crar funciones que iteren en los elementos
def ret_list(row):
    ret_val = [False,False] #Esta va a ser la inicialización
    if row["par"] > 6:
        ret_val[0] = True
    if row["impar"] > 6:
        ret_val[1] = True
    return ret_val 

print(df.apply(ret_list,axis=1)) # cuando se aplica esta funcion, los retornos son por fila 
print(df.apply(ret_list,axis=1,result_type="expand")) #Con "expand" puedo guardar los elementos en un DF
#     (sin expand)           (Con expand)
#                              0      1
#0    [True, False]        0   True  False
#1    [True, False]        1   True  False
#2    [True, False]        2   True  False
#3     [True, True]        3   True   True
#4     [True, True]        4   True   True
#5     [True, True]        5   True   True
#6     [True, True]        6   True   True
#7    [False, True]        7  False   True
#8    [False, True]        8  False   True
#9    [False, True]        9  False   True

# ahora se pueden aplicar funciones a columnas individuales o filas individuales
# se debe indicar a que columna se aplica
def div_three (col):
    if col%3 == 0:
        return "divisible por 3"
    return "no es divisible por 3"

print(df.par.apply(div_three))
print(df["par"].sum()) # si lo quiero hacer por separado 


# Sample fruit price DataFrame
data = {'Fruit': ['Apple', 'Banana', 'Orange'],  
        'Price': [2.5, 1.2, 3.3]}
df = pd.DataFrame(data)

# Calculate average price  
avg_price = df['Price'].mean()  
print(avg_price)

# Filter prices > average
filter = df['Price'] > avg_price
df.loc[filter]

# isin() filter on fruits   
fruit_filter = df['Fruit'].isin(['Apple','Orange']) 
df.loc[fruit_filter]



