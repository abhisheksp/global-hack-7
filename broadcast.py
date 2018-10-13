import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from cryptography.fernet import Fernet
from whatsapp import send_messages


cred = credentials.Certificate('service.json')
firebase_admin.initialize_app(cred, {
    "databaseURL": 'https://globalhacks7.firebaseio.com',
})

cipher_key = ''
with open('cipher_key.txt') as f:
    cipher_key = bytes(f.readline(), 'utf-8')

cipher_suite = Fernet(cipher_key)


def find_numbers():
    numbers_encrypted = db.reference('/numbers').get()
    number_decrypter = lambda n: cipher_suite.decrypt(bytes(n, 'utf-8')).decode('utf-8')
    numbers = list(map(number_decrypter, numbers_encrypted))
    return numbers


def broadcast(message):
    print('message: ', message)
    numbers = find_numbers()
    print('found numbers:', numbers)
    send_messages(numbers, message)
    return 'Broadcast successful!'
