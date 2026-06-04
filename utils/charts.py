import plotly.express as px

def mission_status_chart(df):
    fig = px.pie(
        df,
        names="Status",
        title="Mission Status Distribution"
    )
    return fig


def agency_chart(df):
    agency = (
        df.groupby("Agency")
        .size()
        .reset_index(name="Missions")
        .sort_values("Missions", ascending=False)
        .head(10)
    )

    fig = px.bar(
        agency,
        x="Agency",
        y="Missions",
        title="Top 10 Agencies"
    )

    return fig
