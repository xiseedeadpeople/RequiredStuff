import flet as ft
from flet_core import ControlEvent, TextField, Checkbox, ElevatedButton


def main(page: ft.Page) -> None:

    # window setup
    page.title = 'signup'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.bgcolor = '#FFFFFF'
    page.window.width = 360
    page.window.height = 700
    page.window.resizable = False

    # fields setup
    text_username: ft.TextField = TextField(label='Логин', text_align=ft.TextAlign.LEFT, width=200)
    text_password: ft.TextField = TextField(label='Пароль', text_align=ft.TextAlign.LEFT, width=200, password=True)
    checkbox_signup: ft.Checkbox = Checkbox(label='Я соглашаюсь четотам', value=False)
    submit_button = ft.ElevatedButton = ElevatedButton(text='Зарегестрироваться', width=200, disabled=True)

    def validate(e: ControlEvent) -> None:
        """ проверяем """
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            submit_button.disabled = False
        else:
            submit_button.disabled = True

        page.update()

    def submit(e: ControlEvent) -> None:
        print(f'Username: {text_username.value}')
        print(f'Password: {text_password.value}')

        page.clean()

        page.add(
            ft.Row(
                controls=[ft.Text(value=f'Welcome: {text_username.value}', size=20)],
                alignment=ft.MainAxisAlignment.CENTER
            )

        )

    checkbox_signup.on_change = validate
    text_username.on_change = validate
    text_password.on_change = validate
    submit_button.on_click = submit

    page.add(
        ft.Row(
            controls=[
                ft.Column(
                    [text_username,
                    text_password,
                    checkbox_signup,
                    submit_button]
                )
            ], alignment= ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)
