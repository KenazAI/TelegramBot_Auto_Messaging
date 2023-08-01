# TelegramBot_Auto_Messaging
The project aims to provide users with an interactive and versatile Telegram bot that simplifies various tasks related to nicknames, messaging, and content distribution.

The bot utilizes the Telegram API and SQLite databases to store and retrieve data. Users can interact with the bot using text commands in a Telegram chat, and the bot responds accordingly. Additionally, the bot comes with a graphical user interface (GUI) built with Tkinter, allowing users to control its functionalities through buttons and input fields.

The main functionalities of the bot are as follows:

Generate Random Nicknames: The bot can generate random nicknames of a specified length using English letters.

Search Nicknames: Users can search for nicknames in the database by providing a keyword, and the bot will display the matching results.

Automatic Message Distribution: The bot can send a predefined message to all the stored nicknames in the database.

Create Chats, Groups, and Channels: The bot can create chats, groups, and channels based on parameters stored in the database.

Load Content: The bot can retrieve content (e.g., images, audio, video) from the content database and send it to users.

The project aims to provide users with an interactive and versatile Telegram bot that simplifies various tasks related to nicknames, messaging, and content distribution.



Функционал бота:

Генерация случайных никнеймов: Бот может генерировать случайные никнеймы заданной длины из букв английского алфавита.

Поиск никнейма по ключевой фразе: Бот выполняет поиск никнеймов в базе данных по заданной ключевой фразе и выводит найденные результаты.

Автоматическая рассылка сообщений: Бот может отправлять заданное сообщение всем никнеймам, хранящимся в базе данных.

Создание чатов, групп и каналов: Бот может создавать чаты, группы и каналы на основе параметров из базы данных.

Загрузка контента: Бот может загружать контент (например, изображения, аудио, видео) из базы данных и отправлять его пользователю.

Инструкция по запуску:

Установите необходимые библиотеки:

Убедитесь, что у вас установлены библиотеки telebot и tkinter. Если их нет, установите их, выполнив следующую команду в командной строке (терминале):

pip install pyTelegramBotAPI

pip install tk
Создайте Telegram бота и получите токен:

Перейдите в Telegram и найдите бота @BotFather.
Следуйте инструкциям для создания нового бота и получения его токена.
Создайте базы данных и таблицы:

Создайте четыре базы данных: nicknames.db, chats.db, content.db, и content_table.
Создайте таблицы nicknames_table, chats_table, и content_table в соответствующих базах данных. Опишите структуру таблиц в соответствии с указанными выше полями.
Запустите бота:

Вставьте ваш токен Telegram бота в код, заменив 'YOUR_TELEGRAM_BOT_TOKEN' на ваш токен.
Запустите скрипт в вашей среде разработки или из командной строки (терминала):
Copy code
python your_bot_script.py
Используйте бота:

Бот будет работать на основе команд, которые можно отправлять ему в чате. Например, вы можете отправить команду /generate для генерации случайного никнейма или /search <keyword> для поиска никнеймов по ключевой фразе <keyword>. Ваш бот также будет иметь графический интерфейс пользователя (GUI) с использованием библиотеки tkinter, который позволит вам управлять ботом с помощью кнопок и текстовых полей.
Наслаждайтесь функционалом бота:

Теперь вы можете пользоваться функционалом бота, генерировать никнеймы, выполнять поиск, создавать чаты и рассылать сообщения всем никнеймам в базе данных. Вы также можете загружать контент и отправлять его пользователям. Пользуйтесь и наслаждайтесь всеми возможностями вашего Telegram бота!
