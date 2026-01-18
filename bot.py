#!/usr/bin/env python3

import os
import telebot
import buttons as btn
import config as cfg
from telebot.types import Message
from PIL import Image


bot = telebot.TeleBot(cfg.__token__)


def add_pic(x, y, message: Message):
    if message.content_type == 'photo':
        try:
            image_get = bot.get_file(message.photo[-1].file_id)
            image = bot.download_file(image_get.file_path)
            with open(cfg.__path__+'/user_images/image_'+str(message.chat.id)+'.png', 'wb') as new_image:
                new_image.write(image)
            if os.path.exists(cfg.__path__+'/user_images/tier_list_'+str(message.chat.id)+'.png'):
                tier_list = Image.open(cfg.__path__+'/user_images/tier_list_'+str(message.chat.id)+'.png')
            else:
                tier_list = Image.open(cfg.IMAGE)
            tier_image = Image.open(cfg.__path__+'/user_images/image_'+str(message.chat.id)+'.png')
            tier_image = tier_image.resize((330, 322))
            tier_list.paste(tier_image, (x,y))
            tier_list.save(cfg.__path__+'/user_images/tier_list_'+str(message.chat.id)+'.png')
            with open (cfg.__path__+'/user_images/tier_list_'+str(message.chat.id)+'.png', 'rb') as user_tier_list:
                bot.send_photo(message.chat.id, user_tier_list, caption='Ваш тир-лист сейчас выглядит так')
                os.remove(cfg.__path__+'/user_images/image_'+str(message.chat.id)+'.png')
                return True
        except:
            bot.send_message(message.chat.id, 'Неизвестная ошибка!\nПроверьте ваше изображение либо попробуйте снова.', reply_markup=btn.StopMenu)
            return False
    else:
        bot.send_message(message.chat.id, 'Вы прислали: '+message.content_type+'\nОжидалось: photo', reply_markup=btn.StopMenu)
        return False


@bot.message_handler(commands=['start'])
def start(message: Message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, 'Чтобы создать тир-лист нажмите начать', reply_markup=btn.BeginMenu)

@bot.callback_query_handler(func=lambda callback: callback.data=='begin')
def begin(callback):
    bot.delete_message(chat_id=callback.message.chat.id , message_id=callback.message.message_id)
    if os.path.exists(cfg.__path__+'/user_images/tier_list_'+str(callback.message.chat.id)+'.png'):
        with open(cfg.__path__+'/user_images/tier_list_'+str(callback.message.chat.id)+'.png', 'rb') as image:
            bot.send_message(callback.message.chat.id, 'Обнаружен сохраненный тир-лист', reply_markup=btn.DeleteMenu)
            bot.send_photo(callback.message.chat.id, image, reply_markup=btn.TierMenu)
    else:
        with open(cfg.IMAGE, 'rb') as image:
            bot.send_photo(callback.message.chat.id, image, reply_markup=btn.TierMenu)

@bot.callback_query_handler(func=lambda callback: callback.data=='S')
def s_tier(callback):
    msg = bot.send_message(callback.message.chat.id, 'Загрузите изображение для категории S', reply_markup=btn.StopMenu)
    bot.register_next_step_handler(msg, s_tier2)

def s_tier2(message: Message):
    if add_pic(x=351, y=11, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите второе изображение для категории S', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, s_tier3)

def s_tier3(message: Message):
    if add_pic(x=698, y=11, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите третье изображение для категории S', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, s_tier4)

def s_tier4(message: Message):
    if add_pic(x=1052, y=11, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите четвертое изображение для категории S', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, s_tier5)

def s_tier5(message: Message):
    if add_pic(x=1407, y=11, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите пятое изображение для категории S', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, s_tier6)

def s_tier6(message: Message):
    if add_pic(x=1761, y=11, message=message) == True:
        bot.send_message(message.chat.id, 'Категория S готова!', reply_markup=btn.TierMenu)

@bot.callback_query_handler(func=lambda callback: callback.data=='A')
def a_tier(callback):
    msg = bot.send_message(callback.message.chat.id, 'Загрузите изображение для категории A', reply_markup=btn.StopMenu)
    bot.register_next_step_handler(msg, a_tier2)

def a_tier2(message: Message):
    if add_pic(x=351, y=350, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите второе изображение для категории A', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, a_tier3)

def a_tier3(message: Message):
    if add_pic(x=698, y=350, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите третье изображение для категории A', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, a_tier4)

def a_tier4(message: Message):
    if add_pic(x=1052, y=350, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите четвертое изображение для категории A', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, a_tier5)

def a_tier5(message: Message):
    if add_pic(x=1407, y=350, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите пятое изображение для категории A', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, a_tier6)

def a_tier6(message: Message):
    if add_pic(x=1761, y=350, message=message) == True:
        bot.send_message(message.chat.id, 'Категория A готова!', reply_markup=btn.TierMenu)

@bot.callback_query_handler(func=lambda callback: callback.data=='B')
def b_tier(callback):
    msg = bot.send_message(callback.message.chat.id, 'Загрузите изображение для категории B', reply_markup=btn.StopMenu)
    bot.register_next_step_handler(msg, b_tier2)

def b_tier2(message: Message):
    if add_pic(x=351, y=690, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите второе изображение для категории B', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, b_tier3)

def b_tier3(message: Message):
    if add_pic(x=698, y=690, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите третье изображение для категории B', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, b_tier4)

def b_tier4(message: Message):
    if add_pic(x=1052, y=690, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите четвертое изображение для категории B', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, b_tier5)

def b_tier5(message: Message):
    if add_pic(x=1407, y=690, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите пятое изображение для категории B', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, b_tier6)

def b_tier6(message: Message):
    if add_pic(x=1761, y=690, message=message) == True:
        bot.send_message(message.chat.id, 'Категория B готова!', reply_markup=btn.TierMenu)

@bot.callback_query_handler(func=lambda callback: callback.data=='C')
def c_tier(callback):
    msg = bot.send_message(callback.message.chat.id, 'Загрузите изображение для категории C', reply_markup=btn.StopMenu)
    bot.register_next_step_handler(msg, c_tier2)

def c_tier2(message: Message):
    if add_pic(x=351, y=1029, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите второе изображение для категории C', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, c_tier3)

def c_tier3(message: Message):
    if add_pic(x=698, y=1029, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите третье изображение для категории C', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, c_tier4)

def c_tier4(message: Message):
    if add_pic(x=1052, y=1029, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите четвертое изображение для категории C', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, c_tier5)

def c_tier5(message: Message):
    if add_pic(x=1407, y=1029, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите пятое изображение для категории C', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, c_tier6)

def c_tier6(message: Message):
    if add_pic(x=1761, y=1029, message=message) == True:
        bot.send_message(message.chat.id, 'Категория C готова!', reply_markup=btn.TierMenu)

@bot.callback_query_handler(func=lambda callback: callback.data=='D')
def d_tier(callback):
    msg = bot.send_message(callback.message.chat.id, 'Загрузите изображение для категории D', reply_markup=btn.StopMenu)
    bot.register_next_step_handler(msg, d_tier2)

def d_tier2(message: Message):
    if add_pic(x=351, y=1368, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите второе изображение для категории D', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, d_tier3)

def d_tier3(message: Message):
    if add_pic(x=698, y=1368, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите третье изображение для категории D', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, d_tier4)

def d_tier4(message: Message):
    if add_pic(x=1052, y=1368, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите четвертое изображение для категории D', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, d_tier5)

def d_tier5(message: Message):
    if add_pic(x=1407, y=1368, message=message) == True:
        msg = bot.send_message(message.chat.id, 'Загрузите пятое изображение для категории D', reply_markup=btn.StopMenu)
        bot.register_next_step_handler(msg, d_tier6)

def d_tier6(message: Message):
    if add_pic(x=1761, y=1368, message=message) == True:
        bot.send_message(message.chat.id, 'Категория D готова!', reply_markup=btn.TierMenu)

@bot.callback_query_handler(func=lambda callback: callback.data=='delete')
def delete(callback):
    bot.delete_message(chat_id=callback.message.chat.id, message_id=callback.message.message_id)
    if os.path.exists(cfg.__path__+'/user_images/tier_list_'+str(callback.message.chat.id)+'.png'):
        os.remove(cfg.__path__+'/user_images/tier_list_'+str(callback.message.chat.id)+'.png')
        bot.send_message(callback.message.chat.id, 'Тир-лист успешно удален!')
        begin(callback)
    else:
        bot.send_message(callback.message.chat.id, 'Тир-лист не найден!')


if __name__ == '__main__':
    bot.polling(none_stop=True)
