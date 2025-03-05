import streamlit as st
import datetime
import pytz  # Falls Zeitzone benötigt wird

def calculate_bmi(height, weight, timezone='Europe/Zurich'):
    """
    Berechnet den BMI und gibt eine strukturierte Antwort zurück.

    Args:
        height (float): Körpergröße in Metern.
        weight (float): Gewicht in Kilogramm.
        timezone (str): Zeitzone für die Zeitstempelanzeige.

    Returns:
        dict: Ein Dictionary mit Eingaben, berechnetem BMI, Kategorie und Zeitstempel.
    """
    if height <= 0 or weight <= 0:
        st.error("Größe und Gewicht müssen positive Werte sein.")
        return None

    bmi = weight / (height ** 2)

    # Bestimme die BMI-Kategorie
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

    # Zeitstempel mit richtiger Zeitzone
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

# 🌟 Streamlit UI
st.title("💪 BMI Rechner")

# Eingaben von Nutzer
height = st.slider("Größe auswählen (m)", min_value=0.5, max_value=2.5, value=1.70, step=0.01)
weight = st.slider("Gewicht auswählen (kg)", min_value=30.0, max_value=200.0, value=70.0, step=0.5)

# BMI Berechnung ausführen
result = calculate_bmi(height, weight)

if result:
    st.markdown(f"""
    ### 📝 Ergebnisse:
    - **Größe:** {result['height']} m  
    - **Gewicht:** {result['weight']} kg  
    - **BMI:** <span style='color:{result["color"]}; font-weight:bold;'>{result['bmi']}</span>  
    - **Kategorie:** {result['category']}  
    - 🕒 **Berechnet am:** {result['timestamp']}
    """, unsafe_allow_html=True)

    # Optionale BMI-Interpretation
    st.info("💡 Ein gesunder BMI liegt zwischen 18.5 und 24.9.")




