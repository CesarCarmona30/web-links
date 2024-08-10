import reflex as rx
# import web_links.constants as const
# from web_links.routes import Route
from web_links.components.link_button import link_button
from web_links.components.title import title
from web_links.styles.styles import Color, Spacing

def links() -> rx.Component:
  return rx.vstack(
    title("Contacto"),
    link_button(
      "GitHub", 
      "Mi GH profile", 
      "icons/github.svg",
      "https://github.com/CesarCarmona30",
      True,
      Color.SECONDARY.value
    ),
    link_button(
      "LinkedIn",
      "Mi Ln profile", 
      "icons/linkedin.svg",
      "https://www.linkedin.com/in/c%C3%A9sar-carmona-67a751308/",
    ),
    title("Redes"),
    link_button(
      "Facebook", 
      "Mi Fb profile", 
      "icons/facebook.svg",
      "https://www.facebook.com/clcg58/"
    ),
    link_button(
      "Instagram", 
      "Mi Ig profile",
      "icons/instagram.svg",
      "https://www.instagram.com/cesar58.js/"
    ),
    link_button(
      "X", 
      "Mi X profile",
      "icons/x_twitter.svg",
      "https://x.com/_cesar_carmona"
    ),
    width="100%",
    spacing=Spacing.DEFAULT.value
  )
