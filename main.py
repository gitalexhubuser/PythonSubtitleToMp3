import winsound
from gtts import gTTS
import codecs
import re

# Открыть файл с текстом и прочитать его содержимое
# with open('1. Getting started with Blender 3.1.srt', 'r') as file:
#     text = file.read()

with codecs.open('1. Getting started with Blender 3.2.srt', 'r', encoding='utf-8') as f:
    text = f.read()

    # Удаление номеров строк и временных меток.
    text2 = re.sub(r'\d+\n\d{2}:\d{2}:\d{2},\d+ --> \d{2}:\d{2}:\d{2},\d+\n', '', text)

# Инициализировать объект gTTS с текстом и языком
tts = gTTS(text=text2, lang='ru')

# Сохранить аудиофайл
tts.save("output.mp3")
winsound.Beep(2500, 500)