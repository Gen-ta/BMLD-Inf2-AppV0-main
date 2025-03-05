import streamlit as st
import matplotlib.pyplot as plt
import datetime
import numpy as np

def calculate_bmi(weight, height):
    return weight / (height ** 2)

st.title("BMI Rechner")

height = st.slider("Wählen Sie Ihre Größe (m)", min_value=0.5, max_value=2.5, value=1.70, step=0.01)
weight = st.slider("Wählen Sie Ihr Gewicht (kg)", min_value=30.0, max_value=200.0, value=70.0, step=0.5)

bmi = calculate_bmi(weight, height)

if bmi < 18.5:
    category = "Untergewicht"
elif 18.5 <= bmi < 24.9:
    category = "Normalgewicht"
elif 25 <= bmi < 29.9:
    category = "Übergewicht"
else:
    category = "Adipositas"

st.write(f"Ihr BMI ist: **{bmi:.1f}**")
st.write(f"Berechnet am: {datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
st.write(f"Kategorie: **{category}**")

# Diagramm erstellen
fig, ax = plt.subplots()

categories = ["Untergewicht", "Normalgewicht", "Übergewicht", "Adipositas"]
values = [18.5, 24.9, 29.9, 40]  # Maximalwerte jeder Kategorie
colors = ['blue', 'green', 'orange', 'red']

# Balkendiagramm erstellen
y_pos = np.arange(len(categories))
ax.barh(y_pos, values, color=colors, height=0.5, alpha=0.6)

# Aktuellen BMI als Linie einzeichnen
ax.axvline(x=bmi, color='black', linestyle='--', label=f'Ihr BMI: {bmi:.1f}')

# Labels setzen
ax.set_yticks(y_pos)
ax.set_yticklabels(categories)
ax.set_xlabel("BMI-Wert")
ax.set_title("BMI-Kategorien")
ax.legend()
plt.tight_layout()

# Diagramm in Streamlit anzeigen
st.pyplot(fig)
