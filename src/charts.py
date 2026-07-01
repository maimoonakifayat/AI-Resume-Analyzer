import plotly.express as px


def create_skill_chart(matched, missing):

    labels = ["Matched Skills", "Missing Skills"]

    values = [len(matched), len(missing)]

    fig = px.pie(
        names=labels,
        values=values,
        title="Skill Match Analysis"
    )

    return fig