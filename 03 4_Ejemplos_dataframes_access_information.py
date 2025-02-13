#Access data in the DF 
import pandas as pd
import numpy as np

#La forma mas comun de crear dataFrames es a partir de archivos
path = r"C:\Users\LENOVO\OneDrive\02 - Documentos\Phyton for everybody\Codigos Python\Tabla_datos_2.csv"
df = pd.read_csv(path)

#Metodo de Heads and Tails
heads = df.head() #por default muestra las 5 primeras filas de la tabla, a menos que se especifique ()
print(heads)
heads = df.head(3) #En este caso, se esta espeficando cuantas filas quiero que se muestren 
print(heads)
tails = df.tail() #contrario a heads, muestra las ultimas 5 filas por default
print(tails)

#Descriptive statistics
print(df.describe())
# muestra los datos estadisticos de las columnas que posean numeros o con los cuales se puedan hacer calculos
    # Conteo de elementos
    # promedio
    # desviacion estandar 
    # percentil 25, 50, 70
    # valor minimo y maximo 
# se pueden llamar los metodos por separado
print("Valor minimo de población desocupada: ", df["poblacion_Desocupada"].min())
print("Valor minimo de población ocupada: ", df["poblacion_Ocupada"].min())
print("Valor minimo de población total: ", df["poblacion_Total"].min())
print("Resumen:\n",df.min()) #muestra el valor para cada columna por separado, a menos que se establezca el rango o columna
#Tambien se puede obtener la información de los valores no numericos
print(df.describe(include="all")) #se usa la libreria numpy


#Se puede buscar el nombre de las columnas
print(df.columns)
# >>> Index(['sexo', 'poblacion_Desocupada', 'poblacion_Ocupada', 'poblacion_Total','estado'],

#tambien funciona seleccionando la columna con el metodo punto 
print(df.estado)

# se puede obtener valores de columnas en lista 
print(df[["poblacion_Desocupada","poblacion_Total"]]) #imprime las columnas solicitadas y ademas la primera de indices
#para estos casos lo mas optimo es usar loc e iloc

#iloc() se usa solo con indices numericos para filas y columnas
print(df.iloc[0]) #se usa para ubicar filas, se puede solo una posicion, rango y tambien indices [i,j]
print(df.iloc[0:3]) # rango de [a:b]
print(df.iloc[0:7,0]) # indice [[a:b,j]]con rango en filas pero no columnas
print(df.iloc[10:16,1:3]) # rango en filas y rango en columnas [a:b,i:j]

#loc se usa con los "tags" de las filas entonces no es el indice, aunque en este ejemplo es el mismo
print(heads)
#|      sexo|  poblacion_Desocupada|  poblacion_Ocupada|  poblacion_Total  estado|
#|0    Total|                 30743|            1766690|          1797433  Oaxaca|
#|1  Hombres|                 18948|             999821|          1018769  Oaxaca|
#|2  Mujeres|                 11795|             766869|           778664  Oaxaca|
print(df.loc[1:2],df.iloc[1:2]) #en loc se muestra el limite superior en iloc no, entonces 
    # loc muestra dos [1 y 2]
#      sexo  poblacion_Desocupada  poblacion_Ocupada  poblacion_Total  estado
#1  Hombres                 18948             999821          1018769  Oaxaca
#2  Mujeres                 11795             766869           778664  Oaxaca       sexo  poblacion_Desocupada  poblacion_Ocupada  poblacion_Total  estado

    # iloc muestra uno [1] no muestra el limite superior    
#1  Hombres                 18948             999821          1018769  Oaxaca

#se aplica lo mismo, para ubicar rangos pero se usan tags 
print(df.loc[0:7,"sexo"]) # indice [[a:b,"A"]]con rango en filas y tag en columna
print(df.loc[10:16,["poblacion_Desocupada","estado"]]) # rango en filas y lista de tags en columna [a:b,["A","B"]]