import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('service.json')
firebase_admin.initialize_app(cred, {
    "databaseURL": 'https://globalhacks7.firebaseio.com',
})
