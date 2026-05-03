import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Análisis de dataset")

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
