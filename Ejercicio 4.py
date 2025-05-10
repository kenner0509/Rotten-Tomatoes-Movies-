import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
df_movies = pd.read_csv('./Data/Rotten Tomatoes Movies.csv')

# Crear una copia del DataFrame original
df_movies_copy = df_movies.copy()

# Explode de los géneros
df_genres_exploded = df_movies_copy.assign(
    genre=df_movies_copy['genre'].str.split(',')
).explode('genre')

# Eliminar espacios en blanco alrededor de los géneros
df_genres_exploded['genre'] = df_genres_exploded['genre'].str.strip()

# Calcular el promedio de audiencia por género
promedios_por_genero = df_genres_exploded.groupby('genre')['audience_rating'].mean().sort_values(ascending=False)

# Mostrar los 10 géneros con mejor audiencia
top_10_generos = promedios_por_genero.head(10)

# Gráfico circular
plt.figure(figsize=(8, 8))
top_10_generos.plot.pie(autopct='%1.1f%%', startangle=140)
plt.title("Top 10 géneros por promedio de audiencia")
plt.ylabel('')
plt.show()
