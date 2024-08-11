import reflex as rx
import web_links.constants as const
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
      const.GITHUB_URL,
      highlight_color=Color.SECONDARY.value
    ),
    link_button(
      "LinkedIn",
      "Mi Ln profile", 
      "icons/linkedin.svg",
      const.LINKEDIN_URL,
    ),
    title("Redes"),
    link_button(
      "Facebook", 
      "Mi Fb profile", 
      "icons/facebook.svg",
      const.FACEBOOK_URL
    ),
    link_button(
      "Instagram", 
      "Mi Ig profile",
      "icons/instagram.svg",
      const.INSTAGRAM_URL
    ),
    link_button(
      "X", 
      "Mi X profile",
      "icons/x_twitter.svg",
      const.XTWITTER_URL
    ),
    width="100%",
    spacing=Spacing.DEFAULT.value
  )
