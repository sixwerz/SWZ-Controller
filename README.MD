<h2 align="center">🕹️ ** Telegram remote controller - Manage your PC with Telegram ** 🕹️</h1>

## Screenshots:
![screenshot 1](https://github.com/sixwerz/SWZ-Controller/blob/main/screenshots/screenshot1.png)

## Required Libraries

```
pip install pyTelegramBotAPI
pip install pyautogui
pip install opencv-python
```

pyTelegramBotApi - library for creating Telegram bots. \n
pyautogui - library for mouse and keyboard control \n
opencv-python - library for use a web camera \n

## How to use

In the line you need to change bot_token to the token of your bot

```
bot = telebot.TeleBot('bot_token')
```
*bot token can be found at @BotFather*

then you can run controller.py
and go to the telegram bot

When you start the bot using the <strong>/start</strong> command, you will see a menu with a list for managing the computer
