14–16 февраля 2024 

Проект подготовлен в рамках MegaSchool'24 по треку искусственный интеллект

### Идея: создать Retrieval-Augmented Generation ассистента, способного вести диалог на основе  данных, извлеченных из истории telegram каналов, чатов и других источников с использованием локальной LLM.

### Описание

<details><summary><b>Что делает наше приложение?</b></summary>

- [Видео-демонстрация](https://drive.google.com/file/d/18JUK7K6xzXk3STs3g2sm5rz1H2a4ktrk/view?usp=sharing)
- [Примеры ответов](https://github.com/alexiv-tn65/MegaSchool-24/blob/main/images/example.png)
</details>

<details><summary><b>Установка и запуск приложения</b></summary>

- склонируйте репозиторий  `git clone https://github.com/alexiv-tn65/MegaSchool-24.git`
- установите зависимости  `pip install -r requirements.txt`
- скачайте (экспортируйте) историю чата или телеграм канала  в файл *.json, как показано на картинке ![Alt text](https://github.com/alexiv-tn65/MegaSchool-24/blob/main/images/export_telegram_history.png)
- [Видео-демонстрация подготовки фаила](https://drive.google.com/file/d/1wklGH_8Op8Kk2k9KD2XjNWOMw_UBZXaA/view?usp=sharing)
- назовем этот файл `result.json`
- сгенерируйте фаил `preprocessed_data.pkl` из  `result.json`, выполнив в командной строке: `python -m file_preparation path\to\your\result.json`
- например: `python -m file_preparation examples\result.json`
- запустите приложение командой:  `python3 run_app.py`
</details>


<details><summary><b> How to install and run the application</b></summary>

### What do you need? 
1. Python 3.11 (Tested with Python 3.11.8)
2. Сhat history from telegram or other sources
3. A [Llama.cpp](https://github.com/ggerganov/llama.cpp) supported model in your local system

HOW TO INSTALL
1) clone this repo  `git clone https://github.com/alexiv-tn65/MegaSchool-24.git`
2) install requirements.  `pip install -r requirements.txt`


HOW TO RUN
1) download (export) chat history from telegram to *.json file as shown in the picture,\
   let's call this file `result.json`
2) generate a file `preprocessed_data.pkl` from `result.json`,\
   run the command:\
   python -m file_preparation path\to\your\result.json \
   example:\
   python -m file_preparation examples\result.json

3) move your LL model file in *.gguf format  to `models\`
4) set the environment variable **MODEL_PATH** to your model:\
   export MODEL_PATH=/path/to/your/model/file

5) start: python3 run_app.py

</details>
