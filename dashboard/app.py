import streamlit as st
import pandas as pd
import joblib
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Smart River Monitoring",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
/* Gradient background */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Glass cards */
.glass {
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 20px;
    margin: 10px;
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
}

/* Title */
.title {
    font-size: 40px;
    font-weight: bold;
    text-align: center;
    color: #00e5ff;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #cfd8dc;
    margin-bottom: 30px;
}

/* Alert styles */
.alert-red {
    background: #ff1744;
    padding: 15px;
    border-radius: 15px;
    font-weight: bold;
    text-align: center;
}

.alert-yellow {
    background: #ff9100;
    padding: 15px;
    border-radius: 15px;
    font-weight: bold;
    text-align: center;
}

.alert-green {
    background: #00c853;
    padding: 15px;
    border-radius: 15px;
    font-weight: bold;
    text-align: center;
}

/* Footer */
.footer {
    text-align: center;
    font-size: 14px;
    color: #b0bec5;
    margin-top: 30px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown('<div class="title">🌊 Smart River Monitoring System</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Real-Time AI • IoT • Environmental Protection</div>', unsafe_allow_html=True)

# ---------------- LOAD MODEL ----------------
model = joblib.load("model/flood_model.pkl")
placeholder = st.empty()

# Thresholds
FLOOD_LEVEL = 6.0
TURBIDITY_LIMIT = 70
PLASTIC_LIMIT = 0.6

# ---------------- REAL-TIME LOOP ----------------
while True:
    df = pd.read_csv("data/sensor_log.csv")
    latest = df.iloc[-1]

    water = latest["water_level"]
    turbidity = latest["turbidity"]
    plastic = latest["plastic_density"]

    X = [[water, turbidity, plastic]]
    flood_pred = model.predict(X)[0]

    with placeholder.container():
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
            <div class="glass">
                <h3>🌊 Water Level</h3>
                <h1>{water} m</h1>
            </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
            <div class="glass">
                <h3>🧪 Turbidity</h3>
                <h1>{turbidity} NTU</h1>
            </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
            <div class="glass">
                <h3>🗑️ Plastic Density</h3>
                <h1>{plastic}</h1>
            </div>
            """, unsafe_allow_html=True)

        # ALERTS
        if flood_pred == 1 or water > FLOOD_LEVEL:
            st.markdown('<div class="alert-red">🚨 FLOOD ALERT – Immediate Action Required</div>', unsafe_allow_html=True)
        elif turbidity > TURBIDITY_LIMIT:
            st.markdown('<div class="alert-yellow">⚠️ POLLUTION ALERT – High Turbidity Detected</div>', unsafe_allow_html=True)
        elif plastic > PLASTIC_LIMIT:
            st.markdown('<div class="alert-yellow">🗑️ PLASTIC WASTE ALERT – Cleanup Needed</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="alert-green">✅ RIVER STATUS NORMAL</div>', unsafe_allow_html=True)

        st.markdown("### 📈 Live Sensor Trends")
        st.line_chart(df[["water_level", "turbidity"]])

        st.markdown('<div class="footer">AI-Enabled Smart River Monitoring • Final Year Project</div>', unsafe_allow_html=True)

    time.sleep(1)
