import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/Space_Missions_Dataset.csv")

st.title("Executive Dashboard")

col1,col2,col3 = st.columns(3)

col1.metric("Total Missions",len(df))
col2.metric("Agencies",df["Agency"].nunique())
col3.metric("Countries",df["Country_Region"].nunique())

fig = px.pie(
    df,
    names="Status",
    title="Mission Status"
)

st.plotly_chart(fig,use_container_width=True)
