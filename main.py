from gtts import gTTS
import re, codecs, winsound

FILE = '1. Getting started with Blender 3.1.srt'
# FILE = '1. Getting started with Blender 3.2.srt'

def SubtitleToMp3(fileName):
    # Открыть файл с текстом и прочитать его содержимое
    with codecs.open(fileName, 'r', encoding='utf-8') as f:
        text = f.read()

        # Удаление номеров строк и временных меток.
        text2 = re.sub(r'\d+\n\d{2}:\d{2}:\d{2},\d+ --> \d{2}:\d{2}:\d{2},\d+\n', '', text)

    # Инициализировать объект gTTS с текстом и языком
    tts = gTTS(text = text2, lang = 'ru')

    # Сохранить аудиофайл
    tts.save("output.mp3")

    # Подать звуковой сигнал, когда всё будет готово!
    winsound.Beep(2500, 500)


if __name__ == "__main__":
    SubtitleToMp3(FILE)
