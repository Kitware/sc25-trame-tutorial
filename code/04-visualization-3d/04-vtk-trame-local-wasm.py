#!/usr/bin/env python
# -*- coding: utf-8 -*-

from trame.app import get_server
from trame.ui.vuetify3 import SinglePageLayout
from trame.widgets import vuetify3 as v3, vtklocal
from trame.decorators import TrameApp, change

from vtkmodules.vtkInteractionStyle import vtkInteractorStyleSwitch  # noqa
import vtkmodules.vtkRenderingOpenGL2  # noqa

from vtkmodules.vtkCommonColor import vtkNamedColors
from vtkmodules.vtkCommonComputationalGeometry import vtkParametricKuen
from vtkmodules.vtkCommonCore import vtkMath
from vtkmodules.vtkFiltersSources import vtkParametricFunctionSource
from vtkmodules.vtkRenderingCore import (
    vtkActor,
    vtkPolyDataMapper,
    vtkProperty,
    vtkRenderWindow,
    vtkRenderWindowInteractor,
    vtkRenderer,
)


def setup_vtk():
    colors = vtkNamedColors()

    colors.SetColor("BkgColor", [26, 51, 102, 255])

    surface = vtkParametricKuen()
    source = vtkParametricFunctionSource()

    renderer = vtkRenderer()
    mapper = vtkPolyDataMapper()
    actor = vtkActor()

    backProperty = vtkProperty()
    backProperty.SetColor(colors.GetColor3d("Tomato"))

    # Create a parametric function source, renderer, mapper, and actor
    source.SetParametricFunction(surface)

    mapper.SetInputConnection(source.GetOutputPort())

    actor.SetMapper(mapper)
    actor.SetBackfaceProperty(backProperty)
    actor.GetProperty().SetDiffuseColor(colors.GetColor3d("Banana"))
    actor.GetProperty().SetSpecular(0.5)
    actor.GetProperty().SetSpecularPower(20)

    renderWindow = vtkRenderWindow()
    renderWindow.AddRenderer(renderer)

    renderer.AddActor(actor)
    renderer.SetBackground(colors.GetColor3d("BkgColor"))
    renderer.ResetCamera()
    renderer.GetActiveCamera().Azimuth(30)
    renderer.GetActiveCamera().Elevation(-30)
    renderer.GetActiveCamera().Zoom(0.9)
    renderer.ResetCameraClippingRange()

    surface.SetMinimumU(-4.5)
    surface.SetMaximumU(4.5)
    surface.SetMinimumV(0.05)
    surface.SetMaximumV(vtkMath.Pi() - 0.05)

    renderer.ResetCamera()
    renderer.GetActiveCamera().Azimuth(30)
    renderer.GetActiveCamera().Elevation(-30)
    renderer.GetActiveCamera().Zoom(0.9)
    renderer.ResetCameraClippingRange()
    renderWindow.Render()

    interactor = vtkRenderWindowInteractor()
    interactor.SetRenderWindow(renderWindow)
    interactor.GetInteractorStyle().SetCurrentStyleToTrackballCamera()

    return renderWindow, surface


@TrameApp()
class VtkApp:
    def __init__(self, server=None):
        self.server = get_server(server)
        self.render_window, self.source = setup_vtk()
        self._build_ui()

    @property
    def ctrl(self):
        return self.server.controller

    @change("u_range", "v_range")
    def on_change(self, u_range, v_range, **_):
        self.source.SetMinimumU(u_range[0])
        self.source.SetMaximumU(u_range[1])
        self.source.SetMinimumV(v_range[0])
        self.source.SetMaximumV(v_range[1])
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
                    v_model=("v_range", [0.05, vtkMath.Pi() - 0.05]),
                    min=0.05,
                    max=vtkMath.Pi() - 0.05,
                    step=0.05,
                    density="compact",
                    hide_details=True,
                    classes="mx-4",
                )
            with layout.content:
                with v3.VContainer(fluid=True, classes="ma-0 pa-0 h-100"):
                    with vtklocal.LocalView(self.render_window, throttle_rate=20) as view:
                        self.ctrl.view_update = view.update_throttle
                        self.ctrl.view_reset_camera = view.reset_camera


if __name__ == "__main__":
    app = VtkApp()
    app.server.start()
