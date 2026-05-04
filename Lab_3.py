import pandas as pd 
import streamlit as st
import matplotlib.pyplot as plt

# 1. Cargar archivo de electric vehicles
df_electricv = pd.read_csv("Electric_Vehicle_Population-2.csv")

st.title("Tabla de Electric Vehicles")

# 2. Número de filas y columnas
filas, columnas = df_electricv.shape
st.write(f"Filas: {filas}, Columnas: {columnas}")

# 3. Nombres de columnas
st.subheader("Columnas del dataset")
st.write(df_electricv.columns.tolist())

# 4. Primeras 6 filas
st.subheader("Primeras 6 filas")
st.write(df_electricv.head(6))

# 5. Estadísticas generales
st.subheader("Estadísticas de variables numéricas")
st.write(df_electricv.describe())
#------------DIVISIÓN----------------
# 1. Cargar archivo de electric vehicles
df_gym = pd.read_csv("GymExerciseTracking.csv")

st.title("Tabla de Gym Exercises")

# 2. Número de filas y columnas
filas, columnas = df_gym.shape
st.write(f"Filas: {filas}, Columnas: {columnas}")

# 3. Nombres de columnas
st.subheader("Columnas del dataset")
st.write(df_gym.columns.tolist())

# 4. Primeras 6 filas
st.subheader("Primeras 6 filas")
st.write(df_gym.head(6))

# 5. Estadísticas generales
st.subheader("Estadísticas de variables numéricas")
st.write(df_gym.describe())
#------------DIVISIÓN----------------
# 1. Cargar archivo de electric vehicles
df_steam = pd.read_csv("steam_store_data_2024.csv")

st.title("Tabla de Steam Store")

# 2. Número de filas y columnas
filas, columnas = df_steam.shape
st.write(f"Filas: {filas}, Columnas: {columnas}")

# 3. Nombres de columnas
st.subheader("Columnas del dataset")
st.write(df_steam.columns.tolist())

# 4. Primeras 6 filas
st.subheader("Primeras 6 filas")
st.write(df_steam.head(6))

# 5. Estadísticas generales
st.subheader("Estadísticas de variables numéricas")
st.write(df_steam.describe())
#------------DIVISIÓN----------------
# 1. Cargar archivo de electric vehicles
df_netflix = pd.read_csv("netflix_titles.csv")

st.title("Tabla de Netflix Titles")

# 2. Número de filas y columnas
filas, columnas = df_netflix.shape
st.write(f"Filas: {filas}, Columnas: {columnas}")

# 3. Nombres de columnas
st.subheader("Columnas del dataset")
st.write(df_netflix.columns.tolist())

# 4. Primeras 6 filas
st.subheader("Primeras 6 filas")
st.write(df_netflix.head(6))

# 5. Estadísticas generales
st.subheader("Estadísticas de variables numéricas")
st.write(df_netflix.describe())


st.title("Parte 4. Exploración Avanzada (")

# --- CARGA DE ARCHIVOS ---
try:
    df_electricv = pd.read_csv("Electric_Vehicle_Population-2.csv")
    df_gym = pd.read_csv("GymExerciseTracking.csv")
    df_steam = pd.read_csv("steam_store_data_2024.csv")
    df_netflix = pd.read_csv("netflix_titles.csv")
except FileNotFoundError as e:
    st.error(f"No se encontró el archivo: {e.filename}")
    st.stop()

# ---------------------------------------------------------
# 1. VEHÍCULOS ELÉCTRICOS
# ---------------------------------------------------------
st.header("1. Análisis de Vehículos Eléctricos")

# Crear variable categórica
# Rangos: <100 (Bajo), 100-250 (Medio), >250 (Alto)
bins_electricv = [0, 100, 250, float('inf')]
labels_electricv = ['Bajo', 'Medio', 'Alto']
df_electricv['RangoCategoria'] = pd.cut(df_electricv['Electric_Range'], bins=bins_electricv, labels=labels_electricv, right=False)

st.subheader("Conteo por Categoría de Rango")
conteo_electricv = df_electricv['RangoCategoria'].value_counts()
st.write(conteo_electricv)

st.subheader("Gráfico de Distribución")
fig1, ax1 = plt.subplots()
conteo_electricv.plot(kind='bar', ax=ax1, color='teal')
ax1.set_title("Vehículos por Categoría de Rango Eléctrico")
ax1.set_xlabel("Categoría")
ax1.set_ylabel("Cantidad")
st.pyplot(fig1)

st.subheader("Análisis Agrupado (Promedios y Desviación)")
# Ajustar nombres de columnas según el CSV
resumen_electricv = df_electricv.groupby('RangoCategoria', observed=False).agg({
    'Base_MSRP': 'mean',
    'Model Year': 'mean',
    'Electric_Range': 'std'
})
st.table(resumen_electricv)

st.markdown("---")

# ---------------------------------------------------------
# 2. GIMNASIO
# ---------------------------------------------------------
st.header("2. Análisis de Gimnasio")

# Crear variable categórica
# Rangos: <3 (Baja), 3-5 (Moderada), 6-7 (Alta)
bins_gym = [0, 3, 6, 8]
labels_gym = ['Baja', 'Moderada', 'Alta']
df_gym['NivelFrecuencia'] = pd.cut(df_gym['Workout_Frequency (days/week)'], bins=bins_gym, labels=labels_gym, right=False)

st.subheader("Conteo por Nivel de Frecuencia")
conteo_gym = df_gym['NivelFrecuencia'].value_counts()
st.write(conteo_gym)

st.subheader("Gráfico de Frecuencia")
fig2, ax2 = plt.subplots()
conteo_gym.plot(kind='bar', ax=ax2, color='orange')
ax2.set_title("Registros por Nivel de Frecuencia al Gimnasio")
ax2.set_xlabel("Nivel")
ax2.set_ylabel("Cantidad")
st.pyplot(fig2)

st.subheader("Análisis Agrupado")
resumen_gym = df_gym.groupby('NivelFrecuencia', observed=False).agg({
    'Session_Duration (hours)': 'mean',
    'Experience_Level': 'mean',
    'BMI': 'std'
})
st.table(resumen_gym)

st.markdown("---")

# ---------------------------------------------------------
# 3. VIDEOJUEGOS (STEAM)
# ---------------------------------------------------------
st.header("3. Análisis de Videojuegos")

# Identificar nombres de columnas
col_p = 'price' if 'price' in df_steam.columns else 'Precio'
col_d = 'discount' if 'discount' in df_steam.columns else 'salePercentage'

# --- LIMPIEZA DE DATOS (PARA EVITAR EL TYPEERROR) ---

# 1. Limpiar PRECIO: Convertir a número y poner 0 a los "Free"
df_steam[col_p] = pd.to_numeric(df_steam[col_p], errors='coerce').fillna(0)

# 2. Limpiar DESCUENTO: 
# Si los descuentos tienen el signo '%', primero lo quitamos
if df_steam[col_d].dtype == 'object':
    df_steam[col_d] = df_steam[col_d].str.replace('%', '', regex=False)

# Convertir a número y poner 0 a los que estén vacíos o tengan texto
df_steam[col_d] = pd.to_numeric(df_steam[col_d], errors='coerce').fillna(0)

# ----------------------------------------------------

# Crear categorías de precio
bins_games = [0, 10, 25, float('inf')]
labels_games = ['Baja', 'Media', 'Alta']
df_steam['GamaJuego'] = pd.cut(df_steam[col_p], bins=bins_games, labels=labels_games, right=False)

st.subheader("Conteo por Gama de Juego")
conteo_steam = df_steam['GamaJuego'].value_counts()
st.write(conteo_steam)

st.subheader("Gráfico de Gamas")
fig3, ax3 = plt.subplots()
conteo_steam.plot(kind='bar', ax=ax3, color='purple')
ax3.set_title("Cantidad de Juegos por Gama de Precio")
ax3.set_xlabel("Gama")
ax3.set_ylabel("Cantidad")
st.pyplot(fig3)

st.subheader("Análisis Agrupado de Precios")
# Ahora que ambas columnas son números, el .agg() funcionará perfectamente
resumen_steam = df_steam.groupby('GamaJuego', observed=False).agg({
    col_p: ['mean', 'std'],
    col_d: 'mean'
})
st.table(resumen_steam)

st.markdown("---")

# ---------------------------------------------------------
# 4. NETFLIX
# ---------------------------------------------------------
st.header("4. Análisis de Netflix")

# Mapeo manual para Tipo de Audiencia
mapeo = {
    'G': 'Niños', 'TV-Y': 'Niños', 'TV-G': 'Niños', 'TV-Y7': 'Niños', 'TV-Y7-FV': 'Niños',
    'PG': 'Adolescentes', 'TV-PG': 'Adolescentes',
    'PG-13': 'Adultos Jóvenes', 'TV-14': 'Adultos Jóvenes',
    'R': 'Adultos', 'TV-MA': 'Adultos', 'NC-17': 'Adultos'
}
df_netflix['TipoAudiencia'] = df_netflix['rating'].map(mapeo)

st.subheader("Conteo por Tipo de Audiencia")
conteo_net = df_netflix['TipoAudiencia'].value_counts()
st.write(conteo_net)

st.subheader("Gráfico de Audiencias")
fig4, ax4 = plt.subplots()
conteo_net.plot(kind='bar', ax=ax4, color='red')
ax4.set_title("Contenido de Netflix por Audiencia")
ax4.set_xlabel("Audiencia")
ax4.set_ylabel("Cantidad")
st.pyplot(fig4)

st.subheader("Análisis Agrupado (Contenido y Duración)")
# Extraer número de la columna duration para promediar
df_netflix['duration_min'] = df_netflix['duration'].str.extract('(\d+)').astype(float)

resumen_net = df_netflix.groupby('TipoAudiencia', observed=False).agg({
    'type': lambda x: x.mode()[0] if not x.mode().empty else "N/A",
    'duration_min': 'mean'
}).rename(columns={'type': 'Contenido más común', 'duration_min': 'Duración Promedio'})

st.table(resumen_net)