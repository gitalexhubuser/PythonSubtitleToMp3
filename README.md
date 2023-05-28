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

После создания venv, далее его необходимо активировать!

## Гайд по активации venv в cmd

Доказательством его активации будет служить серый текст в скобочках слева:
<img src="https://i.imgur.com/Dnif6tL.png" width="100%" align="center"/>

Заменить путь на свой, и тупо запустить `run.cmd`

Внури уже вписана команда по активации venv

`cmd /k "cd /d E:\PythonSubtitle\bogatov_subtitles\Scripts & activate` 

## Гайд по активации venv в VSCode

Доказательством его активации будет служить зелёный текст в скобочках слева:

<img src="https://i.imgur.com/qJXt77V.png" width="100%" align="center"/>

Есть хорошая команда в VSCode `Activate Env In Current Terminal` и по умолчанию она отключена! И в user и в workspace.
Если её включить в настройках (File - Preferences - Settings - ввод в поиск фразы "Activate Env In Current Terminal"), то venv будет сразу автоматически активироваться при открытии и запуске проекта.

Вручную я активировал venv введя эти команды:

`bogatov_subtitles\Scripts\activate.bat`

`.\bogatov_subtitles\Scripts\activate`

Не 2 сразу! А какая-то из них.


## Как прочувствовать venv

Введя команду `pip list` - можно увидеть список установленных библиотек.

Таким образом, можно иметь 100500 версий одной и той же библиотеки.

<img src="https://i.imgur.com/GOxSEpn.png" width="100%" align="center"/>

## Ссылки
| Описание | Ссылка |
| ------ | ------ |
Урок: | https://www.youtube.com/watch?v=APOPm01BVrk
Репо: | https://github.com/gitalexhubuser/PythonSubtitleToMp3
