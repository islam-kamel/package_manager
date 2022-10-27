import firebase_admin
from firebase_admin import firestore
from firebase_admin import get_app

# Application Default credentials are automatically created.
config = {
    'apiKey': "AIzaSyAayjmvIcb7cwojSNZH2h5h3I2yrfrx-CM",
    'authDomain': "update-manager-c767d.firebaseapp.com",
    'projectId': "update-manager-c767d",
    'storageBucket': "update-manager-c767d.appspot.com",
    'messagingSenderId': "859352236545",
    'appId': "1:859352236545:web:4263d5fb299a747b31b600",
    'measurementId': "G-5EZ124GW63"
}

# cred_obj = firebase_admin.credentials.Certificate('./cred.json')
app = firebase_admin.initialize_app()
# app = firebase_admin.get_app('package')
db = firestore.client()
# print(app.credential)
