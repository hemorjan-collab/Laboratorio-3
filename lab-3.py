import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Análisis de dataset")
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

 #DATASET|1
st.header("Agregar nuevo registro de Gimnasio")
df=pd.read_csv("GymExerciseTracking.csv")

edad =st.number_input("Ingrese su edad")
genero=st.selectbox("Seleccione su género",["Male","Female"])
peso= st.number_input("Ingrese su peso en Kg")
altura=st.number_input("Ingrese su altura en metros (m)")
max_bmp=st.number_input("Ingrese su frecuencia cardíaca máxima (bpm)")
bmp_usual=st.number_input("Ingrese su frecuencia cardíaca usual (bpm)")
bmp_reposo=st.number_input("Ingrese su frecuencia cardíaca en reposo (bpm)")
duracion_sesion=st.number_input("Ingrese la duración de su sesión de ejercicio en horas")
calorias_quemadas=st.number_input("Ingrese las calorías quemadas durante su sesión de ejercicio")
tipo_ejercicio=st.selectbox("Seleccione el tipo de ejercicio",["Yoga","HIIT","Cardio","Strenght"])
procentaje_grasa=st.number_input("Ingrese su porcentaje de grasa corporal (%)")
toma_de_agua=st.number_input("Ingrese la cantidad de agua que toma diariamente (litros)")
frecuencia=st.number_input("Ingrese la frecuencia de sus sesiones de ejercicio (dias por semana)")
experiencia=st.selectbox("Seleccione su nivel de experiencia en el gimnasio", ["1", "2", "3"])
bmi=st.number_input("Ingrese su índice de masa corporal (BMI)")

if st.button("Agregar registro"):
    nuevo_registro={
        "Age": edad,
        "Gender": genero,
        "Weight (kg)": peso,
        "Height (m)": altura,
        "Max_BPM": max_bmp,
        "Avg_BPM": bmp_usual,
        "Resting_BPM": bmp_reposo,
        "Session_Duration (hours)": duracion_sesion,
        "Calories_Burned": calorias_quemadas,
        "Workout_Type": tipo_ejercicio,
        "Fat_Percentage": procentaje_grasa,
        "Water_Intake (liters)": toma_de_agua,
        "Workout_Frequency (days/week)": frecuencia,
        "Experience_Level": experiencia,
        "BMI": bmi
}
    
    df = pd.concat([df, pd.DataFrame([nuevo_registro])])
    st.success("Registro agregado exitosamente")

st.dataframe(df)

 #DATASET|2

generos = [
    "Action & Adventure",
    "Anime Features",
    "Anime Series",
    "British TV Shows",
    "Children & Family Movies",
    "Classic Movies",
    "Comedies",
    "Crime TV Shows",
    "Cult Movies",
    "Docuseries",
    "Documentaries",
    "Dramas",
    "Faith & Spirituality",
    "Horror Movies",
    "Independent Movies",
    "International Movies",
    "International TV Shows",
    "Kids' TV",
    "Korean TV Shows",
    "LGBTQ Movies",
    "Music & Musicals",
    "Reality TV",
    "Romantic Movies",
    "Romantic TV Shows",
    "Sci-Fi & Fantasy",
    "Science & Nature TV",
    "Spanish-Language TV Shows",
    "Sports Movies",
    "Teen TV Shows",
    "Thrillers",
    "TV Action & Adventure",
    "TV Comedies",
    "TV Dramas",
    "TV Horror",
    "TV Mysteries",
    "TV Sci-Fi & Fantasy",
    "TV Shows",
    "TV Thrillers"
]

st.header("Agregar nuevo registro de serie/pelicula de Netflix")
df=pd.read_csv("netflix_titles.csv")

id=st.text_input("Ingrese el ID de la serie/pelicula (formato: 's' seguido de un número)")
tipo=st.selectbox("Seleccione el tipo de programa: ", ["Movie", "TV Show"])
nombre=st.text_input("Ingrese el nombre de la serie/pelicula")
director=st.text_input("Ingrese el nombre del director")    
cast=st.text_input("Ingrese el elenco principal (separado por comas)")
pais=st.text_input("Ingrese el país de origen")
añadido=st.text_input("Ingrese la fecha de añadimiento a Netflix (formato: 'DD -abrv. mes- AA')")
estreno=st.text_input("Ingrese el año de estreno (formato: 'AAAA')")
rating=st.selectbox("Seleccione la clasificación por edades: ", ["G", "TV-MA", "TV-Y7", "PG", "PG-13", "TV-14", "R"])
duracion=st.text_input("Ingrese la duración (formato: '_ min' para películas o '_ Seasons' para series)")
categoria=st.multiselect("Seleccione las categorías (géneros) de la serie/pelicula: ", generos)
desc=st.text_area("Ingrese una breve descripción de la serie/pelicula")

if st.button("Agregar serie/pelicula"):

    nuevo_stream={
        "show_id": id,
        "type": tipo,
        "title": nombre,
        "director": director,
        "cast": cast,
        "country": pais,
        "date_added": añadido,
        "release_year": estreno,
        "rating": rating,
        "duration": duracion,
        "listed_in": ", ".join(categoria),
        "description": desc,

}
    
    df = pd.concat([df, pd.DataFrame([nuevo_stream])])
    st.success("Serie/pelicula agregado exitosamente")
st.dataframe(df)


###PARTE 3###
    #GIMNASIO#
st.header("Filtración de datos - gimnasio")
df1 = pd.read_csv("GymExerciseTracking.csv")

columnas=[
    "Age",
    "Gender",
    "Weight (kg)",
    "Height (m)",
    "Max_BPM",
    "Avg_BPM",
    "Resting_BPM",
    "Session_Duration (hours)",
    "Calories_Burned",
    "Workout_Type",
    "Fat_Percentage",
    "Water_Intake (liters)",
    "Workout_Frequency (days/week)",
    "Experience_Level",
    "BMI"
]

col_elegida=st.selectbox("Seleccione la columna para filtrar: ", columnas, key="columna_gym")
valor_ref=st.text_input("Ingrese el valor de referencia para filtrar: ")
igualdad=st.selectbox("Seleccione el tipo de comparación: ", ["Igual a", "Mayor que", "Menor que", "No aplica"], key="igualdad_gym")
genero=st.selectbox("Seleccione el género para filtrar: ", ["Male", "Female", "Todos"])
tipo_ej=st.selectbox("Seleccione el tipo de ejercicio para filtrar: ", ["Yoga", "HIIT", "Cardio", "Strenght", "Todos"])

if st.button("Filtrar datos"):
    df_filtrado=df.copy()

    if igualdad=="Igual a":
        df_filtrado = df_filtrado[df_filtrado[col_elegida]==valor_ref]

    elif igualdad=="Mayor que" and df[col_elegida].dtype != "object":
        df_filtrado = df_filtrado[df_filtrado[col_elegida]>float(valor_ref)]

    elif igualdad=="Menor que" and df[col_elegida].dtype != "object":
        df_filtrado = df_filtrado[df_filtrado[col_elegida]<float(valor_ref)]
    
    elif igualdad=="No aplica":
        st.warning("No se aplicará ningún filtro de comparación")

    if genero != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Gender"]==genero]

    if tipo_ej != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Workout_Type"]==tipo_ej]

        st.success("Datos filtrados exitosamente")

    st.dataframe(df_filtrado)

    #NETFLIX#
st.header("Filtración de datos - Netflix")
df2 = pd.read_csv("netflix_titles.csv")
df2["duration"] = df2["duration"].str.extract(r"(\d+)").astype(float) #Extraer solo el número de la duración y convertirlo a float para facilitar las comparaciones numéricas
#\d representa un dígito, + indica que se buscan uno o más dígitos, y los paréntesis indican que queremos capturar esa parte específica del texto. 
#luego, el resultado se convierte a tipo float para permitir comparaciones numéricas en la filtración.
df2["date_added"] = pd.to_datetime(df2["date_added"], errors="coerce") #Convertir la columna "date_added" a formato datetime,
#con manejo de errores para fechas mal formateadas

columnas=[
    "show_id",
    "type",
    "title",
    "director",
    "cast",
    "country",
    "date_added",
    "release_year",
    "rating",
    "duration",
    "listed_in",
    "description"
]
col_netflix=st.selectbox("Seleccione la columna para filtrar: ", columnas, key="columna_netflix")
id=st.text_input("Ingrese el ID de la serie/pelicula para filtrar (formato: 's' seguido de un número)")
tipo=st.selectbox("Seleccione el tipo de programa para filtrar: ", ["Movie", "TV Show", "Todos"])
origen=st.text_input("Ingrese el país de origen para filtrar (filtrado en inglés): ")
added=st.text_input("Ingrese la fecha de añadimiento a Netflix para filtrar (formato: 'DD -abrv. mes- AA')")
release=st.text_input("Ingrese el año de referencia para filtrar (formato: 'AAAA')")
rating=st.selectbox("Seleccione la clasificación por edades para filtrar: ", ["G", "TV-MA", "TV-Y7", "PG", "PG-13", "TV-14", "R", "Todos"])
duracion_min=st.text_input("Ingrese la duración de minutos para filtrar: ")
duracion_season=st.text_input("Ingrese la cantidad de temporadas para filtrar: ")
listed=st.multiselect("Seleccione las categorías (géneros) para filtrar: ", generos)
num_comparacion=st.selectbox("Seleccione el tipo de comparación: ", ["Igual a", "Mayor que", "Menor que", "No aplica"], key="comparacion")

if st.button("Filtrar datos de Netflix"):
    df_filtrado2=df2.copy()

    if id:
        df_filtrado2 = df_filtrado2[df_filtrado2["show_id"]==id]

    if tipo != "Todos":
        df_filtrado2 = df_filtrado2[df_filtrado2["type"]==tipo]

    if release:
        df_filtrado2 = df_filtrado2[df_filtrado2["release_year"]==int(release)]

    if rating != "Todos":
        df_filtrado2 = df_filtrado2[df_filtrado2["rating"]==rating]

    if origen:
        df_filtrado2 = df_filtrado2[df_filtrado2["country"]==origen]
    
    if added:
        fecha_usuario = pd.to_datetime(added, errors="coerce") # Convertir la fecha ingresada por el usuario a formato datetime,
       #con manejo de errores para fechas mal formateadas

        if num_comparacion=="Igual a":
            df_filtrado2 = df_filtrado2[df_filtrado2["date_added"]==fecha_usuario]
        elif num_comparacion=="Mayor que":
            df_filtrado2 = df_filtrado2[df_filtrado2["date_added"] > fecha_usuario]
        elif num_comparacion=="Menor que":
            df_filtrado2 = df_filtrado2[df_filtrado2["date_added"] < fecha_usuario]
        elif num_comparacion=="No aplica":
            st.warning("No se aplicará ningún filtro de comparación para duración mínima")


    if duracion_min:
        if num_comparacion=="Igual a":
            df_filtrado2 = df_filtrado2[df_filtrado2["duration"]==float(duracion_min)]
        elif num_comparacion=="Mayor que":
            df_filtrado2 = df_filtrado2[df_filtrado2["duration"] > float(duracion_min)]
        elif num_comparacion=="Menor que":
            df_filtrado2 = df_filtrado2[df_filtrado2["duration"] < float(duracion_min)]
        elif num_comparacion=="No aplica":
            st.warning("No se aplicará ningún filtro de comparación para duración mínima")

    if duracion_season:
        df_filtrado2 = df_filtrado2[df_filtrado2["duration"].str.contains(duracion_season)]

    if listed:
        for genero in listed:
            df_filtrado2 = df_filtrado2[df_filtrado2["listed_in"].str.contains(genero)]

    
    st.success("Datos filtrados exitosamente")
    st.dataframe(df_filtrado2)

#---------------------------------PARTE 4-------------------------------
st.title("Parte 4. Exploración Avanzada ")
# 1. VEHÍCULOS ELÉCTRICOS
st.header("1. Análisis de Vehículos Eléctricos")
#Se agrega una nueva columna, pero no se visualiza, porque no se dicta como tal en las intrucciones
# Rangos: <100 (Bajo), 100-250 (Medio), >250 (Alto), se representan en bin y labels, como si fuera una frasco y su etiqueta
bins_electricv = [0, 100, 250, float('inf')]
labels_electricv = ['Bajo', 'Medio', 'Alto']
#pd cut se utiliza como etiqueta
#Rango Categoría porque así pide la instrucción
df_electricv['Rango Categoria'] = pd.cut(df_electricv['Electric_Range'], bins=bins_electricv, labels=labels_electricv, right=False)

#Ahora realizo la segunda parte para saber la cantidad de registros de cada categoría
st.subheader("Conteo por Categoría de Rango")
#Sigo utilizando las variables establecidas desde el primer ejercicio y creo nuevas a modo de organización
# .count devuelve un recuento de valores, en este caso los de la nueva columna
conteo_electricv = df_electricv['Rango Categoria'].value_counts()
st.write(conteo_electricv)


