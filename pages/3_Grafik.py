# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

import streamlit as st
import pandas as pd
import altair as alt
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

st.title("📈 BMI-Daten Grafik")

# Display BMI data graph
if 'data_df' in st.session_state and not st.session_state['data_df'].empty:
    df = st.session_state['data_df']
    
    color_scale = alt.Scale(
        domain=['🟦 Untergewicht', '🟩 Normalgewicht', '🟧 Übergewicht', '🟥 Adipositas'],
        range=['blue', 'green', 'orange', 'red']
    )
    
    y_min = df['bmi'].min() - 5
    y_max = df['bmi'].max() + 5
    
    chart = alt.Chart(df).mark_point().encode(
        x=alt.X('timestamp:T', title='Zeitstempel'),
        y=alt.Y('bmi:Q', title='BMI-Wert', scale=alt.Scale(domain=[y_min, y_max])),
        color=alt.Color('category:N', title='Kategorie', scale=color_scale),
        tooltip=['timestamp', 'height', 'weight', 'bmi', 'category']
    ).properties(
        title='Verlauf der BMI-Daten'
    )
    
    st.altair_chart(chart, use_container_width=True)
else:
    st.write("Noch keine Daten vorhanden.")
