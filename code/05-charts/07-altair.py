# https://altair-viz.github.io/getting_started/overview.html

# import altair with an abbreviated alias
import altair as alt

# load a sample dataset as a pandas DataFrame
from vega_datasets import data

cars = data.cars()

# make the chart
chart = (
    alt.Chart(cars)
    .mark_point()
    .encode(
        x="Horsepower",
        y="Miles_per_Gallon",
        color="Origin",
    )
    .interactive()
)

chart.save("chart-altair.html")
