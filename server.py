import os
from functools import wraps
from flask import Flask, render_template, request, jsonify, abort, redirect, make_response
from flask_login import LoginManager, login_user
import firebase_admin
from firebase_admin import auth, credentials, exceptions
import datetime
from dotenv import load_dotenv

app = Flask(__name__)

#no cred necessary running on google cloud
cred = credentials.Certificate("serviceaccountkey.json")
firebase_app = firebase_admin.initialize_app(cred)

def protected(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        cookie = request.cookies.get('session')
        if not cookie:
            return redirect('/signin')
        try:
            decodedCookie = auth.verify_session_cookie(cookie, check_revoked=True)
            return func(*args, **kwargs)
        except auth.InvalidSessionCookieError:
            return redirect('/signin')
    return wrapper

@app.route("/")
def welcome():
    return render_template('welcome.html')

#Authentication-----------------------------------

@app.route("/signup")
def signUp():
    return render_template('auth/signup.html')

@app.route("/signin")
def signIn():
    return render_template('auth/signin.html')

@app.route("/resetpassword")
def passwordReset():
    return render_template('auth/forgotpassword.html')

@app.route('/sessionLogin', methods=['POST'])
def session_login():
    token = request.json['idToken']
    expires_in = datetime.timedelta(days=5)
    try:
        session_cookie = auth.create_session_cookie(id_token=token, expires_in=expires_in, app=firebase_app)
        response = jsonify({'status': 'success'})
        expires = datetime.datetime.now() + expires_in
        response.set_cookie('session', session_cookie,  expires=expires, httponly=True, secure=True)
        return response
    except exceptions.FirebaseError:
        return abort(401, 'Failed to create session token')

@app.route("/logout")
def logout():
    try:
        resp = make_response(redirect('/signin'))
        resp.set_cookie('session', expires=0)
        return resp
    except:
        return redirect("/signin")

#Dispatch----------------------------------------

@app.route("/dispatch")
@protected
def dispatch():
    return render_template('welcome.html')

if __name__ == "__main__":
    app.run(debug=True)