import reflex as rx
from web_links.styles.styles import Size
from web_links.styles.styles import TextColor

def info_text(title: str, body: str) -> rx.Component:
  return rx.box(
    rx.text(
      title, 
      as_="span",
      font_weight="bold", 
      color=TextColor.HEADER.value
    ),
    f" {body}", 
    font_size=Size.MEDIUM.value,
    color=TextColor.BODY.value
  )