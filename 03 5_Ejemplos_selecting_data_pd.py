#SELECTING DATA IN A PANDAS DATAFRAME
import pandas as pd

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#Creacion de masks
    #Las mascaras, son lista de booleanos (true o false) que evaluan cada elemento de un DataFrame
    # Basado en unos parametros establecidos, nosotros ponemos las condiciones 

data = {'name': ['Ana', 'Carlos', 'Luis', 'Maria', 'Pedro'],
        'age': [23, 35, 19, 28, 41],
        'city': ['Madrid', 'Barcelona', 'Sevilla', 'Madrid', 'Valencia']}
df_exe = pd.DataFrame(data)
print(df_exe)
#     name  age       city | ["age"]>30
#0     Ana   23     Madrid | False
#1  Carlos   35  Barcelona | True
#2    Luis   19    Sevilla | False
#3   Maria   28     Madrid | False
#4   Pedro   41   Valencia | True

mask_exe = df_exe["age"] > 30 #crea una lista de True, False segun los elementos que cumplan con age>30
print(mask_exe)

#Con esta nueva lista, se puede filtrar los elementos y no por rango, sino por la condicion
filtered_df = df_exe[mask_exe]
print(filtered_df)
#     name  age       city
#1  Carlos   35  Barcelona
#4   Pedro   41   Valencia
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

file_path = r"C:\Users\LENOVO\OneDrive\02 - Documentos\Phyton for everybody\Codigos Python\USCG.Search.Rescue.Stats.csv"
df = pd.read_csv(file_path)
print(df.head())

#Creación de la mascara (mask)
mask = [False for _ in range(len(df))]
mask[3:7] = [True,True,True,True] #Tambien se puede [True]*4 los rangos a ambos lados deben corresponder
print (mask)

#Ahora se aplica la mascara al df 
print(df[mask]) #Esto retorna solo las filas que tienen [True] en la mask
print(df.loc[mask])

#con la mask se pueden crear operadores logicos y operadores de comparacación
mask = df.loc[:,"Lives Lost After CG Notification"] < df.loc[:,"Lives Lost Before CG Notification"]
print(mask)
print(df.loc[mask])
#Buscamos las columnas 
print(df.columns)


#compara los valores de cada elemento de cada columna para ver si A<B ?? los que sean asi marca [True]
# En pandas, se pueden usar operadores para poder usar los operadores logicos
    # And: &
    # Or:  |
    # Not: ~
Quantile50_cases = df["Cases"].quantile(0.5) #Buscamos el percentil 50 en lugar de usar describe
Quantile50_sorties = df["Sorties"].quantile(0.5)
print("Cases (50%): ", Quantile50_cases ,"\n", "Sorties (50%)", Quantile50_sorties)

#otra forma de buscr la info, es directamente usando la tabla de describe() como si fuera un dataFrame
desc = df.describe()
Quantile50_cases_sorties = desc.loc["50%",["Cases","Sorties"]]
print(Quantile50_cases_sorties)
#Cases      55945.5
#Sorties     4221.0

#Ahora con estos valores puedo aplicar los operadores logicos
mask = (df.loc[:,"Cases"]<Quantile50_cases) & (df.loc[:,"Sorties"]>Quantile50_sorties)
Filt_df = df[mask]
print(Filt_df[["Cases","Sorties"]])

#con toda esta info se puede crear una nueva columna 
print(df.columns) #Columnas antes de agregar la nueva columna 
    #[Fiscal Year', 'Cases', 'Responses', 'Sorties', 'Lives Saved',
    # 'Lives Lost After CG Notification', 'Lives Lost Before CG Notification',
    #'Total', 'Lives Unaccounted For ']

#para agregar la nueva columna se debe agendar con .loc[:,"Nuevo nombre"]
df.loc[:,"Saved per Sortie"] = df.loc[:,"Lives Saved"]/df.loc[:,"Sorties"]
print(df.columns)
print(df["Saved per Sortie"])

#se puede usar un metodo de pandas llamado unique para identificar los elementos unicos en una columna
#es como usar set() en un arreglo
print(df.Cases.unique())

#se puede filtrar una usando una mascara con df[mask] pero si agregamos ~ antes se invierte el filtro
no_filt = df[~mask]
print(no_filt)