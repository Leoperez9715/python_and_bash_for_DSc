import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

#obtención de los datos de paises
life_df = pd.read_csv("expectancy.csv") #Lectura del excel y convertir en DF
#life_df.rename(columns={"my-life-expectancy":"both"}) #
life_df["mf-life-expectancy"] = life_df["both"]
print(life_df.head(75))

#obtención de datos de felicidad
happiness_df = pd.read_csv("happiness-2021.csv")
print(happiness_df.head())

#Ya con los dos dataframes, se puede usar merge
df = happiness_df.merge(life_df)
print(df.head(25), df.shape)

#print(df.corr())