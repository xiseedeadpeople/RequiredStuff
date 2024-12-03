# main
# flet, flet_route
import flet as ft
from flet_route import Routing, path
from eer import MyHome
from xrx import DetailsParam


def main(page: ft.Page) -> None:
    page.theme_mode = 'dark'

    app_rroutes = [
        path(url='/',
             clear=True,
             view=MyHome.view)

        # path(url='/details/:you_id',
        #      clear=True,
        #      view=DetailsParam.view2)
    ]

    Routing(page=page, app_routes=app_rroutes)
    page.go(page.route)


ft.app(target=main)

# --------------------------------------------------------------------------------------------------------
# 2nd screen
import flet as ft
from flet_route import Routing, path, Params, Basket

class MyHome:
    def __init__(self):
        pass

    def view(self, page: ft.Page, params: Params, basket: Basket) -> ft.View:
        print(params)

        s_y_p = '"s_y_p" triggered (:err.py" -> 11)'

        return ft.View(
            '/', controls=[
                ft.Text('Homepage!', size=30),
                ft.ElevatedButton('go to ???', on_click=lambda _:page.go(f'/details/{s_y_p}'))
            ]
        )

# --------------------------------------------------------------------------------------------------------
# 3rd screen
from flet_route import Routing, path, Params, Basket
import flet as ft


class DetailsParam:
    def __init__(self):
        pass

    def view(self, page: ft.Page, params: Params, basket: Basket) -> ft.View:

        mydetails = params.get('you_id')

        return ft.View(
            '/details/:you_id', controls=[
                ft.Text(f'yo param is {mydetails}', size=30),
                ft.ElevatedButton('Back Home', bgcolor='blue', color='white', on_click=lambda _:page.go('/'))
            ]
        )

