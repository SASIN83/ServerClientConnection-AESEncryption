import socket as s
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
IP = '192.168.1.108'
ADDR = (IP,PORT)


client = s.socket(s.AF_INET, s.SOCK_STREAM)
client.connect(ADDR)

def send():
    msg = input("Enter Value or press 0 to disconnect: ")
    message = encrypt_message(msg)
    if decrypt_message(message)=="0":
        client.send(encrypt_message("!DISCONNECTED"))
        exit()
    else:
        client.send(message)

def receive():
    receiver = True
    send()
    while receiver:
        receive_message = client.recv(2048)
        receive_message = decrypt_message(receive_message)
        if not receive_message:# or receive_message.decode('utf-8') == "!Done":
            send()
        if receive_message:
            print(receive_message)
            if receive_message in [" ","EMPTY", "Invalid Input (Input should be in Set-Number format example: SetA-Two)"]:
                send()

receive()