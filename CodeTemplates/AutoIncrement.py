# flet run test.py
import flet as ft


class IncrementCounter(ft.UserControl):
    def __init__(self, text: str, start_number: int = 0) -> None:
        super().__init__()
        self.text = text
        self.counter = start_number
        self.text_number: ft.Text = ft.Text(value=str(start_number), size=40)

    def increment(self, e: ft.ControlEvent):
        self.counter += 1
        self.text_number.value = str(self.counter)
        self.update()

    def build(self) -> ft.Row:
        return ft.Row(controls=[ft.ElevatedButton(self.text, on_click=self.increment), self.text_number],
                      alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                      width=300)


def main(page: ft.Page) -> None:

    # window setup
    page.title = 'Reusable App'
    page.spacing = 30
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'
    #
    # page.bgcolor = '#000000'
    # page.window.width = 360
    # page.window.height = 700
    # page.window.resizable = False

    # TODO: НАСЛЕДОВАНИЕ ЧЕКНИ
    page.add(IncrementCounter('People'))
    page.add(IncrementCounter('Animals', 10))
    page.add(IncrementCounter('Items', 25))


ft.app(target=main)
