import streamlit as st
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_App_DB")  # switch drive 

# initialize the login manager
login_manager = LoginManager(data_manager)
login_manager.login_register()  # open login/register page

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
    )

st.title("Meine erste Streamlit App")

# !! WICHTIG: Eure Emails müssen in der App erscheinen!!

# Streamlit über den Text unten direkt in die App - cool!
("""
Diese App wurde von folgenden Personen entwickelt:
- Aylin Ago (agoayl01@students.zhaw.ch)
- Genta Arifi (arifigen@students.zhaw.ch)

Diese App ist das leere Gerüst für die App-Entwicklung im Modul Informatik 2 (BMLD/ZHAW)

Autorinnen: Aylin Ago (agoayl01@students.zhaw.ch) und Genta Arifi (arifigen@students.zhaw.ch)""")

st.title("🏠 Willkommen zur genayl App!")

st.write("Klicken Sie auf den Button unten, um zum BMI-Rechner zu gelangen.")

# Button to navigate to BMI calculator
st.page_link("pages/1_Rechner.py", label="➡️ Zum BMI-Rechner", icon="📊")

# Display saved BMI data
st.title("📊 Gespeicherte BMI-Daten")

if 'data_df' in st.session_state and not st.session_state['data_df'].empty:
    st.dataframe(st.session_state['data_df'])
else:
    st.write("Noch keine Daten vorhanden.")
