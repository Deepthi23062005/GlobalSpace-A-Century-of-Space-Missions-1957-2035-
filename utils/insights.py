def generate_insights(df):

    insights = []

    insights.append(
        f"Total Missions: {len(df)}"
    )

    insights.append(
        f"Total Agencies: {df['Agency'].nunique()}"
    )

    insights.append(
        f"Countries: {df['Country_Region'].nunique()}"
    )

    return insights
