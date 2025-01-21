import firebase_admin
from firebase_admin import firestore


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

    def save():
        pass
    def update(self):
        pass



class Reservations:
    def __init__(self, start_date, customer, location, requestor, contact, purchase_order, items=[]):
        pass
        
class Moves:
    def __init__(self, date, customer, start, end, requestor):
        pass

class Repairs:
    def __init__(self, unit, customer, date, contact, requestor):
        pass

class Rentals:
    def __init__(self,):
        pass

class Customers:
    def __init__(self, name, address, phone, email):
        pass
    def save():
        pass
    def update(self):
        pass
    def get_locations(self):
        pass
    def get_moves(self):
        pass
    def get_rentals(self):
        pass
    def get_repairs(self):
        pass
    def get_reservations(self):
        pass