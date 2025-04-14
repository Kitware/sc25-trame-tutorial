#!/usr/bin/env python
# -*- coding: utf-8 -*-

from trame.app import get_server
from trame.ui.html import DivLayout
from trame.widgets import matplotlib as mplw, client
from trame.decorators import TrameApp, change

import numpy as np
import matplotlib.pyplot as plt

STYLE_NO_SIZE = "position: absolute; top: 0; left: 0; width: 100%; height: 100%;"


def setup_matplotlib():
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    return fig


@TrameApp()
class ChartApp:
    def __init__(self, server=None):
        self.server = get_server(server)
        self.figure = setup_matplotlib()

        with DivLayout(self.server) as layout:
            # Make it full screen
            client.Style("#app { height: 100vh; with: 100vw; } body {margin: 0}")
            layout.root.style = "height: 100%;"
            with client.SizeObserver("fig_size"):
                self.ctrl.update = mplw.Figure(self.figure, style=STYLE_NO_SIZE).update

    @property
    def ctrl(self):
        return self.server.controller

    @change("fig_size")
    def on_size(self, fig_size, **_):
        if fig_size is None:
            return

        dpi = fig_size.get("dpi")
        size = fig_size.get("size")

        width = size.get("width")
        height = size.get("height")

        # size in inch
        self.figure.set_figwidth(width / dpi)
        self.figure.set_figheight(height / dpi)

        self.ctrl.update(self.figure)


if __name__ == "__main__":
    app = ChartApp()
    app.server.start()
