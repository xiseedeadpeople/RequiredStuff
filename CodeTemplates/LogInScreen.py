# flet run test.py
import flet as ft

button = ft.ElevatedButton(
    text="Кастомная кнопка",
    width=400,
    height=200,
    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=ft.BorderRadius(
        top_left=60,
        top_right=60,
        bottom_left=60,
        bottom_right=60
    )),

    bgcolor='#F1F1F1',
    color=ft.colors.WHITE
    )
)

def main(page: ft.Page) -> None:

    # window setup
    # page.spacing = 30
    page.vertical_alignment = 'center'
    page.horizontal_alignment = 'center'

    # page.window_title_bar_hidden = True
    page.window.full_screen = False
    page.bgcolor = '#000000'
    page.window.width = 1920
    page.window.height = 1080
    # page.window.resizable = False

    # fields setup
    text_username: ft.TextField = ft.TextField(label='привет, {юзернейм}', text_align=ft.TextAlign.LEFT,
                                               width=500, text_size=20, hint_text='логин',
                                               border_color='#FFFFFF')

    text_password: ft.TextField = ft.TextField(label=' ', text_align=ft.TextAlign.LEFT,
                                               width=500, text_size=20, hint_text='пароль',
                                               border_color='#FFFFFF', password=True, can_reveal_password=True)

    checkbox_signup: ft.Checkbox = ft.Checkbox(label='соглашаюсь с правилами использования (реферну позже их тут)', value=False, )
    submit_button = ft.ElevatedButton = ft.ElevatedButton(text='войти', width=500, disabled=True)

    def validate(e: ft.ControlEvent) -> None:
        """ проверяем """
        if all([text_username.value, text_password.value, checkbox_signup.value]):
            submit_button.disabled = False

        else:
            submit_button.disabled = True

        page.update()

    def submit(e: ft.ControlEvent) -> None:
        """Функция, которая идет после прохода логин экрана"""
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
            ], alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=main)
