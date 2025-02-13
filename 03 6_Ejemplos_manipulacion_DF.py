# Ejemplos manipulación DF 
import pandas as pd
data = {'name': ['Ana', 'Carlos', 'Luis', 'Maria', 'Pedro'],
        'age': [23, 35, 19, 28, 41],
        'city': ['Madrid', 'Barcelona', 'Sevilla', 'Madrid', 'Valencia']}
df = pd.DataFrame(data)
#print(df)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## RENAMING
# Se puede usar la función rename() para cambiar tanto los nombres de las columbas como los indices
df = df.rename(columns={"name":"nombre"}) # se debe guardar en una nueva variable o actualizar el df
#print (df)

#se puede usar la misma función pero esta vez con los indices de la tabla 0,1,2... 
df = df.rename(index={0:"a",1:"b",2:"c",3:"d",4:"e"})
#print(df)

#si no quiero actualizar la variable, porque los cambios son temporales puedo usar la funcion inplace
df.rename(columns={"age":"edad","city":"ciudad"}, inplace=True)
print(df) #no tube que almacenar en ninguna variable la modificación que ya hice

df.reset_index(inplace=True) #funcion reinicia los indices, pero los creados lo deja en una nueva columna
#ahora hay una nueva columna que se llama "index" 
print(df)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## DROP/ELIMINAR

#drop x columnas
df.drop(columns="index",inplace=True)
print(df)

#drop x fila
df.drop(index=0,inplace=True)
print(df)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Cambiar tipo
print(df.edad) #Los elementos en un dataframe se consideran objetos, es por eso que se deben cambiar
df.edad = df.edad.astype(str)
print(df.edad)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Combinar filas y crear una nueva
df["nombre y ciudad"] = df.nombre + " en " + df.ciudad + " a los " + df.edad 
df.reset_index(drop=True,inplace=True) #Reinicia el conteo de los indices, a pesar de haber eliminado
print(df)

##UPDATE DATAFRAME DATA
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
data_ = {"first":["Carl","Francis","Sam"],
         "last":["Po","Nyguen","Smith"],
         "age":["32","45","22"],
         "CH_count":[12, 14, 39]}
clients = pd.DataFrame(data_)
print(clients)
## Agregar filas: Para agregar filas o nueva información (Pero no columnas)
## es necesario crear una nueva dataframe con la información y adicionarla
new_data = {"first":["Sue","Boya"],
         "last":["Rankler","Maple"],
         "age":["93", "12"],
         "CH_count":[22, 1]}
new_clients = pd.DataFrame(new_data)
print(new_clients)

##Se adiciona por medio del metodo .append()
clients = pd.concat([clients, new_clients],ignore_index=True)
print(clients)
#Ahora con la nueva tabla e info, se puede actualizar o cambiar la info segun se necesite
clients.loc[0,"first"] = "Carlos"
clients.loc[0:1, "CH_count"] = -1 #El loc se fija en el index, no en la posicion [a:b] en rango 
clients.iloc[0:1,1] = "Pérez" #el iloc si considera posicon entonces es [a:b-1] en rango 
print(clients)


#Se pueden realizar operaciones matematicas
clients.CH_count = clients.CH_count + 3 #Esto es actualizando la variable, pero se puede hacer "inplace"
clients.CH_count -= 2 #Este es un inplace que me mantiene la variable cambiada sin asignarla nuevamente 
print(clients)

#Se puede reemplazar valores en toda la matriz
clients.replace(0,1,inplace=True)
print(clients)