#!/usr/bin/env python
# -*- coding: utf-8 -*-

from trame.app import get_server
from trame.ui.html import DivLayout
from trame.widgets import matplotlib as mplw

import numpy as np
import matplotlib.pyplot as plt


def setup_matplotlib():
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)

    return fig


class ChartApp:
    def __init__(self, server=None):
        self.server = get_server(server)
        self.figure = setup_matplotlib()

        with DivLayout(self.server):
            mplw.Figure(self.figure)


if __name__ == "__main__":
    app = ChartApp()
    app.server.start()
