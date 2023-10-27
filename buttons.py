from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


BeginMenu = InlineKeyboardMarkup()
Begin  = InlineKeyboardButton(text='Начать', callback_data='begin')
BeginMenu.add(Begin)

TierMenu = InlineKeyboardMarkup(row_width=1)
S = InlineKeyboardButton(text='S-Тир', callback_data='S')
A = InlineKeyboardButton(text='A-Тир', callback_data='A')
B = InlineKeyboardButton(text='B-Тир', callback_data='B')
C = InlineKeyboardButton(text='C-Тир', callback_data='C')
D = InlineKeyboardButton(text='D-Тир', callback_data='D')
TierMenu.add(S,A,B,C,D)

DeleteMenu = InlineKeyboardMarkup()
Delete = InlineKeyboardButton(text='Удалить тир-лист', callback_data='delete')
DeleteMenu.add(Delete)

StopMenu = InlineKeyboardMarkup()
Stop = InlineKeyboardButton(text='Остановить', callback_data='stop')
StopMenu.add(Stop)
