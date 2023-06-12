import pysrt
import re
from gtts import gTTS

from pydub import AudioSegment
import os
import winsound


subs = pysrt.open('1. Getting started with Blender 3.1.srt') # маленький
# subs = pysrt.open('1. Getting started with Blender 3.2.srt')  # весь ! огромный
# subs = pysrt.open('1. Getting started with Blender 3.3.srt')  # средний

clean_subs = []

for sub in subs:
    # text = re.sub(r'\d', '', sub.text)
    text = re.sub(r'\d+\n\d{2}:\d{2}:\d{2},\d+ --> \d{2}:\d{2}:\d{2},\d+\n', '', sub.text)
    clean_subs.append(text)

for i, sub in enumerate(clean_subs):
    tts = gTTS(sub, lang='ru')
    filename = f'{subs[i].start.to_time().strftime("%H;%M;%S,%f")}.mp3'
    filename = filename.replace(':', ';')  # Замена двоеточий
    tts.save(filename)


#########################################

# 2 Вручную
# audio_files = [
#     '00;00;00,390000.mp3', 
#                '00;00;01,111000.mp3', '00;00;03,000000.mp3',
#                '00;00;05,230000.mp3', '00;00;17,980000.mp3']

# Автоматом. Получаем список файлов в текущей директории
files = os.listdir('.')
audio_files = tuple([file for file in files if file.endswith('.mp3') 
                     and file != 'output.mp3'
                     and file != 'combined_audio.mp3'])

# print(audio_files)

    

# Создаем пустой сегмент длительностью равной общей длительности всех аудиофайлов
total_duration = sum([AudioSegment.from_file(file).duration_seconds * 1000 for file in audio_files])
combined_audio = AudioSegment.silent(duration=total_duration+20000)

# Наложение каждого аудиофайла на пустой сегмент с учетом временной задержки
start_time = 0
for file in audio_files:
    time_str = file.split('.')[0] # получаем строку временного кода из названия файла

    hours = int(time_str[0:2]) # первые два символа - часы
    minutes = int(time_str[3:5]) # следующие два символа - минуты
    seconds = int(time_str[6:8]) # следующие два символа - секунды
    time_ms = ((hours * 60 + minutes) * 60 + seconds) * 1000 # преобразуем в миллисекунды

    segment = AudioSegment.from_file(file)
    duration = segment.duration_seconds
    # print("duration: ", duration)

    # combined_audio = combined_audio.overlay(segment, position=start_time+time_ms)
    combined_audio = combined_audio.overlay(segment, position = start_time + time_ms + duration)

# Сохраняем объединенный аудиофайл
combined_audio.export("combined_audio.mp3", format="mp3")

# Подать звуковой сигнал, когда всё будет готово!
winsound.Beep(2500, 500)
