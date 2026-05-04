import pandas as pd 
import streamlit as st

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


