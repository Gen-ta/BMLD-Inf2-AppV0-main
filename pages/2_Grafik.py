import streamlit as st
import datetime
import pytz  
import matplotlib.pyplot as plt
import pandas as pd

from utils.login_manager import LoginManager
from utils.data_manager import DataManager

LoginManager().go_to_login('Start.py') 

def calculate_bmi(height, weight, timezone='Europe/Zurich'):
    if height <= 0 or weight <= 0:
        st.error("Grösse und Gewicht müssen positive Werte sein.")
        return None

    bmi = weight / (height ** 2)

    if bmi < 18.5:
        category = "🟦 Untergewicht"
        color = "blue"
    elif bmi < 25:
        category = "🟩 Normalgewicht"
        color = "green"
    elif bmi < 30:
        category = "🟧 Übergewicht"
        color = "orange"
    else:
        category = "🟥 Adipositas"
        color = "red"

    tz = pytz.timezone(timezone)
    now = datetime.datetime.now(tz).strftime('%d.%m.%Y %H:%M:%S')

    return {
        "timestamp": now,
        "height": height,
        "weight": weight,
        "bmi": round(bmi, 1),
        "category": category,
        "color": color
    }

st.title("💪 BMI Rechner")

height = st.slider("Grösse auswählen (m)", min_value=0.5, max_value=2.5, value=1.70, step=0.01)
weight = st.slider("Gewicht auswählen (kg)", min_value=30.0, max_value=200.0, value=70.0, step=0.5)

result = calculate_bmi(height, weight)

if result:
    data_manager = DataManager()
    data_manager.append_record(session_state_key='data_df', record_dict=result)

    st.markdown(f"""
    ### 📝 Ergebnisse:
    - **Grösse:** {result['height']} m  
    - **Gewicht:** {result['weight']} kg  
    - **BMI:** <span style='color:{result["color"]}; font-weight:bold;'>{result['bmi']}</span>  
    - **Kategorie:** {result['category']}  
    - 🕒 **Berechnet am:** {result['timestamp']}
    """, unsafe_allow_html=True)

    st.info("💡 Ein gesunder BMI liegt zwischen 18.5 und 24.9.")

    # --- Load saved data ---
    data_df = data_manager.get_records(session_state_key='data_df')

    if data_df is not None and not data_df.empty:
        data_df['timestamp'] = pd.to_datetime(data_df['timestamp'], format='%d.%m.%Y %H:%M:%S')
        data_df = data_df.sort_values(by='timestamp')
        
        # --- Plotting the BMI history ---
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.plot(data_df['timestamp'], data_df['bmi'], marker='o', linestyle='-', label='BMI Verlauf')
        ax.axhline(18.5, color='blue', linestyle='dashed', label='Untergewicht')
        ax.axhline(25, color='green', linestyle='dashed', label='Normalgewicht')
        ax.axhline(30, color='orange', linestyle='dashed', label='Übergewicht')
        ax.axhline(35, color='red', linestyle='dashed', label='Adipositas')
        
        ax.set_xlabel('Datum')
        ax.set_ylabel('BMI')
        ax.set_title('BMI Verlauf über die Zeit')
        ax.legend()
        ax.grid()
        plt.xticks(rotation=45)
        
        st.pyplot(fig)
