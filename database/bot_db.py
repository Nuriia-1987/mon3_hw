import sqlite3
import random

from config import bot

def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()
    if db:
        print("База данных подключина!")

    db.execute("CREATE TABLE IF NOT EXISTS menu"
                "(photo TEXT, style TEXT,"
               "name TEXT PRIMARY KEY,"
                "decription TEXT,"
                "wigth INTEGER, price INTEGER)")
    db.commit()


async def sgl_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO menu VALUES"
                       "(?, ?, ?, ?, ?, ?)", tuple(data.values()))
    db.commit()


async def dql_command_random(message):
    result = cursor.execute("SELECT * FROM menu").fetchall()
    random_user = random.choice(result)
    await bot.send_photo(message.chat.id, random_user[0],
                         caption=f"Type: {random_user[1]}\n"
                                 f"Name: {random_user[2]}\n"
                                 f"Description: {random_user[3]}\n"
                                 f"Weight: {random_user[4]}\n"
                                 f"Price: {random_user[5]}")


async def sql_command_all():
    return cursor.execute("SELECT * FROM menu").fetchall()


async def sql_command_delete(name):
    cursor.execute("DELETE FROM menu WHERE name == ?", (name, ))
    db.commit()
