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

data_df = st.session_state['data_df']
if data_df.empty:
    st.info('Keine BMI Daten vorhanden. Berechnen Sie Ihren BMI auf der Startseite.')
    st.stop()

# Weight over time
st.line_chart(data=data_df.set_index('timestamp')['weight'], use_container_width=True)
st.caption('Gewicht über Zeit (kg)')

# Height over time 
st.line_chart(data=data_df.set_index('timestamp')['height'], use_container_width=True)
st.caption('Grösse über Zeit (m)')

# BMI over time
st.line_chart(data=data_df.set_index('timestamp')['bmi'], use_container_width=True)
st.caption('BMI über Zeit')

# Button to navigate to the tips and tricks page
st.page_link("pages/4_Tipps&Tricks.py", label="➡️ Zu Tipps & Tricks", icon="💡")
