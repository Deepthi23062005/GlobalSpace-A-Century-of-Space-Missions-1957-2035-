import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import os

# Debug information
st.write("Current folder:", os.getcwd())

# Page configuration
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

# Get path to CSV file
BASE_DIR = Path(__file__).resolve().parent
CSV_FILE = BASE_DIR.parent / "data" / "space_missions_dataset.csv"

# Show path for debugging
st.write("Looking for file:", CSV_FILE)

# Load data
try:
    df = pd.read_csv(CSV_FILE)

    st.title("🚀 Space Mission Analytics")

    st.metric("Total Missions", len(df))

    # Check column exists before plotting
    if "Status" in df.columns:
        fig = px.pie(df, names="Status", title="Mission Status Distribution")
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.error(f"'Status' column not found. Available columns: {list(df.columns)}")

except FileNotFoundError:
    st.error(f"CSV file not found at: {CSV_FILE}")
except Exception as e:
    st.error(f"Error loading data: {e}")
