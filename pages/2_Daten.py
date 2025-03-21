# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

import streamlit as st
import pandas as pd
from utils.data_manager import DataManager

# initialize the data manager
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="BMLD_App_DB")  # switch drive 

# load the data from the persistent storage into the session state
data_manager.load_user_data(
    session_state_key='data_df', 
    file_name='data.csv', 
    initial_value = pd.DataFrame(), 
    parse_dates = ['timestamp']
)

st.title("📊 Gespeicherte BMI-Daten")

# Display saved BMI data
if 'data_df' in st.session_state and not st.session_state['data_df'].empty:
    st.dataframe(st.session_state['data_df'])
else:
    st.write("Noch keine Daten vorhanden.")

# Button to save current BMI data
if st.button("Aktuelle BMI-Daten speichern"):
    if 'current_bmi_data' in st.session_state:
        data_manager.append_record(session_state_key='data_df', record_dict=st.session_state['current_bmi_data'])
        st.success("Daten erfolgreich gespeichert!")
    else:
        st.error("Keine aktuellen BMI-Daten vorhanden.")

# Button to navigate to the graphics page
if st.button("Zur Grafikseite gehen"):
    st.experimental_set_query_params(page="3_Grafik")
