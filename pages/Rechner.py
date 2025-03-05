import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
def calculate_bmi(weight, height):
   return weight / (height ** 2)
st.title("BMI-Rechner")
with st.form("bmi_form"):
   weight = st.number_input("Gewicht (kg)", min_value=1.0, step=0.1, format="%.1f")
   height = st.number_input("Größe (m)", min_value=0.5, step=0.01, format="%.2f")
   submit = st.form_submit_button("Berechnen")
if submit:
   if height > 0:
       bmi = calculate_bmi(weight, height)
       st.write(f"Ihr BMI beträgt: **{bmi:.2f}**")
       
       categories = ["Untergewicht", "Normalgewicht", "Übergewicht", "Adipositas"]
       values = [18.5, 24.9, 29.9, 40]
       colors = ['blue', 'green', 'orange', 'red']
       
       fig, ax = plt.subplots()
       bars = ax.bar(categories, values, color=colors)
       
       ax.axhline(y=bmi, color='black', linestyle='--', label=f'Ihr BMI: {bmi:.2f}')
       ax.legend()
       ax.set_ylabel("BMI-Wert")
       ax.set_title("BMI-Kategorien")
       
       st.pyplot(fig)
   else:
       st.error("Die Größe muss größer als 0 sein.")