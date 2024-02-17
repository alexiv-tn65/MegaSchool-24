14–16 февраля 2024, https://mega.itmo.ru/megaschool

Проект подготовлен в рамках MegaSchool'24 по треку искусственный интеллект

## Описание

## Идея: создать ассистента для изучения иностранных языков

## Результаты проекта:

-
-
### Demo
-

## Установка

HOW TO INSTALL
### What do you need? 
1. A free Telegram bot token from [@BotFather](https://t.me/BotFather)
2. A [Llama.cpp](https://github.com/ggerganov/llama.cpp) supported model in your local system 

1) clone this repo  `git clone https://github.com/alexiv-tn65/MegaSchool-24.git`
2) install requirements.  `pip install -r MegaSchool-24\requirements_app.txt`


HOW TO RUN
1) get bot token from https://t.me/BotFather
2) add bot token to environment:
export BOT_TOKEN=<Your Telegram bot token>

3) move your model file to `models\`
4) set **model_path** to your model: 
export MODEL_PATH=/path/to/your/model/file

5) start: python3 main.py

FEATURES: