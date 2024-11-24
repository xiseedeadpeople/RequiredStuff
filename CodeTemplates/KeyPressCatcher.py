# flet run test.py
import flet as ft


def main(page: ft.Page) -> None:

    # window setup
    page.title = 'signup'
    page.spacing = 30
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    page.bgcolor = '#000000'
    page.window.width = 360
    page.window.height = 700
    page.window.resizable = False

    #
    key = ft.Text('Key', size=20, color='pink')
    shift = ft.Text('Shift', size=20, color='red')
    ctrl = ft.Text('Ctrl', size=20, color='blue')
    alt = ft.Text('Alt', size=20, color='green')

    #
    def on_keyboard(e: ft.KeyboardEvent) -> None:
        key.value = e.key
        shift.visible = e.shift
        ctrl.visible = e.ctrl
        alt.visible = e.alt
        print(e.data)
        page.update()

    #
    page.on_keyboard_event = on_keyboard


    #
    page.add(
        ft.Text('exexexexex'),
        ft.Row(
            controls=[key, shift, alt,ctrl],
            alignment=ft.MainAxisAlignment.CENTER)
    )

ft.app(target=main)
