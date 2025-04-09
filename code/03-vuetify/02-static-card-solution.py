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
                with v3.VCard(elevation=4, rounded="lg"):
                    with html.Div(classes="pa-4"):
                        html.Div(
                            "{{ card.title }}",
                            classes="ps-4 text-caption text-medium-emphasis",
                        )
                        with v3.VCardTitle(classes="pt-0 mt-n1 d-flex align-center"):
                            html.Div("{{ card.value }}", classes="me-2")
                            with v3.VChip(
                                label=True,
                                color=("card.color",),
                                prepend_icon=(
                                    "`mdi-arrow-${card.change.startsWith('-') ? 'down' : 'up'}`",
                                ),
                                size="x-small",
                            ):
                                with html.Template(raw_attrs=["#prepend"]):
                                    v3.VIcon(size=10)
                                html.Span("{{ card.change }}", classes="text-caption")

                    v3.VSparkline(
                        color=("card.color",),
                        fill=True,
                        gradient=(
                            "[`${card.color}E6`, `${card.color}33`, `${card.color}00`]",
                        ),
                        height=50,
                        line_width=1,
                        min=0,
                        model_value=("card.data",),
                        padding=0,
                        smooth=True,
                    )


# Start Server ----------------------------------------------------------------
server.start()
