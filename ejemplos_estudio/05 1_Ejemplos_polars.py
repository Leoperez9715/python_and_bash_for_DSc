import polars as pl
import matplotlib.pyplot as plt

# Crear primer DataFrame
data1 = [{"fruit": "apples", "count": 10, "price": 0.50}, 
         {"fruit": "bananas", "count": 20, "price": 0.25}]
df1 = pl.from_dicts(data1)

# Crear segundo DataFrame
data2 = [{"fruit": "apples", "count": 10, "price": 0.45}, 
         {"fruit": "bananas", "count": 20, "price": 0.67},
         {"fruit": "oranges", "count": 15, "price": 0.75}]
df2 = pl.from_dicts(data2)

# Unir las dos tablas por la columna "fruit"
df_joined = df1.join(df2, on="fruit", how="inner", suffix="_right")

# Sumar el total de "count" y calcular el promedio de "price" después de la unión
df_aggregated = df_joined.group_by("fruit").agg([
    (pl.col("count") + pl.col("count_right")).alias("total_count"),
    (pl.col("price") + pl.col("price_right")).mean().alias("average_price")
])

print(df_aggregated)

# Extraer columnas para la gráfica
fruits = df_aggregated['fruit']
total_counts = df_aggregated['total_count']
average_prices = df_aggregated['average_price']

# Graficar un diagrama de barras con el total de "count"
fig, ax1 = plt.subplots()

# Crear el primer eje para el total de conteo
color = 'tab:blue'
ax1.set_xlabel('Fruits')
ax1.set_ylabel('Total Count', color=color)
ax1.bar(fruits, total_counts, color=color, alpha=0.6, label='Total Count')
ax1.tick_params(axis='y', labelcolor=color)

# Crear un segundo eje para el precio promedio
ax2 = ax1.twinx()  
color = 'tab:red'
ax2.set_ylabel('Average Price', color=color)  
ax2.plot(fruits, average_prices, color=color, marker='o', label='Average Price')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  
plt.title('Total Fruit Counts and Average Prices After Join')
plt.show()