import pyrebase

config = {
    "apiKey": "AIzaSyAT0-Rbo7uNHKMdoLwcuBhpEV86w0gvl6k",
    "authDomain": "clipboard-6718f.firebaseapp.com",
    "databaseURL": "https://clipboard-6718f.firebaseio.com",
    "storageBucket": "clipboard-6718f.appspot.com"
}

firebase = pyrebase.initialize_app(config)
user = firebase.auth().sign_in_with_email_and_password("test@test.com", "1q1q1q")
db = firebase.database()


def send_to_firebase(val):
    db.child("data").push(val, user['idToken'])


def listen_to_firebase(handler):
    print("Listening to Firebase server...")
    db.child("data").stream(handler, user['idToken'])

