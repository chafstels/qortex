# Qortex

Qortex - тестовое задание

## Запуск проекта

Чтобы запустить проект, выполните следующие шаги:

1. Склонируйте репозиторий с помощью команды:

   ```bash
   git clone git@github.com:chafstels/qortex.git

2. Создайте файл .env и скопируйте весь текст из файла example_env в него. Этот файл будет содержать конфигурационные настройки для вашего проекта.
   ```bash
   cp example_env .env

3. Наконец, запустите проект с помощью Docker Compose:
   ```bash
   docker-compose up --build