import streamlit as st
import pandas as pd

st.title("Meine erste Streamlit App")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
("""
SyntaxError: unterminated triple-quoted string literal (detected at line 16)
Diese App wurde von folgenden Personen entwickelt:
- Aylin Ago (agoayl01@students.zhaw.ch)
- Genta Arifi (arifigen@students.zhaw.ch)

Diese App ist das leere Gerüst für die App-Entwicklung im Modul Informatik 2 (BMLD/ZHAW)

Autorinnen: Aylin Ago (agoayl01@students.zhaw.ch) und Genta Arifi (arifigen@students.zhaw.ch)""")


import streamlit as st

st.title("🏠 Willkommen zur genayl App!")

st.write("Klicken Sie auf den Button unten, um zum BMI-Rechner zu gelangen.")


st.page_link("pages/Rechner.py", label="➡️ Zum BMI-Rechner", icon="📊")
