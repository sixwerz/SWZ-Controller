<h1>🕹️ ** Telegram remote controller - Manage your PC with Telegram ** 🕹️</h1>

## Screenshots:

## Required Libraries

```
pip install pyTelegramBotAPI
pip install pyautogui
pip install opencv-python
```

pyTelegramBotApi - library for creating Telegram bots.
pyautogui - library for mouse and keyboard control
opencv-python - library for use a web camera

## How to use

In the line you need to change bot_token to the token of your bot

```
bot = telebot.TeleBot('bot_token')
```
*bot token can be found at @BotFather*

then you can run controller.py
and go to the telegram bot

When you start the bot using the <s>/start</s> command, you will see a menu with a list for managing the computer


