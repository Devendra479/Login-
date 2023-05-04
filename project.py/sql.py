import sqlite3
import hashlib



conn = sqlite3.connect("userdata")
cur= conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata(
   id INTEGER PRIMARY KEY,
   username VARCHAR(255) NOT NULL,
   password VARCHAR(255) NOT NULL
)
""")


username1, password1 = "Dev", hashlib.sha256("Dev3456".encode()).hexdigest()
username2, password2 = "Kev", hashlib.sha256("Fev3458".encode()).hexdigest()
username3, password3 = "Cev", hashlib.sha256("DeVEN356".encode()).hexdigest()
username4, password4 = "Mev", hashlib.sha256("ADV3456".encode()).hexdigest()
cur.execute("INSERT INTO userdata (username,password) VALUES(?,?)",(username1,password1))
cur.execute("INSERT INTO userdata (username,password) VALUES(?,?)",(username2,password2))
cur.execute("INSERT INTO userdata (username,password) VALUES(?,?)",(username3,password3))
cur.execute("INSERT INTO userdata (username,password) VALUES(?,?)",(username4,password4))
cur.execute("SELECT * FROM userdata")


conn.commit()