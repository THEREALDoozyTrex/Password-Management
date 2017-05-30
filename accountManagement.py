import sqlite3

conn = sqlite3.connect("masterPass.db")

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS master_passwords (
    master_username text,
    master_password text
    )""")

c.execute("""CREATE TABLE IF NOT EXISTS passwords (
    master_username text,
    username text,
    password text
    )""")


def add_password(master_username, password_name, username, password):
    c.execute("INSERT INTO passwords (master_username, username, password) VALUES (?, ?, ?)",
              (master_username, username, password))
    conn.commit()

def get_passwords(master_username):
    c.execute("SELECT * FROM passwords where master_username=?", (master_username,))
    return c.fetchall()


def signup(master_username, master_password):
    c.execute("INSERT INTO master_passwords (master_username, master_password) VALUES (?, ?)",
              (master_username, master_password)
              )
    conn.commit()

def login(master_username, master_password):
    c.execute("SELECT * FROM master_passwords WHERE master_username=? AND master_password=?",
              (master_username, master_password)
              )

    if c.fetchall() != []:
        return True
    else:
        return False
