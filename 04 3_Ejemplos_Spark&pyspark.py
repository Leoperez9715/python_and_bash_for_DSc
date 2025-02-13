#04 3_Ejemplos_Spark&pyspark

#Dask - es una libreria propia de python, esta diseñada para operaciones distribuidas
import dask.dataframe as dd 
import pandas as pd 
import random
import time

#Podemos crear un data frame con una gran cantidad de numeros
time_1 = time.time()
leng = 10000000
data = {"a":(random.randint(0,100) for _ in range(leng)),
        "b":(random.randint(2,200) for _ in range(leng))}

time_2 = time.time()
df = pd.DataFrame(data)
print(df.head)

time_3 = time.time()

lapso_1 = time_2 - time_1
lapso_2 = time_3 - time_2
print(f"El tiempo amtes de crear el DF fue {lapso_1: .6f} segundos")
print(f"El tiempo en crear el DF fue {lapso_2: .6f} segundos")

#El tiempo para crear un dataframe con pandas fue de aproximandamente 18s lo cual es un consumo de memoria
#considerable teniendo en cuenta que no era un valor demasiado grande. 
time_4 = time.time()
##DataFrame con Dask
ddf = dd.from_pandas(df,npartitions=3) #el numero de particiones indica cuantas operaciones al tiempo
print(ddf)
#|Dask DataFrame Structure:
#|                 a      b
#|npartitions=3
#|0              int64  int64
#|3333334          ...    ...
#|6666667          ...    ...
#|9999999          ...    ...
#|Dask Name: frompandas, 1 expression

# El df de Dask se ve diferente, muestra en cada columna que tipo de dato es y muestra el numero de
# particiones que se esta usando
time_5 = time.time()
lapso_3 = time_5 - time_4
print(f"El tiempo en crear el DF con Dask fue {lapso_3: .6f} segundos")
# El tiempo en crear el DF en dask fue de 0.29s a comparación de los 18 de pandas. 

# Para las operaciones, se debe usar el metodo ".compute" que indica que se debe realizar todas las 
# operaciones debido a que se usar el "lazy evaluation"

print(ddf.std().compute())
# Se pueden realizar operaciones intermedias, pero hasta que no tenga el ".compute" no se muestran como tal
result = ddf.a.sum() - ddf.b.sum()
print(result, "computado", result.compute())

#Cuando se usa Dask internamente se esta creando una grafica de operaciones y tareas
print(result.dask,"n/", result.visualize())
