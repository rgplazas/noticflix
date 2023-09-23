import flet as ft
from flet import *
from sidebar import ModernNavBar

# main function
def main(page: Page):
    #title
    page.title = "NoticFlex"

    #alignemnts
    page.horizontal_alignment="center"
    page.vertical_alignment="center"

    #add class to page
    page.add(
        Container(
            width=200,
            height=580,
            bgcolor="black",
            border_radius=10,
            animate=animation.Animation(500, "decelerate"), #animate the sidebar
            alignment= alignment.center, # aling inner contents
            padding=10,
            content=ModernNavBar()
        )
    )   

    page.update()

ft.app(target=main)