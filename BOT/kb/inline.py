from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


async def inline_house_1():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Продать дом', callback_data='продать_дом'))
    keyboard.adjust(1,)
    return keyboard.as_markup()


async def inline_object_type():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Дом', callback_data='Дом'))
    keyboard.add(InlineKeyboardButton(text='Дача', callback_data='Дача'))
    keyboard.add(InlineKeyboardButton(text='Котедж', callback_data='Котедж'))
    keyboard.adjust(1,)
    return keyboard.as_markup()

async def inline_number_floors():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='1', callback_data='1'))
    keyboard.add(InlineKeyboardButton(text='2', callback_data='2'))
    keyboard.add(InlineKeyboardButton(text='3', callback_data='3'))
    keyboard.add(InlineKeyboardButton(text='4', callback_data='4'))
    keyboard.add(InlineKeyboardButton(text='5', callback_data='5'))
    keyboard.adjust(2, 2, 1)
    return keyboard.as_markup()


async def inline_wall_material():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Кирпич', callback_data='Кирпич'))
    keyboard.add(InlineKeyboardButton(text='Бревно', callback_data='Бревно'))
    keyboard.add(InlineKeyboardButton(text='Брус', callback_data='КБрусотедж'))
    keyboard.add(InlineKeyboardButton(text='Пеноблок', callback_data='Пеноблок'))
    keyboard.add(InlineKeyboardButton(text='Газоселикатный блок', callback_data='Газоселикатный блок'))
    keyboard.add(InlineKeyboardButton(text='Керамзитобетонный блок', callback_data='Керамзитобетонный блок'))
    keyboard.add(InlineKeyboardButton(text='Сэндвич панель', callback_data='Сэндвич панель'))

    keyboard.adjust(2, 2, 1, 1, 1)
    return keyboard.as_markup()



async def inline_yes():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='подведен', callback_data='подведен'))
    keyboard.add(InlineKeyboardButton(text='возможность подключения', callback_data='возможность подключения'))
    keyboard.adjust(1,)
    return keyboard.as_markup()

async def inline_yes_no():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Да', callback_data='Да'))
    keyboard.add(InlineKeyboardButton(text='Нет', callback_data='Нет'))
    keyboard.adjust(2,)
    return keyboard.as_markup()

async def inline_post():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Опубликовать', callback_data='Опубликовать'))
    keyboard.add(InlineKeyboardButton(text='Отмена', callback_data='Отмена'))
    keyboard.adjust(2,)
    return keyboard.as_markup()