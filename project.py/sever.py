import sqlite3
import hashlib
import socket
import threading

sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever.bind(("localhost", 9999))
sever.listen()

def handle_connection(c):
    c.send("Username: ".encode())
    username = c.recv(1024).decode()
    c.send("password: ".encode())
    password = c.recv(1024)
    password = hashlib.sha256(password).hexdigest()

    conn = sqlite3.connect("userdata")
    cur = conn.cursor()

    cur.execute("SELECT * FROM userdata WHERE username = ? AND password = ?",(username,password))

    if cur.fetchall():
        c.send("Login successful".encode())
    else:
        c.send("login failed".encode())

while True:
    client, addr = sever.accept()
    threading.Thread(target=handle_connection, args=(client,)).start()
