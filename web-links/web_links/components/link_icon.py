import reflex as rx
from web_links.styles.styles import Size

def link_icon(
    image: str, 
    url: str, 
    alt: str, 
    width: str = Size.VERY_BIG.name, 
    height: str = Size.VERY_BIG.name
  ) -> rx.Component:
  return rx.link(
    rx.image(
      src=image,
      width=width,
      height=height,
      alt=alt
    ),
    href=url,
    is_external=True
  )