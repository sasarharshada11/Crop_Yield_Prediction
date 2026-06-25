import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# ==============================
# PAGE CONFIG
# ==============================

st.set_page_config(
    page_title="Crop Yield Prediction",
    page_icon="🌾",
    layout="wide"
)

# ==============================
# CUSTOM CSS
# ==============================

st.markdown("""
<style>

.stApp{
background: linear-gradient(135deg,#E8F5E9,#FFF8E1,#E3F2FD);
}

.main-title{
text-align:center;
font-size:50px;
font-weight:bold;
color:#1B5E20;
}

.sub-title{
text-align:center;
font-size:20px;
color:#2E7D32;
margin-bottom:20px;
}

.result-box{
background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 4px 12px rgba(0,0,0,0.15);
text-align:center;
}

</style>
""", unsafe_allow_html=True)

# ==============================
# LOAD MODEL
# ==============================

model = joblib.load("crop_yield_model.pkl")

# ==============================
# HEADER
# ==============================

st.markdown("""
<div class="main-title">
🌾 Crop Yield Prediction System
</div>

<div class="sub-title">
Smart Agriculture Analytics Dashboard
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# ==============================
# INPUT SECTION
# ==============================

col1, col2 = st.columns(2)

with col1:

    crop = st.selectbox(
        "Crop",
        ["Rice", "Wheat", "Maize", "Sugarcane", "Potato", "Tomato"]
    )

    variety = st.selectbox(
        "Variety",
        [
            "Basmati","Jasmine","Arborio",
            "Soft Red","Hard Red","Durum",
            "Sweet","Dent","Flint",
            "Co 0238","Co 86032","Co 99004",
            "Russet","Red","Yukon Gold",
            "Roma","Cherry","Beefsteak"
        ]
    )

    region = st.selectbox(
        "Region",
        [
            "Maharashtra","Punjab","Haryana","Bihar",
            "Karnataka","West Bengal",
            "Andhra Pradesh","Tamil Nadu",
            "Madhya Pradesh","Uttar Pradesh"
        ]
    )

    season = st.selectbox(
        "Season",
        ["Kharif","Rabi","Zaid"]
    )

    soil_type = st.selectbox(
        "Soil Type",
        ["Loamy","Clay","Sandy","Silt","Peaty","Saline"]
    )

with col2:

    nitrogen = st.slider("Nitrogen",0.0,150.0,75.0)
    phosphorus = st.slider("Phosphorus",0.0,100.0,50.0)
    potassium = st.slider("Potassium",0.0,100.0,50.0)
    temperature = st.slider("Temperature (°C)",10.0,45.0,25.0)
    humidity = st.slider("Humidity (%)",30.0,100.0,70.0)
    ph_value = st.slider("pH Value",4.0,9.0,6.5)
    rainfall = st.slider("Rainfall (mm)",20.0,400.0,200.0)

# ==============================
# PREDICTION
# ==============================

if st.button("🚀 Predict Yield"):

    input_df = pd.DataFrame({
        "Crop": [crop],
        "Variety": [variety],
        "Region": [region],
        "Season": [season],
        "Soil_Type": [soil_type],
        "Nitrogen": [nitrogen],
        "Phosphorus": [phosphorus],
        "Potassium": [potassium],
        "Temperature": [temperature],
        "Humidity": [humidity],
        "pH_Value": [ph_value],
        "Rainfall": [rainfall]
    })

    prediction = model.predict(input_df)
    predicted_yield = prediction[0]

    st.markdown(f"""
    <div class="result-box">
    <h2>🌾 Predicted Yield Result</h2>
    <h1>{predicted_yield:,.2f} Kg/Hectare</h1>
    </div>
    """, unsafe_allow_html=True)

    st.subheader("💡 Smart Recommendation")

    if predicted_yield >= 7000:
        st.success("""
        ✅ Excellent Yield Expected

        • Maintain current fertilizer schedule

        • Continue proper irrigation

        • Monitor pests regularly

        • Harvest at optimum maturity
        """)

    elif predicted_yield >= 5000:
        st.warning("""
        ⚠ Moderate Yield Expected

        • Improve nutrient management

        • Apply organic manure

        • Monitor irrigation carefully
        """)

    else:
        st.error("""
        ❌ Low Yield Expected

        • Conduct soil testing

        • Improve irrigation

        • Use recommended fertilizers

        • Select suitable crop variety
        """)

# ==============================
# CHARTS
# ==============================

st.markdown("---")
st.subheader("📊 Agriculture Analytics")

crop_df = pd.DataFrame({
    "Crop":["Rice","Wheat","Maize","Sugarcane","Potato","Tomato"],
    "Count":[120,95,80,60,75,90]
})

fig1 = px.pie(
    crop_df,
    names="Crop",
    values="Count",
    title="🌾 Crop Distribution"
)

st.plotly_chart(fig1, use_container_width=True)

season_df = pd.DataFrame({
    "Season":["Kharif","Rabi","Zaid"],
    "Yield":[6500,7200,5800]
})

fig2 = px.bar(
    season_df,
    x="Season",
    y="Yield",
    title="☁ Average Yield by Season"
)

st.plotly_chart(fig2, use_container_width=True)

region_df = pd.DataFrame({
    "Region":["Maharashtra","Punjab","Haryana","Bihar","Karnataka"],
    "Yield":[7100,7600,6900,6200,6700]
})

fig3 = px.bar(
    region_df,
    x="Region",
    y="Yield",
    title="📍 Average Yield by Region"
)

st.plotly_chart(fig3, use_container_width=True)

# ==============================
# FOOTER
# ==============================

st.markdown("---")
st.caption("🌾 Crop Yield Prediction using Machine Learning")