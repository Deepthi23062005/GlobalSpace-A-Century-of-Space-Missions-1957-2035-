import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

st.title("Cost Analysis")

fig = px.histogram(
    df,
    x="Cost_USD_Million",
    nbins=30
)

st.plotly_chart(fig, use_container_width=True)
