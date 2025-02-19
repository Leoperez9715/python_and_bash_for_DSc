## Operadores logicos
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})

# Comparison operators 
print(df[df['A'] == 2]) # Filtro simple, solo toma las filas que cumplan con el criterio, se realiza sobre la columna
# df =     A B
#      (1) 2 5  La posicion es (1) porque (0) A:1 y B:4 no cumple se muestra la posicion que cumple

# Boolean operators
filter = (df['A'] > 1) & (df['B'] == 6)  
print(df[filter]) # Complex filter, en este caso, se deben cumplir los dos criterios. todos los elementos 
# de A cumplen pero solo el elemento en la 3ra columna (posición 2) cumple
# df =     A B
#      (2) 2 5 

# Filters with loc accessor
filter = df['A'] > 1 # Se crea el filtro, sobre "A" se buscan todas las filas con A > 1 
print(df.loc[filter]) # Se imprime el dataframe, usando loc y aplicando el filtro que se creo anteriormente

# isin() method
values = [2, 5] 
filter = df['A'].isin(values) #Es un metodo que me indica si los valores que cree, se encuentran en esa columna 
print(df[filter]) # De nuevo se aplica el filtro