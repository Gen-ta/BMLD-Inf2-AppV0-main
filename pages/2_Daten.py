# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  
# ====== End Login Block ======

import streamlit as st
import pandas as pd
from utils.data_manager import DataManager

st.title('📊 BMI Werte')

# --- Load saved data ---
data_manager = DataManager()
data_df = data_manager.get_records(session_state_key='data_df')

if data_df is None or not isinstance(data_df, pd.DataFrame) or data_df.empty:
    st.info('Keine BMI Daten vorhanden. Berechnen Sie Ihren BMI auf der Startseite.')
    st.stop()

# Sort dataframe by timestamp
data_df['timestamp'] = pd.to_datetime(data_df['timestamp'], format='%d.%m.%Y %H:%M:%S', errors='coerce')
data_df = data_df.dropna(subset=['timestamp'])
data_df = data_df.sort_values('timestamp', ascending=False)

# Display table
st.dataframe(data_df)
