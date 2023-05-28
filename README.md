# Python Subtitle To Mp3
## Описание
Subtitle __*.srt__ to __*.mp3__

Озвучка субтитров. А так же убирание таймкодов из текста.

Сохранение полученного результат в отдельный звуковой файл.

## Использование

В main.py переменную `FILE` заменить на имя файла для озвучки!

Сейчас стоит `'1. Getting started with Blender 3.2.srt'`

Активировать виртуальное окружение (есть 2 способа)

Установить всё из `requirements.txt` не глобально в систему! А в `venv`.

Запустить скрипт можно через Windows cmd terminal `run.cmd`
Либо через VSCode, файл main.py, открыв терминал и запустив скрипт `ctrl + f5`

## Гайд по созданию venv (виртуальное окружение)
Создание виртуального окружения

Через интепритатор Python, который установлен в систему, ввести команду:

`python -m venv bogatov_subtitles`

где:
`ython` - интепритатор Python установленый в систему либо VSCode
`-m` - ...
`venv` - ...
`bogatov_subtitles` - уникальное имя виртуального окружения, и по факту папка внутри проекта

После создания venv, Далее его необходимо активировать!

## Гайд по активации venv в cmd
Если через `vscode`
Доказательством его активации будет служить зелёный текст в скобочках слева
<img src="https://i.imgur.com/qJXt77V.png" width="100%" align="center"/>

Если через `cmd`
<img src="https://i.imgur.com/Dnif6tL.png" width="100%" align="center"/>



## Гайд по активации venv в VSCode
Activate Env In Current Terminal

``
`bogatov_subtitles\Scripts\activate.bat` 
.\bogatov_subtitles\Scripts\activate 

``

pip list (Голый! При только только созданом виртуальном окружении)
<!-- pip        21.2.4 
setuptools 58.1.0  -->

pip list (Финальный)
<!-- certifi            2023.5.7
charset-normalizer 3.1.0
click              8.1.3
colorama           0.4.6
gTTS               2.3.2
idna               3.4
pip                21.2.4
requests           2.31.0
setuptools         58.1.0
urllib3            2.0.2 -->




## Ссылки
| Описание | Ссылка |
| ------ | ------ |
Урок: | https://www.youtube.com/watch?v=APOPm01BVrk
Репо: | https://github.com/gitalexhubuser/PythonSubtitleToMp3
# PythonSubtitleToMp3
