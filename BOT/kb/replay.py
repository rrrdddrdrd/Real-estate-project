from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove


admin_menu = ReplyKeyboardMarkup(
    keyboard=[
        # [
        #     KeyboardButton(text='Добавить объект'),
        # ],
        [
            KeyboardButton(text='Добавить объекты в excel'),
        ],
        [
            KeyboardButton(text='Добавить администратора'),
        ],
        [
            KeyboardButton(text='Статистика по объектам'),
        ],
        [
            KeyboardButton(text='Вывести все объекты в excel'),
        ],
        [
            KeyboardButton(text='Статистика по объектам в excel'),
        ],
        [
            KeyboardButton(text='Изменить статус объекта на продан'),
        ],
    ],
    resize_keyboard=True,
)

phone_count = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='‼️‼️НАЖМИТЕ СЮДА ДЛЯ РЕГИСТРАЦИИ НОМЕРА ТЕЛЕФОНА‼️‼️',
                           request_contact=True),

        ],
    ],
    # resize_keyboard=True,
)
