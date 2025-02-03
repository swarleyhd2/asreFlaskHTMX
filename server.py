import os
from functools import wraps
from flask import Flask, render_template, request, jsonify, abort, redirect, make_response, Response, url_for
from flask_login import LoginManager, login_user
from firebase_admin import auth, exceptions
from firebase_init import firebase_app
import datetime
from dotenv import load_dotenv
from intuitlib.client import AuthClient
from intuitlib.enums import Scopes
from intuitlib.exceptions import AuthClientError
from uuid import uuid4 as uuid
from form_select_options import equipmentTypes, customers
from firestore_db import Equipment, Customers, Moves, Reservations, Repairs, Rentals, get_locations_select, get_reservations, get_customer_data, create_customer, create_location, create_move, create_rental, create_repair, create_reservation
from forms import moveForm, rentalForm, repairForm, newCustomerForm, newLocationForm

load_dotenv()

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

auth_client = AuthClient(
    client_id = os.getenv('CLIENT_ID'),
    client_secret = os.getenv('CLIENT_SECRET'),
    redirect_uri = 'http://localhost:5000/oauthcallback',
    environment = 'sandbox'
)

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
    
@app.route("/quickbooksAuthorization")
def quicbooksAuth():

    url = auth_client.get_authorization_url([Scopes.ACCOUNTING])

    return redirect(url)

@app.route("/oauthcallback")
def oauthCallback():
    try:
        auth_client.get_bearer_token(request.args.get('code'), request.args.get('realmId'))

    except AuthClientError as e:
        print(e.status_code)
        print(e.content)
    print('callback')
    return render_template('welcome.html')

#Dispatch----------------------------------------
    
@app.route("/order-events")
def orderEvent():
    def eventStream():
        while True:
            yield f'event: NewPickup \ndata: <div>hi</div>\n\n'
    
    return Response(eventStream(), mimetype='text/event-stream')

@app.route("/dispatch")
#@protected
def dispatch():
    return render_template('dispatch.html')
#Sales--------------------------------------------
@app.route("/settings")
#@protected
def settings():
    return render_template('settings.html')

@app.route("/orders")
#@protected
def orders():

    return render_template('orders.html', equipmentTypes=equipmentTypes, newlocationform = newLocationForm(), newcustomerform = newCustomerForm())

@app.route("/newrental", methods=['POST','GET']) 
def newRental():
    form = rentalForm()
    if request.method == 'POST' and form.validate():
            print('test working')
            
    return render_template('modals_and_forms/rental-form.html', equipmentTypes=equipmentTypes, form=form)
            
@app.route("/newrepair", methods=['POST','GET'])         
def newRepair():
    print('repair')
    form = repairForm()
    if request.method == 'POST':
        if form.validate():
            try:
                print('test working')
                return {'status': 'success'}
            except Exception as e:
                print(e)
                return {'error': e}
    else:
        return render_template('modals_and_forms/service-form.html', moveForm=form)
            
@app.route("/newmove", methods=['POST','GET'])           
def newMove():
    form = moveForm()
    if request.method == 'POST':
        if form.validate():
            try:
                print('test working')
                return {'status': 'success'}
            except Exception as e:
                print(e)
                return {'error': e}
    else:
        return render_template('modals_and_forms/move-form.html', moveForm=form)
                  

@app.route("/equipmenttypesection")
def equipmentTypeSection():
    return render_template('modals_and_forms/equipment-form.html', equipmentTypes=equipmentTypes)

@app.route("/dispatchitems")
def dispatchItems():
        res = get_reservations()
        return render_template("modals_and_forms/dispatch-items.html", fdata=res)

@app.route("/locations" , methods=['GET'])
def locations():
    customerID = request.args.get('customer')
    locations = get_locations_select(customerID)
    modalURL = url_for('locationModal', customer=customerID)
    return render_template("modals_and_forms/location-select-options.html", locations=locations, url=modalURL)

@app.route("/locationmodal", methods=['POST', 'GET'])
def locationModal():
    locationModalForm = newLocationForm()

    if request.method == "GET":
        customerID = request.args.get('customer')
        locationModalForm.customer.data = customerID

    if request.method == "POST" and locationModalForm.validate():
        formData = {
            'customer': locationModalForm.customer.data,
            'jobsite': locationModalForm.jobsite.data,
            'address': locationModalForm.address.data,
            'city': locationModalForm.city.data,
            'state': locationModalForm.state.data,
        }
        create_location(formData)
        print('location saved')
    return render_template("modals_and_forms/newlocation.html", newlocationform = locationModalForm)
        
@app.route("/customermodal", methods=['POST', 'GET'])
def customerModal():
    customerModalForm = newCustomerForm()
    if request.method == "POST" and customerModalForm.validate():
        print('customer saved')
    return render_template("modals_and_forms/newcustomer.html", newcustomerform = customerModalForm)



if __name__ == "__main__":
    app.run(debug=True)


