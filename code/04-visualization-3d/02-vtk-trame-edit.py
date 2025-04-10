#!/usr/bin/env python
# -*- coding: utf-8 -*-

from trame.app import get_server
from trame.ui.vuetify3 import SinglePageLayout
from trame.widgets import vuetify3 as v3, vtk as vtkw
from trame.decorators import TrameApp, change

from vtkmodules.vtkInteractionStyle import vtkInteractorStyleSwitch  # noqa
import vtkmodules.vtkRenderingOpenGL2  # noqa

from vtkmodules.vtkRenderingCore import (
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
)


def setup_vtk():
    renderer = vtkRenderer()

    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)

    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)
    interactor.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

    return renderWindow


@TrameApp()
class VtkApp:
    def __init__(self, server=None):
        self.server = get_server(server)
        self.render_window = setup_vtk()
        self._build_ui()

    @property
    def ctrl(self):
        return self.server.controller

    @change("u_range", "v_range")
    def on_change(self, u_range, v_range, **_):
        # make method call to vtk object
        self.ctrl.view_update()

    def _build_ui(self):
        with SinglePageLayout(self.server, full_height=True) as layout:
            with layout.toolbar.clear() as tb:
                tb.density = "compact"
                v3.VRangeSlider(
                    label="U",
                    v_model=("u_range", [-4.5, 4.5]),
                    min=-4.5,
                    max=4.5,
                    step=0.1,
                    density="compact",
                    hide_details=True,
                    classes="mx-4",
                )
                v3.VRangeSlider(
                    label="V",
                    v_model=("v_range", [0.05, 3.14159 - 0.05]),
                    min=0.05,
                    max=3.14159 - 0.05,
                    step=0.05,
                    density="compact",
                    hide_details=True,
                    classes="mx-4",
                )

            with layout.content:
                with v3.VContainer(fluid=True, classes="ma-0 pa-0 h-100"):
                    with vtkw.VtkRemoteView(
                        self.render_window, interactive_ratio=1
                    ) as view:
                        self.ctrl.view_update = view.update
                        self.ctrl.view_reset_camera = view.reset_camera


if __name__ == "__main__":
    app = VtkApp()
    app.server.start()
