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


def save_event(message, from_number, event_metadata):
    location = event_metadata['location']
    nationality = event_metadata['nationality']
    group_name = event_metadata['groupName']
    data = {
        "event": message,
        "patronPhone": from_number,
        "location": location,
        "nationality": nationality,
        "messengerType": 'Whatsapp',
        "groupName": group_name
    }
    root = db.reference()
    root.child('events').push(data)


def identify_event_metadata(from_number):
    found_patrons = list(db.reference('patron').order_by_child("phone").equal_to(from_number).get().values())
    if len(found_patrons) == 0:
        return None, False
    patron = found_patrons[0]
    return patron, True


def broadcast(from_number, message):
    print('message: ', message)
    numbers = find_numbers()
    print('found numbers:', numbers)
    send_messages(numbers, message)
    tweet(message)
    facebook_group_post(message)
    metadata, found = identify_event_metadata(from_number)
    if not found:
        return 'Broadcast successful but unknown Patron'
    save_event(message, from_number, metadata)
    return 'Broadcast successful!'
