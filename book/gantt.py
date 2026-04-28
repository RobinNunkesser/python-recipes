import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Task="AI A", Start='2005-01-01', Finish='2010-09-30', Fachgebiet="Artificial Intelligence"),
    dict(Task="AI B", Start='2019-07-01', Finish='2025-06-16', Fachgebiet="Artificial Intelligence"),
    dict(Task="SE A", Start='2009-09-01', Finish='2025-06-16', Fachgebiet="Software Engineering"),
    dict(Task="Job C", Start='2010-10-01', Finish='2024-11-08', Fachgebiet="Mobile Software Engineering")
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Fachgebiet", color="Fachgebiet", template="plotly_dark")
fig.update_layout(showlegend=False)
fig.write_image(f"/Users/nunkesser/repos/work/images/denomination/timeline.svg", width=650, height=400, scale=1)
