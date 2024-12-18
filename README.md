# vk_clicker
Эта программа принимает от пользователя нужную для сокращения ссылку, и выводит сокращенный вариант на экран.
Или же выводит количество переходов по ссылке

Программа всё сделает за вас на основе методов VK API, вам нужно лишь ввести ссылку.

## Как установить 
Для запуска понадобится токен [VK API](https://dev.vk.com/ru), а так же установленный [Python](https://pythonru.com/baza-znanij/gde-skachat-python-i-kak-ego-ustanovit-na-linux-mac-os-windows) на вашем компьютере. Затем используйте команду `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.
Так же понадобится библиотека `load-dotenv`, которая позволяет загружать переменные окружения из файла .env в вашу среду выполнения. Это полезно для управления конфиденциальной информацией, такой как ключи API и настройки конфигурации.
Установите её командой:
```python
pip install python-dotenv
```
Создайте файл `.env` со всеми переменными среды, которые необходимы вашему приложению(в нашем случае - это [VK API](https://dev.vk.com/ru), а так же установленный [Python](https://pythonru.com/baza-znanij/gde-skachat-python-i-kak-ego-ustanovit-na-linux-mac-os-windows, который позволяет делать запрос к сайту). Важно, добавьте `.env`-файл в .gitignore.

![Снимок экрана 2024-12-17 в 18 39 14](https://github.com/user-attachments/assets/b924224b-22e8-4bce-9e78-fd8bf725fbcf)


## Как запустить 
Для запуска скрипта из терминала используйте команду `python3`, путь до репозитория, название файла с кодом и через пробел вашу ссылку.


<img width="864" alt="Снимок экрана 2024-12-15 в 21 03 51" src="https://github.com/user-attachments/assets/f7151526-9c24-4e53-95fe-5e029378bef5" />


У меня это `python3 Desktop/vk_clicker/hello_api.py vk.com`

![Untitled](https://github.com/user-attachments/assets/0454d1e6-396c-484a-a62a-de48a20af6f1)
