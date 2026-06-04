import streamlit as st

st.set_page_config(
    page_title="🚀 Space Mission Analytics",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Space Mission Analytics Dashboard")

st.markdown("""
Welcome to the Space Mission Analytics Platform.
Use the sidebar to navigate through dashboards.
""")
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/Space_Missions_Dataset.csv")

st.title("🚀 Space Mission Analytics")

st.metric("Total Missions", len(df))

fig = px.pie(df, names="Status")
st.plotly_chart(fig)
