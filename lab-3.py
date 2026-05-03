import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Análisis de dataset")
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

st.header("Filtración de datos - gimnasio")
df= pd.read_csv("GymExerciseTracking.csv")

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

col_elegida=st.selectbox("Seleccione la columna para filtrar: ", columnas)
valor_ref=st.text_input("Ingrese el valor de referencia para filtrar: ")
igualdad=st.selectbox("Seleccione el tipo de comparación: ", ["Igual a", "Mayor que", "Menor que"])
