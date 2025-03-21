import streamlit as st
import datetime
import pytz  

from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 

def calculate_bmi(height, weight, timezone='Europe/Zurich'):
    """
    Berechnet den BMI und gibt eine strukturierte Antwort zurück.

    Args:
        height (float): Körpergrösse in Metern.
        weight (float): Gewicht in Kilogramm.
        timezone (str): Zeitzone für die Zeitstempelanzeige.

    Returns:
        dict: Ein Dictionary mit Eingaben, berechnetem BMI, Kategorie und Zeitstempel.
    """
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
    # --- Save BMI data ---
    from utils.data_manager import DataManager
    DataManager().append_record(session_state_key='data_df', record_dict=result)
    
    st.markdown(f"""
    ### 📝 Ergebnisse:
    - **Grösse:** {result['height']} m  
    - **Gewicht:** {result['weight']} kg  
    - **BMI:** <span style='color:{result["color"]}; font-weight:bold;'>{result['bmi']}</span>  
    - **Kategorie:** {result['category']}  
    - 🕒 **Berechnet am:** {result['timestamp']}
    """, unsafe_allow_html=True)    

    
    st.info("💡 Ein gesunder BMI liegt zwischen 18.5 und 24.9.")
    
    if st.button("Daten speichern und zur Datenseite gehen"):
        st.session_state['current_bmi_data'] = result
        st.experimental_set_query_params(page="2_Daten")




