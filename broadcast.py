import requests
from firebase_admin import db
from cipher import cipher
from whatsapp import send_messages
from twitter import tweet


def find_numbers():
    numbers_encrypted = db.reference('/numbers').get()
    cipher_suite = cipher()
    number_decrypter = lambda n: cipher_suite.decrypt(bytes(n, 'utf-8')).decode('utf-8')
    numbers = list(map(number_decrypter, numbers_encrypted))
    return numbers


def find_group_ids():
    group_ids = db.reference('/group_ids').get()
    return group_ids


def facebook_group_post(message):
    group_ids = find_group_ids()
    print('Group IDS: ', group_ids)
    url = 'https://cce34c71.ngrok.io/grouppost'
    payload = {'message': message, 'groupids': group_ids}
    requests.post(url, json=payload)


def broadcast(message):
    print('message: ', message)
    numbers = find_numbers()
    print('found numbers:', numbers)
    send_messages(numbers, message)
    tweet(message)
    facebook_group_post(message)
    return 'Broadcast successful!'
