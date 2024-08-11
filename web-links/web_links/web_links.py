import reflex as rx
from web_links.components.navbar import navbar
from web_links.components.footer import footer
from web_links.views.header.header import header
from web_links.views.links.links import links
import web_links.styles.styles as styles
from web_links.styles.styles import Size

class State(rx.State):
    pass

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )

app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)
app.add_page(
    index,
    title="Links",
    description="Web de enlaces a mis redes sociales elaborado con Python puro utilizando Reflex.",
    image="favicon.ico"
)
app._compile()