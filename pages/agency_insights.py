import streamlit as st
from utils.data_loader import load_data
from utils.charts import agency_chart

df = load_data()

st.title("Agency Insights")

st.plotly_chart(
    agency_chart(df),
    use_container_width=True
)
