14–16 февраля 2024 

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
2. Сhat history from telegram or other sources
3. A [Llama.cpp](https://github.com/ggerganov/llama.cpp) supported model in your local system

HOW TO INSTALL
1) clone this repo  `git clone https://github.com/alexiv-tn65/MegaSchool-24.git`
2) install requirements.  `pip install -r requirements.txt`


HOW TO RUN
1) download (export) chat history from telegram to *.json file as shown in the picture,
   let's call this file `result.json`
2) generate a file `preprocessed_data.pkl` from `result.json`,\
   run the command:\
   python -m file_preparation path\to\your\result.json
   example:\
   python -m file_preparation examples\result.json

3) move your LL model file in *.gguf format  to `models\`
4) set the environment variable **model_path** to your model:\
   export MODEL_PATH=/path/to/your/model/file

5) start: python3 run_app.py
