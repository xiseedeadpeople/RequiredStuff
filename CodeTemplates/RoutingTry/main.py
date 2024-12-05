import flet as ft
from views.FletRouter import Router
from idk.AppBar import NavBar

def main(page: ft.Page):

    page.theme_mode = "dark"
    page.appbar = NavBar(page)
    myRouter = Router(page)

    page.on_route_change = myRouter.route_change

    page.add(
        myRouter.body
    )
    page.go('/')

ft.app(target=main)





