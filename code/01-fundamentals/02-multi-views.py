from trame.app import get_server
from trame.widgets import html, client
from trame.ui.html import DivLayout

# Trame setup -----------------------------------------------------------------

server = get_server()

# View ------------------------------------------------------------------------

# Main view
with DivLayout(server):  # template_name="main"
    html.Div("Main View a={{a}} b={{b}}")
    client.ServerTemplate(name="view_a")
    client.ServerTemplate(name="view_b")

# view_a
with DivLayout(server, template_name="view_a"):
    html.Div("View a={{a}}")
    html.Input(
        type="range",
        min=0,
        max=100,
        step=1,
        v_model=("a", 0),  # Set a default value of 0 to variable "a"
    )

# view_b
with DivLayout(server, template_name="view_b"):
    html.Div("View b={{b}}")
    html.Input(
        type="range",
        min=0,
        max=50,
        step=2,
        v_model=("b", 2),  # Set a default value of 0 to variable "b"
    )

# Start Server ----------------------------------------------------------------

server.start()
