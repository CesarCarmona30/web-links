import reflex as rx
import web_links.styles.styles as styles
# from web_links.routes import Route
from web_links.styles.styles import Size
from web_links.styles.styles import Color, TextColor

def navbar() -> rx.Component:
  return rx.hstack(
        rx.link(
            rx.box(
                rx.text("Links", as_="span", color=TextColor.HEADER.value),
                style=styles.navbar_title_style
            ),
            href="/"
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )