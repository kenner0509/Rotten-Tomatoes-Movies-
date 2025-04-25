import pandas as pd

# 1. Importar las librerías necesarias
# 2. Leer el archivo CSV
# 3. Mostrar las primeras filas del DataFrame para revisar su contenido
# 4. Verificar los nombres de las columnas
# 5. Convertir la columna 'in_theaters_date' al tipo datetime
# 6. Verificar que la conversión fue exitosa (dtypes)

# 7. Mostrar si hubo valores no convertidos (NaT)

df_movies = pd.read_csv('./Data/Rotten Tomatoes Movies.csv')

print("Primeras filas del DataFrame:")
print(df_movies.head())

print("\nNombres de las columnas:")
print(df_movies.columns)

df_movies["in_theaters_date"] = pd.to_datetime(df_movies["in_theaters_date"], errors='coerce')

print("\nTipos de datos despues de la conversion:")
print(df_movies.dtypes)

missing_dates = df_movies['in_theaters_date'].isna().sum()
print(f"\nPelículas con fechas no reconocidas: {missing_dates}")