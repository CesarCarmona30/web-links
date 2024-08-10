import reflex as rx
import datetime
from web_links.styles.styles import Size, Spacing
from web_links.styles.styles import Color, TextColor
from web_links.components.link_icon import link_icon

def footer() -> rx.Component:
    return rx.vstack(
        link_icon(
            "./icons/code.svg",
            "https://github.com/cesarcarmona30/web-links",
            "Source code",
            width=Size.VERY_BIG.value,
            height=Size.VERY_BIG.value,
        ),
        rx.link(
            f"{datetime.date.today().year} - ©César Carmona",
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