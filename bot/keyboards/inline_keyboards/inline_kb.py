from pprint import pprint
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from handlers.inline_kb_callbacks.callback_factory import Level, LevelCallbackFactory


def create_inline_kb(width: int,
                     *args: str,
                     button_source: list | None = None,
                     last_btn: str | None = None,
                     **kwargs: str) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []

    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=button_source[button] if button in button_source else button,
                callback_data=button))

    # Заполняем список кнопками из аргументов kwargs
    if kwargs:
        for text, button in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)
    # Добавляем в билдер последнюю кнопку, если она передана в функцию
    if last_btn:
        kb_builder.row(InlineKeyboardButton(
            text=last_btn,
            callback_data="last_btn"
        ))

    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


def create_kb_exercises_levels() -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()
    for lvl in Level:
        kb_builder.button(
            text=lvl.value.title(),
            callback_data=LevelCallbackFactory(lvl=lvl)
        )
    return kb_builder.as_markup()
