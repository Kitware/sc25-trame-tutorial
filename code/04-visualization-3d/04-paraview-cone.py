from paraview import simple

from trame.app import get_server
from trame.ui.vuetify3 import SinglePageLayout
from trame.widgets import vuetify3 as v3, paraview as pvw
from trame.decorators import TrameApp, change


@TrameApp()
class PVApp:
    def __init__(self, server=None):
        self.server = get_server(server)

        # ParaView
        self.cone = simple.Cone()
        self.representation = simple.Show()
        self.view = simple.Render()

        # GUI
        self._build_ui()

    @property
    def ctrl(self):
        return self.server.controller

    @change("resolution")
    def on_change(self, resolution, **_):
        self.cone.Resolution = resolution
        self.ctrl.view_update()

    def _build_ui(self):
        with SinglePageLayout(self.server, full_height=True) as layout:
            with layout.toolbar as tb:
                tb.density = "compact"
                v3.VSpacer()
                v3.VSlider(
                    v_model=("resolution", 6),
                    min=3,
                    max=60,
                    step=1,
                    density="compact",
                    hide_details=True,
                    classes="mx-4",
                )
                v3.VBtn(
                    icon="mdi-crop-free",
                    click=self.ctrl.view_reset_camera,
                )

            with layout.content:
                with v3.VContainer(fluid=True, classes="ma-0 pa-0 h-100"):
                    with pvw.VtkRemoteView(self.view, interactive_ratio=1) as view:
                        self.ctrl.view_update = view.update
                        self.ctrl.view_reset_camera = view.reset_camera


if __name__ == "__main__":
    app = PVApp()
    app.server.start()
