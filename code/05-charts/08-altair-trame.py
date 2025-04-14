# import altair with an abbreviated alias
import altair as alt

# load a sample dataset as a pandas DataFrame
from vega_datasets import data

from trame.app import get_server
from trame.ui.html import DivLayout
from trame.widgets import vega


def create_figure():
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

    return chart


class ChartApp:
    def __init__(self, server=None):
        self.server = get_server(server)
        self.figure = create_figure()

        with DivLayout(self.server):
            vega.Figure(self.figure)


if __name__ == "__main__":
    app = ChartApp()
    app.server.start()
