
import sqlite3

conn = sqlite3.connect("masterPass.db")

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS masterPasswords (
    user text,
    passw text
    )""")

def signup(username, password):
    c.execute("INSERT INTO masterPasswords VALUES ? ?", username, password)
    conn.commit()
    conn.close()

def login(username, password):
    c.execute("SELECT * FROM masterPasswords WHERE passw=? AND user=?", (password, username))
    if passw == password and user == username:
        return True
    else:
        return False

    conn.commit()
    conn.close()
