
import streamlit as st
import pandas as pd

st.set_page_config(page_title="NCC Peptide Pricing Calculator", layout="wide")

# NCC Branding
logo = "https://ncc.health/wp-content/uploads/2022/11/NCC-Logo-retina.png"
st.image(logo, width=220)
st.markdown("<h2 style='color:#006699;'>💉 NCC Peptide Formulation Pricing Calculator</h2>", unsafe_allow_html=True)

# Load peptide pricing from Excel
excel_file = "Peptide Pricing.xlsx"
df = pd.read_excel(excel_file)
price_lookup = dict(zip(df["Name"], df["Cost / gm (AUD)"]))

# Mode selection
mode = st.radio("Select Calculator Mode", ["Single Peptide", "Combo Peptide"], horizontal=True)

# Shared inputs
vial_volume_ml = st.number_input("Vial Volume (mL)", value=3.0, step=0.5)
number_of_vials = st.number_input("Number of Vials", value=25, step=1)
consumables_per_vial = st.number_input("Consumables Cost per Vial (AUD)", value=2.5)
sterile_lab_hours = st.number_input("Sterile Lab Time (Hours)", value=1.0, step=0.5)
lab_rate = st.number_input("Sterile Lab Hourly Rate (AUD)", value=200.0)

# Calculation logic
total_api_cost = 0

if mode == "Single Peptide":
    peptide_name = st.selectbox("Peptide Name", list(price_lookup.keys()))
    strength_per_vial_mg = st.number_input("Strength per Vial (mg)", value=6.0, step=0.5)
    price_per_gram = price_lookup.get(peptide_name, 0)
    st.number_input("AUD Price per Gram", value=price_per_gram, step=0.1, key="price_display", disabled=True)

    total_api_cost = (strength_per_vial_mg * number_of_vials / 1000) * price_per_gram

elif mode == "Combo Peptide":
    st.subheader("Peptide 1")
    peptide1 = st.selectbox("Peptide 1", list(price_lookup.keys()), key="p1")
    strength1 = st.number_input("Strength per Vial (mg)", value=3.0, key="s1")
    price1 = price_lookup.get(peptide1, 0)
    st.number_input("AUD Price per Gram", value=price1, step=0.1, key="pr1", disabled=True)

    st.subheader("Peptide 2")
    peptide2 = st.selectbox("Peptide 2", list(price_lookup.keys()), key="p2")
    strength2 = st.number_input("Strength per Vial (mg)", value=3.0, key="s2")
    price2 = price_lookup.get(peptide2, 0)
    st.number_input("AUD Price per Gram", value=price2, step=0.1, key="pr2", disabled=True)

    total_api_cost = ((strength1 * number_of_vials / 1000) * price1) + ((strength2 * number_of_vials / 1000) * price2)

# Continue shared calculations
total_consumables = number_of_vials * consumables_per_vial
total_lab_cost = sterile_lab_hours * lab_rate
total_batch_cost = total_api_cost + total_consumables + total_lab_cost
cost_per_vial = total_batch_cost / number_of_vials

# Pricing summary
st.markdown("### 💵 Pricing Summary")
retail_markup_percent = st.number_input("Retail Markup (%)", value=100)
retail_price_per_vial = cost_per_vial * (1 + retail_markup_percent / 100)

# Display breakdown
st.markdown("<h4 style='color:#006699;'>💰 Cost Breakdown</h4>", unsafe_allow_html=True)
st.success(f"**Total API Cost:** ${total_api_cost:.2f} AUD")
st.info(f"**Total Consumables:** ${total_consumables:.2f} AUD")
st.info(f"**Total Lab Cost:** ${total_lab_cost:.2f} AUD")
st.success(f"**Total Batch Cost:** ${total_batch_cost:.2f} AUD")
st.warning(f"**Cost per Vial:** ${cost_per_vial:.2f} AUD")
st.markdown(f"<h5 style='color:#006699;'>Retail Price per Vial: <strong>${retail_price_per_vial:.2f} AUD</strong></h5>", unsafe_allow_html=True)

st.markdown("---")
st.caption("Built for National Custom Compounding – June 2025")
