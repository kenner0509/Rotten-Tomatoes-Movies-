import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df_movies = pd.read_csv('./Data/Rotten Tomatoes Movies.csv')

# Contar cuántas películas tiene cada director
conteo_directores = df_movies['directors'].value_counts()

# Obtener los 10 directores más frecuentes
top_10_directores = conteo_directores.head(10)

# Filtrar el DataFrame original con estos directores
top_10_director_names = top_10_directores.index.tolist()
df_top_10 = df_movies[df_movies['directors'].isin(top_10_director_names)].copy()

# Calcular promedio de tomatometer_rating para ellos
promedios_directores = df_top_10.groupby('directors')['tomatometer_rating'].mean().sort_values(ascending=False)

# Gráfico de barras
plt.figure(figsize=(10, 6))
promedios_directores.plot(kind='bar', color='orange')
plt.title("Promedio de valoración de críticos - Top 10 Directores")
plt.xlabel("Director")
plt.ylabel("Promedio tomatometer_rating")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
