# uv pip install trame-vuetify

import random

from trame.app import get_server
from trame.ui.vuetify3 import VAppLayout
from trame.widgets import html, vuetify3 as v3

# Trame setup -----------------------------------------------------------------
server = get_server()

# ViewModel -------------------------------------------------------------------
state = server.state

TITLES = ["Bandwidth Used", "Requests Served"]
VALUES = ["1.01 TB", "7.96 M", "1.04 k", "0.54 GB"]
CHANGES = ["-20.12%", "-7.73%", "+1.03%", "+50.34%"]
COLORS = ["#da5656", "#2fc584", "#2196F3", "#03A9F4", "#1DE9B6", "#FFB74D"]


def generate_data():
    return [random.randint(0, 10) for i in range(15)]


def generate_card():
    return {
        "title": random.choice(TITLES),
        "value": random.choice(VALUES),
        "change": random.choice(CHANGES),
        "color": random.choice(COLORS),
        "data": generate_data(),
    }


@state.change("number_of_cards")
def update_cards(number_of_cards, **_):
    state.cards = [generate_card() for i in range(number_of_cards)]


# View ------------------------------------------------------------------------
with VAppLayout(server):
    with v3.VContainer():
        v3.VSlider(
            v_model=("number_of_cards", 3),
            min=1,
            max=12,
            step=1,
        )
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
