import reflex as rx
import datetime
from web_links.styles.styles import Size, Spacing
from web_links.styles.styles import Color, TextColor

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="./icons/code.svg",
            height=Size.VERY_BIG.value,
            width=Size.VERY_BIG.value,
            alt=""
        ),
        rx.link(
            f"{datetime.date.today().year} ©César Carmona",
            href="https://github.com/cesarcarmona30/",
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.text(
            "Made with ♥.",
            font_size=Size.MEDIUM.value,
            margin_top=Size.ZERO.value
        ),
        align="center",
        margin_botton=Size.BIG.value,
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.ZERO.value,
        color=TextColor.FOOTER.value
    )