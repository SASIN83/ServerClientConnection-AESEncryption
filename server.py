import socket as s
import threading
from datetime import datetime as dt
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

key = b'Sixteen byte key'
iv = b'Sixteen byte iv.'

def encrypt_message(message):
    aes = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(message.encode(), 16)
    encrypted_message = aes.encrypt(padded_data)
    return encrypted_message

def decrypt_message(encrypted_message):
    aes = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = aes.decrypt(encrypted_message)
    unpadded_data = unpad(decrypted_message, 16)
    return unpadded_data.decode()

HEADER = 64 # in bytes
PORT = 5050
#IP = '192.168.1.108'
IP = s.gethostbyname(s.gethostname())
ADDR = (IP,PORT)

server = s.socket(s.AF_INET, s.SOCK_STREAM)
try:
    server.bind(ADDR)
except s.error as e:
    print(e)

def data_handler(data,conn):
    coll = {"SetA":[{"One":1,"Two":2}],"SetB":[{"Three":3,"Four":4}],"SetC":[{"Five":5,"Six":6}],"SetD":[{"Seven":7,"Eight":8}],"SetE":[{"Nine":9,"Ten":10}]}
    try:
        sets,key = data.split("-")
        if sets in coll and key in coll[sets][0]:
            timer =  coll[sets][0][key]
            print(timer)
            for _ in range(timer):
                now = dt.now()
                dt_string = now.strftime("%d-%m-%Y %H:%M:%S")
                conn.send(encrypt_message(dt_string))
                time.sleep(1)
            conn.send(encrypt_message(" "))

        else:
            print(f"{data} is not present in server collection")
            conn.send(encrypt_message("EMPTY"))
    except:
        conn.send(encrypt_message("Invalid Input (Input should be in Set-Number format example: SetA-Two)"))

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected = True
    while connected:
        try:
            msg = conn.recv(2048)
            msg = decrypt_message(msg)
            if msg == "!DISCONNECTED":
                print(f"[CONNECTION CLOSED] {addr} disconnected")
                break
            print(f"[{addr}] : {msg}")
            if msg!="0":
                data_handler(msg,conn)
        except ConnectionResetError:
            print(f"[!Connection Lost - {addr}] An existing connection was forcibly closed by the remote host")
            break
    conn.close()
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")
    while True:
        conn,addr = server.accept()
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

try:
    print("[============== SERVER IS STARTING ==============]")
    start()
except Exception as e:
    print(e)