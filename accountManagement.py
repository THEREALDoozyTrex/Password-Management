import sqlite3

conn = sqlite3.connect("masterPass.db")

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS masterPasswords (
    user text,
    passw text
    )""")

def signup(user,passw):
    c.execute("INSERT INTO masterPasswords (user, passw) VALUES (?, ?)", (user, passw))

def login(username, password):
    c.execute("SELECT * FROM masterPasswords WHERE passw=? AND user=?", (password, username))
    var1 = c.fetchall()

    if var1 != []: return True
    else: return False

    conn.commit()
    conn.close()
