from datetime import datetime
import locale


def get_date() -> str:
    user_locale: tuple[str | None, str | None] = locale.getlocale()

    try:
        locale.setlocale(locale.LC_TIME, user_locale)
    except locale.Error:
        print(f'Locale {user_locale} is not supported on your system. Falling back to "C" locale.')
        locale.setlocale(locale.LC_TIME, 'C')

    xtoday: datetime = datetime.now()

    return f'{xtoday:%c}'  # d.m.y h:m:s
