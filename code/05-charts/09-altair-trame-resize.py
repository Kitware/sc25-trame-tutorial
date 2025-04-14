# import altair with an abbreviated alias
import altair as alt

# load a sample dataset as a pandas DataFrame
from vega_datasets import data

from trame.app import get_server
from trame.ui.html import DivLayout
from trame.widgets import vega, client


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
        .properties(
            width="container",
            height="container",
        )
        .interactive()
    )

    return chart


class ChartApp:
    def __init__(self, server=None):
        self.server = get_server(server)
        self.figure = create_figure()

        with DivLayout(self.server) as layout:
            client.Style("#app { height: 100vh; with: 100vw; } body {margin: 0}")
            layout.root.style = "height: 100%;"
            vega.Figure(self.figure, style="width: 100%;height: 100%;")


if __name__ == "__main__":
    app = ChartApp()
    app.server.start()
