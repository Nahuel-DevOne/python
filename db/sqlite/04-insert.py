import sqlite3

with sqlite3.connect("db/sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        "insert into usuarios values(?, ?)",
        (1, "Hola Mundo"), 
    ) # para evitar una SQL Injection

