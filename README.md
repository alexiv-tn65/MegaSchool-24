14–16 февраля 2024, https://mega.itmo.ru/megaschool

Проект подготовлен в рамках MegaSchool'24 по треку искусственный интеллект

## Идея: создать ассистента для изучения иностранных языков

## Описание

<details><summary><b>Что делает наш сервис?</b></summary>

</details>

<details><summary><b>Запуск сервиса</b></summary>


</details>


## Результаты проекта:

- [Презентация]
- [Демонстрация работы]
- [Демонстрация работы]

## Установка и запуск


### What do you need? 
1. Python 3.11 (Tested with Python 3.11.8)
2. A free Telegram bot token from [@BotFather](https://t.me/BotFather)
3. A [Llama.cpp](https://github.com/ggerganov/llama.cpp) supported model in your local system

HOW TO INSTALL
1) clone this repo  `git clone https://github.com/alexiv-tn65/MegaSchool-24.git`
2) install requirements.  `pip install -r MegaSchool-24\requirements_app.txt`


HOW TO RUN
1) get bot token from https://t.me/BotFather
2) add bot token to environment:
export BOT_TOKEN="Your Telegram bot token"

3) move your model file to `models\`
4) set **model_path** to your model: 
export MODEL_PATH=/path/to/your/model/file

5) start: python3 main.py

FEATURES: