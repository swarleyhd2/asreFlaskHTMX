import firebase_admin
from firebase_admin import firestore

app = firebase_admin.initialize_app()
db = firestore.client()

class Equipment:
    def __init__(self, unit, make, model, year, category, serial, last_pm='1/1/2000', hours=0, status='down', last_location='none', service_history=[], rental_history=[]):
        self.unit = unit
        self.make = make
        self.model = model
        self.year = year
        self.hours = hours
        self.status = status
        self.last_location = last_location
        self.category = category
        self.last_pm = last_pm
        self.serial = serial
        self.service_history = service_history
        self.rental_history = rental_history



class RentalRequest:
    def __init__(self, start_date, est_duration, customer, location, requestor, contact, purchase_order, items=[]):

        
class MoveRequest:
    def __init__(self, date, customer, start, end, requestor):

class RepairRequest:
    def __init__(self, unit, customer, date, contact, requestor):

class RentalContract:
    def __init__(self,):