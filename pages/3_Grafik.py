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

# Generate normal BMI line data
height_range = pd.Series([i/100 for i in range(150, 201)])  # Heights from 1.50m to 2.00m
normal_bmi_weight = 22 * (height_range ** 2)  # Normal BMI is 22

normal_bmi_df = pd.DataFrame({
    'height': height_range,
    'weight': normal_bmi_weight,
    'category': ['Normalgewicht'] * len(height_range)
})

# Display BMI data graph
if 'data_df' in st.session_state and not st.session_state['data_df'].empty:
    df = st.session_state['data_df']
    
    # Combine normal BMI line data with user data
    combined_df = pd.concat([normal_bmi_df, df])
    
    chart = alt.Chart(combined_df).mark_point().encode(
        x=alt.X('height:Q', title='Grösse (m)'),
        y=alt.Y('weight:Q', title='Gewicht (kg)'),
        color=alt.Color('category:N', title='Kategorie'),
        tooltip=['timestamp', 'height', 'weight', 'bmi', 'category']
    ).properties(
        title='Grösse vs. Gewicht mit BMI-Kategorien'
    )
    
    line = alt.Chart(normal_bmi_df).mark_line(color='green').encode(
        x='height:Q',
        y='weight:Q'
    )
    
    st.altair_chart(line + chart, use_container_width=True)
else:
    st.write("Noch keine Daten vorhanden.")
