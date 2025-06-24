
import streamlit as st
from PIL import Image

st.set_page_config(page_title="NCC Peptide Pricing Calculator", layout="wide")

# NCC Logo
logo = "https://ncc.health/wp-content/uploads/2022/11/NCC-Logo-retina.png"
st.image(logo, width=220)

st.markdown("<h2 style='color:#006699;'>💉 NCC Peptide Formulation Pricing Calculator</h2>", unsafe_allow_html=True)

# Input section
st.markdown("### 1. Peptide & Batch Details")

col1, col2, col3 = st.columns(3)
with col1:
    peptide_name = st.selectbox("Peptide Name", ["BPC-157", "TB500", "CJC-1295", "Ipamorelin"])
with col2:
    strength_per_vial_mg = st.number_input("Strength per Vial (mg)", value=6.0, step=0.5)
with col3:
    vial_volume_ml = st.number_input("Vial Volume (mL)", value=3.0, step=0.5)

col4, col5, col6 = st.columns(3)
with col4:
    price_per_gram = st.number_input("AUD Price per Gram", value=1198.5)
with col5:
    number_of_vials = st.number_input("Number of Vials", value=25, step=1)
with col6:
    consumables_per_vial = st.number_input("Consumables Cost per Vial (AUD)", value=2.5)

st.markdown("### 2. Sterile Lab Costs")
col7, col8 = st.columns(2)
with col7:
    sterile_lab_hours = st.number_input("Sterile Lab Time (Hours)", value=1.0, step=0.5)
with col8:
    lab_rate = st.number_input("Sterile Lab Hourly Rate (AUD)", value=200.0)

# Calculation section
total_api_cost = (strength_per_vial_mg * number_of_vials / 1000) * price_per_gram
total_consumables = number_of_vials * consumables_per_vial
total_lab_cost = sterile_lab_hours * lab_rate
total_batch_cost = total_api_cost + total_consumables + total_lab_cost
cost_per_vial = total_batch_cost / number_of_vials

st.markdown("### 3. Pricing Summary")
col9, col10 = st.columns(2)
with col9:
    retail_markup_percent = st.number_input("Retail Markup (%)", value=100)
with col10:
    retail_price_per_vial = cost_per_vial * (1 + retail_markup_percent / 100)

# Display results
st.markdown("<h4 style='color:#006699;'>💰 Cost Breakdown</h4>", unsafe_allow_html=True)
st.success(f"**Total API Cost:** ${total_api_cost:.2f} AUD")
st.info(f"**Total Consumables:** ${total_consumables:.2f} AUD")
st.info(f"**Total Lab Cost:** ${total_lab_cost:.2f} AUD")
st.success(f"**Total Batch Cost:** ${total_batch_cost:.2f} AUD")
st.warning(f"**Cost per Vial:** ${cost_per_vial:.2f} AUD")
st.markdown(f"<h5 style='color:#006699;'>Retail Price per Vial: <strong>${retail_price_per_vial:.2f} AUD</strong></h5>", unsafe_allow_html=True)

st.markdown("---")
st.caption("Built for National Custom Compounding – June 2025")
