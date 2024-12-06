import flet as ft
from flet_model import Router, Model


class Secondp(Model):
    route = 'home'
    controls = [ft.Text('2nd here here', size=20), ft.ElevatedButton('go gome', on_click='about_to')]

    def about_to(self, e):
        self.page.go('home')


class Homepage(Model):
    route = 'home'
    controls = [ft.Text('Homepage here', size=20), ft.ElevatedButton('second_page', on_click='second_page_to')]

    def second_page_to(self, e):
        self.page.go('second_page')


def main(page: ft.Page):
    page.theme_mode = 'light'

    Router(
        {'home': Homepage(page), 'second_page': Secondp(page)}
    )
    print(page.route)
    page.go(page.route)

ft.app(main)
