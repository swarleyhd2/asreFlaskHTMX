import firebase_admin
from firebase_admin import credentials, firestore

#no cred necessary running on google cloud
cred = credentials.Certificate("svcacct.json")
firebase_app = firebase_admin.initialize_app(cred)
db = firebase_admin.firestore.client(app=firebase_app)