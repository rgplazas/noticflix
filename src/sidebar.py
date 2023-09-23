import flet as ft
from flet import *
from functools import partial
import time

# sidebar class
class ModernNavBar(UserControl):
    def _init__(self):
        super().__init__()
    
    def UserData(self, initials: str, name: str, description: str):
        # fist row user info, different from the icon rows, so we create a seperate function for it
        return Container(
            content=Row(
                controls=[
                    Container(
                        width=42,
                        height=42,
                        bgcolor="bluegrey900",
                        alignment=alignment.center,
                        border_radius=8,
                        content=Text(
                            value=initials,
                            size=20,
                            weight="bold",
                            color="white54",
                        )
                    ),
                    Column(
                        spacing=1,
                        alignment="center",
                        controls=[
                            Text(
                                value=name,
                                size=11,
                                weight="bold",
                                color="white54",
                                # here we need to include some details for the animation (comes later)
                                opacity=1, # full opacity 0 - 1
                                animate_opacity=200 # speed of animation
                            ),
                            Text(
                                value=description,
                                size=9,
                                weight="w400",
                                color="white54",
                                # here we need to include some details for the animation (comes later)
                                opacity=1, # full opacity 0 - 1
                                animate_opacity=200 # speed of animation
                            ),
                        ]
                    )
                ]
            )
        )
    
    #now for the main sidebar row and icons
    def ContainedIcon(self, icon_name:str, text:str):
        return Container(
            width=180,
            height=45,
            border_radius=10,
            on_hover=None,
            content=Row(
                controls=[
                    IconButton(
                        icon=icon_name,
                        icon_size=18,
                        icon_color="white54",
                        style=ButtonStyle(
                            shape={
                                "":RoundedRectangleBorder(radius=7),
                            },
                            overlay_color={"":"transparent"},
                        ),
                    ),
                    Text(
                        value=text,
                        color="white54",
                        size=11,
                        opacity=1,
                        animate_opacity=200,
                    )
                ]
            ),
        )
        pass

    def build(self):
        return Container(
            # define dimensiones y caracteristicas cuando retornamos el contenedor
            width=200,
            height=580,
            padding=padding.only(top=10),
            alignment=alignment.center,
            content=Column(
                controls=[
                # agregar los iconos del sidebar
                self.UserData("LI","Line Indent","Software Endineer"),
                # add a divider
                Divider(height=5, color="transparent"),
                self.ContainedIcon(icons.SEARCH, "Search"),
                self.ContainedIcon(icons.DASHBOARD_ROUNDED, "Dashboard"),
                self.ContainedIcon(icons.BAR_CHART, "Revenue"),
                self.ContainedIcon(icons.NOTIFICATIONS, "Notifications"),
                self.ContainedIcon(icons.PIE_CHART_OUTLINE_ROUNDED, "Analytics"),
                self.ContainedIcon(icons.FAVORITE_ROUNDED, "Likes"),
                ]
            )
        )

