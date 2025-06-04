from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton


async def inline_price_house():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text='Показать объявления', callback_data='показать_объявления'))
    keyboard.add(InlineKeyboardButton(text="🔍 Фильтр объявлений", callback_data="фильтр_объявлений"))
    keyboard.add(InlineKeyboardButton(text='Показать избранные объявления', callback_data='показать_избранные_объявления'))
    keyboard.add(InlineKeyboardButton(text='Вывести все объекты в exel', callback_data='exel'))

    keyboard.adjust(1,)
    return keyboard.as_markup()


async def inline_price_house_filtr():
    keyboard = InlineKeyboardBuilder()
    keyboard.add(InlineKeyboardButton(text="🏡 Дома", callback_data="filter_category_Дом"))
    keyboard.add(InlineKeyboardButton(text="🏢 Квартиры", callback_data="filter_category_Квартира"))
    keyboard.add(InlineKeyboardButton(text="🌿 Участки", callback_data="filter_category_Участок"))
    keyboard.add(InlineKeyboardButton(text="💸 Цена до 3 млн", callback_data="filter_price_3000000"))
    keyboard.add(InlineKeyboardButton(text="💸 Цена до 5 млн", callback_data="filter_price_5000000"))
    keyboard.add(InlineKeyboardButton(text="🔍 Показать объявления", callback_data="показать_отфильтрованные"))
    keyboard.add(InlineKeyboardButton(text="❌ Отмена", callback_data="cancel_filter"))


    keyboard.adjust(1,)
    return keyboard.as_markup()