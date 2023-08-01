import telebot
import sqlite3
import random
import string
import tkinter as tk
from tkinter import messagebox

# Инициализация Telegram бота (используйте ваш токен)
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

# Подключение к базе данных SQLite для хранения никнеймов
conn_nicknames = sqlite3.connect('nicknames.db')
cursor_nicknames = conn_nicknames.cursor()

# Подключение к базе данных SQLite для хранения контента
conn_content = sqlite3.connect('content.db')
cursor_content = conn_content.cursor()

# Функция генерации случайных никнеймов
def generate_random_nickname(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

# Функция поиска никнейма по ключам в строке поиска
def search_nickname(search_string):
    conn_nicknames = sqlite3.connect('nicknames.db')
    cursor_nicknames = conn_nicknames.cursor()

    # Используем SQL-запрос для поиска никнеймов по ключевой фразе в базе данных
    cursor_nicknames.execute("SELECT nickname FROM nicknames_table WHERE nickname LIKE ?", ('%' + search_string + '%',))
    results = cursor_nicknames.fetchall()

    # Если найдены результаты, объединяем их в одну строку
    if results:
        found_nicknames = "\n".join(result[0] for result in results)
        return f"Found Nicknames:\n{found_nicknames}"
    else:
        return "No nicknames found for the given search string."

# Функция автоматической рассылки сообщений из базы
def send_message(recipient, text):
    conn_nicknames = sqlite3.connect('nicknames.db')
    cursor_nicknames = conn_nicknames.cursor()

    # Получаем список всех никнеймов из базы данных
    cursor_nicknames.execute("SELECT nickname FROM nicknames_table")
    nicknames = [result[0] for result in cursor_nicknames.fetchall()]

    # Отправляем сообщение каждому никнейму в списке
    for nickname in nicknames:
        try:
            # Здесь используется метод send_message из telebot, чтобы отправить сообщение по заданным параметрам
            bot.send_message(nickname, text)
        except Exception as e:
            # Обрабатываем возможные ошибки при отправке сообщения
            print(f"Error sending message to {nickname}: {e}")
    conn_nicknames.close()

# Функция создания чатов, групп, каналов из списка базы рассылки
def create_chat_group_channel(name):
    conn = sqlite3.connect('chats.db')
    cursor = conn.cursor()

    # Получаем параметры для создания чата из базы данных по его названию
    cursor.execute("SELECT title, description, is_group, is_channel FROM chats_table WHERE title=?", (name,))
    chat_params = cursor.fetchone()

    if chat_params:
        title, description, is_group, is_channel = chat_params

        try:
            if is_group:
                # Здесь используется метод create_group из telebot, чтобы создать группу с заданными параметрами
                created_entity = bot.create_group(chat_title=title)
            elif is_channel:
                # Здесь используется метод create_channel из telebot, чтобы создать канал с заданными параметрами
                created_entity = bot.create_channel(chat_title=title, chat_description=description)
            else:
                # Здесь используется метод create_chat из telebot, чтобы создать чат с заданными параметрами
                created_entity = bot.create_chat(chat_title=title, chat_description=description)

            # Возвращаем результат пользователю
            return f"Created {created_entity.type} {created_entity.title}"
        except Exception as e:
            # Обрабатываем возможные ошибки при создании чатов, групп или каналов
            return f"Error creating chat/group/channel: {e}"
    else:
        return "Chat parameters not found in the database."

    conn.close()

# Функция загрузки контента из специальной базы данных
def load_content(content_id):
    conn = sqlite3.connect('content.db')
    cursor = conn.cursor()

    # Получаем контент из базы данных по его идентификатору
    cursor.execute("SELECT content FROM content_table WHERE id=?", (content_id,))
    content_data = cursor.fetchone()

    if content_data:
        # Отправляем контент пользователю через Telegram бота
        try:
            # Здесь используется метод send_document из telebot, чтобы отправить контент пользователю
            bot.send_document(chat_id='USER_TELEGRAM_CHAT_ID', data=content_data[0])
            return "Content sent successfully!"
        except Exception as e:
            # Обрабатываем возможные ошибки при отправке контента
            return f"Error sending content: {e}"
    else:
        return "Content not found in the database."

    conn.close()

# Окно GUI
root = tk.Tk()
root.title("Telegram Bot GUI")

# Обработчик кнопки для команды /search
def handle_search():
    search_string = search_entry.get()
    result = search_nickname(search_string)
    messagebox.showinfo("Search Result", result)

# Обработчик кнопки для команды /send
def handle_send():
    recipient = recipient_entry.get()
    text = send_entry.get()
    send_message(recipient, text)
    messagebox.showinfo("Message Sent", f"Message sent to {recipient}")

# Обработчик кнопки для команды /generate
def handle_generate():
    generated_nickname = generate_random_nickname()
    messagebox.showinfo("Generated Nickname", f"Generated Nickname: {generated_nickname}")

# Обработчик кнопки для команды /create
def handle_create():
    name = name_entry.get()
    result = create_chat_group_channel(name)
    messagebox.showinfo("Chat/Group/Channel Created", result)

# Обработчик кнопки для команды /load
def handle_load():
    content_id = content_id_entry.get()
    result = load_content(content_id)
    messagebox.showinfo("Load Content Result", result)

# Кнопки и элементы управления GUI
search_label = tk.Label(root, text="Search Nickname:")
search_label.pack()
search_entry = tk.Entry(root)
search_entry.pack()
search_button = tk.Button(root, text="Search", command=handle_search)
search_button.pack()

send_label = tk.Label(root, text="Send Message:")
send_label.pack()
recipient_label = tk.Label(root, text="Recipient:")
recipient_label.pack()
recipient_entry = tk.Entry(root)
recipient_entry.pack()
send_label = tk.Label(root, text="Message Text:")
send_label.pack()
send_entry = tk.Entry(root)
send_entry.pack()
send_button = tk.Button(root, text="Send", command=handle_send)
send_button.pack()

generate_button = tk.Button(root, text="Generate Nickname", command=handle_generate)
generate_button.pack()

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

create_button = tk.Button(root, text="Create Chat/Group/Channel", command=handle_create)
create_button.pack()

content_id_label = tk.Label(root, text="Content ID:")
content_id_label.pack()
content_id_entry = tk.Entry(root)
content_id_entry.pack()
load_button = tk.Button(root, text="Load Content", command=handle_load)
load_button.pack()

# Запуск GUI
root.mainloop()
