import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df_movies = pd.read_csv('./Data/Rotten Tomatoes Movies.csv')

# Promedio de valoración del tomatómetro y la audiencia
promedio_criticos = df_movies['tomatometer_rating'].mean()
promedio_audiencia = df_movies['audience_rating'].mean()

print(f"Promedio de valoración por críticos: {promedio_criticos:.2f}")
print(f"Promedio de valoración por audiencia: {promedio_audiencia:.2f}")

# Calcular la diferencia entre audiencia y críticos
df_movies['rating_diff'] = df_movies['audience_rating'] - df_movies['tomatometer_rating']

# Histograma de las diferencias
plt.figure(figsize=(10, 6))
plt.hist(df_movies['rating_diff'].dropna(), bins=30, color='green', edgecolor='black')
plt.title("Distribucion, diferencias entre audiencia y crítico")
plt.xlabel("Diferencia (audiencia - críticos)")
plt.ylabel("Número de películas")
plt.grid(True)
plt.show()
