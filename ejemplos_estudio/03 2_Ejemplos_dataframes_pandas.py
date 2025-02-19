## DATA IN PYTHON: PANDAS AND ALTERNATIVES

import pandas as pd
#Creación de un dataframe
data = {"name":["John","Mary","Peter","Josh","Anna","Diego"],
        "age":[25,30,35,22,12,28], "gender":["M","F","M","M","F","M"]}
#la tabla se crea como si fuera un diccionario.
df = pd.DataFrame(data)
#con .Dataframe, eldiccionario se modifica para que sea como una tabla
#  |     name  age gender
#  | 0   John  25  M
#  | 1   Mary  30  F
#  | 2   Peter 35  M
#  | 3   Josh  22  M
#  | 4   Anna  12  F
#  | 5   Diego 18  M

#se puede pedir que se muestre la tabla
print(df)
#Se puede solicitar solo una columna de la tabla, de la misma forma como se accede a la info de un diccionario
print(df["name"])
#para acceder a las columnas, cuando se crea el datafram a cada columna se le da un valor. se debe usar una funcion
print(df.iloc[2])
# loc: [2]
# name: peter
# age: 35
# gender: M
#se puede pedir un rango de indices
print("personas de 0 a 3",df.loc[0:3])

# se usa la funcion df.iloc[i,j] para buscar algun elemento indexado en la  tabla
print(df.iloc[0,0])

#Se puede extraer datos a partir de una condicion, por ejemplo mayores o menores
#En lugar de la función iloc, se usa la función loc, y se establece la condicon (edades > 25)
print("Edades mayores a 25",df.loc[df["age"]>25]) #Edad mayor a un rango
print("Edades entre 18 y 25: ",df.loc[(df["age"]>=18)&(df["age"]<=25)])# Edades entre 17 y 25
edades_pares = list(range(0,100,2))
print(edades_pares)
print("Edades pares: ",df.loc[df["age"].isin(edades_pares)]) # pregunta si los elementos estan en un conjunto
print("Nombres con J: ",df.loc[df["name"].str.contains("J")]) #pregunta si hay en ["name"] hay nombres con J

#Se pueden crear condiciones para las columnas
print("Ejemplo condicion \n", df.loc[df["gender"]=="M",["name"]]) #En este caso, si se cumple la condicion, se muestra la columna que se quiere

#Ademas de diccionarios, se puede crear un data frame de una lista de listas
data_2 =[["carl",43,123],["Carol",23,168],["Cas",30,14]] #Eb este caso, cada sublista es una fila 
    # y cada itemn de la lista corresponde a una columna, es decir cada posicion es el numero de la columna 
    # Entonces, cuando se imprime, las columnas no tienen nombre, sino numero
df_2 = pd.DataFrame(data_2)
# |       0   1    2|
# |0   carl  43  123|
# |1  Carol  23  168|
# |2    Cas  30   14|

# se pueden especificar los nombres de las columnas, usando el .dataFrame()
df_22 = pd.DataFrame(data_2, columns=["Name","Age","score"]) #Se debe crear el nuevo dataframe con la lista de columnas
print(df_22)

#La forma mas comun de crear dataFrames es a partir de archivos
path_2 = r"C:\Users\LENOVO\OneDrive\02 - Documentos\Phyton for everybody\Codigos Python\Tabla_datos_2.csv"
# en un string la secuencia "\0" se toma como ruta de escape, con lo cual se debe usar raw string r"" para que
# se identifique como un texto completo o: 1) cambiar todos los \ por /  2) cambiar \ por \\ en todo
# al momento de guardar el csv se debe guardar como csv-UFT8 sino toca hacer un proceso para decodificar. 
#df_3 = pd.read_csv(path_2)
#print(df_3)