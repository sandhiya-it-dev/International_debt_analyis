import plotly.express as px


def bar_chart(df, x, y, title):
    fig = px.bar(
        df,
        x=x,
        y=y,
        title=title,
        text_auto=".2s"
    )

    fig.update_layout(
        template="plotly_white",
        height=500,
        xaxis_title="",
        yaxis_title=""
    )

    return fig