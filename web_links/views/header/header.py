import reflex as rx
import datetime
# import link_bio.constants as const
from web_links.components.link_icon import link_icon
from web_links.components.info_text import info_text
from web_links.components.link_button import link_button
from web_links.styles.styles import Size, Spacing
from web_links.styles.styles import Color, TextColor


def header() -> rx.Component:
  return rx.vstack(
    rx.hstack(
      rx.avatar(
        fallback="CC",
        name="César Carmona", 
        size=Spacing.MEDIUM_BIG.value,
        src="/avatar.jpg",
        radius="full",
        color=TextColor.BODY.value,
        bg=Color.CONTENT.value,
        padding="2px",
        border=f"4px solid {Color.PRIMARY.value}"
      ),
      rx.vstack(
        rx.heading(
          "César Carmona", 
          size=Spacing.BIG.value
        ),
        rx.text(
          "@CesarCarmona",
          margin_top=Size.ZERO.value,
          color=Color.SECONDARY.value
        ),
        rx.hstack(
          link_icon(
            "./icons/ipn_white.svg",
            "https://www.ipn.mx",
            "alt",
            Size.LARGE.value,
            Size.LARGE.value
          ),
          link_icon(
            "./icons/upiicsa_white.svg",
            "https://www.upiicsa.ipn.mx",
            "alt",
            Size.LARGE.value,
            Size.LARGE.value
          ),
          spacing=Spacing.LARGE.value,
          padding_top=Size.SMALL.value
        ),
        spacing=Spacing.ZERO.value,
        align_items="start"
      ),
      align="end",
      spacing=Size.DEFAULT.value
    ),
    rx.vstack(
      rx.flex(
        info_text("20", "años"),
        #rx.spacer(),
        info_text("Lic.", "Ciencias de la Informática"),
        #rx.spacer(),
        info_text("CDMX,", "México"),
        width="100%",
        justify_content="space-between"
      ),
      link_button(
        "Spotify",
        "Profile",
        "./icons/spotify.svg",
        "https://open.spotify.com/user/gc8e2cm2ebeeep8j61nk164c1?si=b5addd95a21c4236",
        True,
        "#1db954"
      ),
      width="100%"
    ),
    rx.text(
      """
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
      Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
      Ut enim ad minim veniam, 
      quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
      Duis aute irure dolor in reprehenderit.
      """,
      font_size=Size.DEFAULT.value,
      color=TextColor.BODY.value
    ),
    width="100%",
    spacing=Size.BIG.value,
    align_items="start"
  )