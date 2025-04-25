import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df = pd.read_csv('./Data/Rotten Tomatoes Movies.csv')

# 1. ¿Cuántas películas hay en total?
num_peliculas = len(df)
print(f"Total de películas: {num_peliculas}")

# 2. ¿Cómo se distribuyen las calificaciones?
distribucion_calificaciones = df['tomatometer_status'].value_counts()
print("\nDistribución de calificaciones:")
print(distribucion_calificaciones)

# 3. Visualizar la distribución de calificaciones con un gráfico circular
plt.figure(figsize=(8, 6))
plt.pie(
    distribucion_calificaciones,
    labels=distribucion_calificaciones.index,
    autopct='%1.1f%%',
    startangle=140
)
plt.title('Distribución de Calificaciones (Tomatometer Status)')
plt.axis('equal')
plt.show()






