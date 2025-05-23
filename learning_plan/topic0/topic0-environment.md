# 🧱 Тема 0 — Подготовка окружения и инструментов

В этой теме ты узнаешь, как установить и настроить всё, что нужно, чтобы **программировать на Python как батя**: интерпретатор, VS Code, терминал, GitHub, виртуальное окружение, pip и многое другое.

## 🔥 Список пунктов и их будущая структура

Каждый пункт содержит:

- 👀 Введение: краткий обзор (what about)
- 📚 Теорию: что это, зачем, история, различия
- 🧪 Подпункты: по шагам, с разбором нюансов
- ✅ Практика: 2 задания на каждый подпункт
- ⚒️ Мини-проект по пункту
- 📘 Теоретический мини-тест

---

## 📌 Пункт 1: Что такое интерпретатор Python

- What about: зачем он нужен, как работает
- CPython, PyPy, Jython
- Интерпретация vs Компиляция (таблица)
- Что такое REPL и зачем он нужен

## 📌 Пункт 2: Установка Python (Windows / macOS / Linux)

- What about: в чём отличие версий, зачем руками ставить
- Где скачать официально, какие галочки ставить/не ставить
- Проверка установки в терминале
- Что такое PATH и зачем он нужен

## 📌 Пункт 3: Установка VS Code и обзор интерфейса

- What about: зачем VS Code именно под Python
- Установка, конфигурация
- Интерфейс: боковая панель, редактор, терминал, плагины
- Запуск файла `.py` внутри VS Code
- `code .` из терминала (и как включить)

## 📌 Пункт 4: Установка расширений VS Code для Python

- What about: зачем нужны расширения вообще
- Python Extension, Pylance, Black Formatter
- GitLens, Code Runner, Auto Rename Tag
- Как обновлять, отключать, настраивать расширения

## 📌 Пункт 5: Консоль, терминал, запуск `.py` файлов

- What about: зачем терминал если есть мышка
- Терминал vs консоль
- Разные оболочки: Git Bash, PowerShell, CMD
- Как запускать Python-скрипт через `python`, `python3`, `py`

## 📌 Пункт 6: Что такое Git и GitHub (основы)

- What about: для чего всё это и как оно связано
- История Git, Линус Торвальдс, децентрализация
- GitHub vs GitLab vs Bitbucket
- Как работает Git: коммиты, ветки, push/pull
- Git vs SVN (фан-сравнение)

## 📌 Пункт 7: Установка Git и создание аккаунта на GitHub

- What about: твоя цель — пушнуть свой код в сеть
- Как установить Git на разных ОС
- Как настроить имя и почту в git
- Как создать и оформить аккаунт на GitHub
- Настройка через VS Code GUI (альтернатива консоли)

## 📌 Пункт 8: Настройка SSH-ключа и push/pull

- What about: чем SSH лучше чем HTTPS
- Генерация ключа через `ssh-keygen`
- Подключение ключа к GitHub
- Проверка соединения, первая синхронизация
- Где хранится ключ (`~/.ssh`)

## 📌 Пункт 9: Как создать проект в VS Code

- What about: что значит "проект" в контексте Python
- Создание папки, открытие в редакторе
- Стартовый `main.py`, запуск, терминал
- Сохранение структуры проекта

## 📌 Пункт 10: Структура Python-проекта

- What about: зачем вообще нужна структура
- src/, main.py, tests/, .gitignore, .vscode/
- Где лучше хранить venv
- Что такое `__init__.py`, когда он нужен

## 📌 Пункт 11: Работа с виртуальным окружением (`venv`)

- What about: зачем оно нужно вообще
- Отличие `venv` от `virtualenv` и `conda`
- Как создать, активировать и удалить `venv`
- Использование в VS Code автоматически

## 📌 Пункт 12: Установка зависимостей через pip

- What about: откуда Python знает как ставить пакеты
- pip install, uninstall, list, freeze
- Использование `python -m pip install`
- PyPI, поиск библиотек, проверка актуальности

## 📌 Пункт 13: Создание `requirements.txt`

- What about: зачем этот файл вообще нужен
- Создание через `pip freeze > requirements.txt`
- Установка зависимостей из файла
- Использование при клонировании проекта

---
