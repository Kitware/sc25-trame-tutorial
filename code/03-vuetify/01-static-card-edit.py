# uv pip install trame-vuetify

from trame.app import get_server
from trame.ui.vuetify3 import VAppLayout
from trame.widgets import html, vuetify3 as v3

# Trame setup -----------------------------------------------------------------
server = get_server()

# ViewModel -------------------------------------------------------------------
state = server.state

state.cards = [
    {
        "title": "Bandwidth Used",
        "value": "1.01 TB",
        "change": "-20.12%",
        "color": "#da5656",
        "data": [5, 2, 5, 9, 5, 10, 3, 5, 3, 7, 1, 8, 2, 9, 6],
    },
    {
        "title": "Requests Served",
        "value": "7.96 M",
        "change": "-7.73%",
        "color": "#2fc584",
        "data": [1, 3, 8, 2, 9, 5, 10, 3, 5, 3, 7, 6, 8, 2, 9, 6],
    },
]

# View ------------------------------------------------------------------------
with VAppLayout(server):
    with v3.VContainer():
        with v3.VRow(dense=True):
            with v3.VCol(v_for="(card, i) in cards", key="i", cols=12, md=4):
                html.Pre("{{ JSON.stringify(card, null, 2) }}", classes="border-thin")
                # Use App.vue template content and convert it to Python


# Start Server ----------------------------------------------------------------
server.start()
