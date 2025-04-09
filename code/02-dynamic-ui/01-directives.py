from trame.app import get_server
from trame.widgets import html
from trame.ui.html import DivLayout

# Trame setup -----------------------------------------------------------------

server = get_server()

# ViewModel -------------------------------------------------------------------
state = server.state


# Reactivity
@state.change("a")
def update_b(a, **_):
    state.ul_li_list = [f"Item {i + 1}" for i in range(int(a))]


# View ------------------------------------------------------------------------

# Main view
with DivLayout(server):
    html.Div("The slider is at {{ a }}")
    html.Input(
        type="range",
        min=0,
        max=20,
        step=1,
        v_model=("a", 0),  # Set a default value of 0 to variable "a"
    )
    html.Input(
        type="range",
        min=0,
        max=20,
        step=1,
        value=(
            "a",
        ),  # property v-model bind (:modelValue + @update:modelValue || :value + @input)
        disabled=True,
    )
    with html.Ul():
        with html.Li(
            "{{ name }}",
            key="idx",
            v_for="name, idx in ul_li_list",
            style=("{ color: idx > 3 ? 'red': 'green' }",),
        ):
            html.Span(
                "(you are not alone)",
                v_if="idx > 0",
                style=("`font-weight: ${idx > 5 ? 'bold' : 'normal'}`",),
            )
            html.Span("(you are alone)", v_else=True)


# Start Server ----------------------------------------------------------------

server.start()
