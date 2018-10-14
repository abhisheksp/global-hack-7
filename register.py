from cryptography.fernet import Fernet
from firebase_admin import db

cipher_key = ''
with open('cipher_key.txt') as f:
    cipher_key = bytes(f.readline(), 'utf-8')

cipher_suite = Fernet(cipher_key)


def register_group(group_id):
    print('Registering Facebook group: {}'.format(group_id))
    existing_groups = db.reference('/group_ids').get() or []
    existing_groups = set(existing_groups)
    existing_groups.add(group_id)
    existing_groups = list(existing_groups)
    root = db.reference('/')
    root.update({'group_ids': existing_groups})
    return 'Facebook group {} successfully registered'.format(group_id)


def register_number(number):
    print('Registering Number: {}'.format(number))
    encrypted_number = cipher_suite.encrypt(bytes(number, 'utf-8'))
    existing_numbers = db.reference('/numbers').get() or []
    existing_numbers = set(existing_numbers)
    existing_numbers.add(encrypted_number.decode('utf-8'))
    existing_numbers = list(existing_numbers)
    root = db.reference('/')
    root.update({'numbers': existing_numbers})
    return '{} successfully registered'.format(number)
