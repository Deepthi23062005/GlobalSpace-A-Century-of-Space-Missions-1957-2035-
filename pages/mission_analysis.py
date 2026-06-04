import streamlit as st
import plotly.express as px
from utils.data_loader import load_data

df = load_data()

st.title("Mission Analysis")

mission_year = (
    df.groupby("Launch_Year")
    .size()
    .reset_index(name="Missions")
)

fig = px.line(
    mission_year,
    x="Launch_Year",
    y="Missions",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)
