import pandas as pd
import pickle

#Crear la tabla con los pandas 
data = {"name":["John", "Mary", "Sarah"], "age": [25,32,28]}
df = pd.DataFrame(data)

#print(df)

for index, row in df.iterrows():
    print(row['name'], row['age'])

df.to_csv("data.csv",index=False)

new_data = pd.read_csv("00 data_2.csv")
#print (new_data)

# Pickling - Serialize the DataFrame
pickle.dump(df, open('data.pkl', 'wb')) 
df3 = pickle.load(open('data.pkl', 'rb'))
#----------------------------------------------------------------------------------------------------------#

frame_01 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}) # SE crea la tabla con cada elemento del diccionario
#como una columna 
# i col1 col2
# 1  1    3
# 2  2    4 

def increment(x): #Se define una función, esta solo aplica una ecuación sencilla de x + 1 
    return x + 1

frame_01['col1'] = frame_01['col1'].apply(increment)
#Se aplica el incremento a la columna 1 col1 :[1,2] ----> col1: [2,3]
# i col1 col2
# 0  2    3
# 1  3    4 

print(frame_01)

#---------------------- USING SPARK -----------------------------
# Example Spark setup

#sc = pyspark.SparkContext()

#rdd = sc.parallelize([1, 2, 3])
#print(rdd.collect())