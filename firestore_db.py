from firebase_init import db

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
        self.start_date = start_date
        self.customer = customer
        self.location = location
        self.requestor = requestor
        self.contact = contact
        self.purchase_order = purchase_order
        self.items = items

    def save():
        pass
    def update(self):
        pass
    def validate():
        pass
        
class Moves:
    def __init__(self, date, customer, pickup, delivery, requestor, notes, equipment, ordered_by='none', delivered_by='none'):
        self.date = date
        self.customer = customer
        self.pickup = pickup
        self.delivery = delivery
        self.requestor = requestor
        self.notes = notes
        self.equipment = equipment
        self.ordered_by = ordered_by
        self.delivered_by = delivered_by


    def save():
        pass
    def update(self):
        pass
    def validate():
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
        locations = {
            "0": "123 Fake Street",
            "1": "456 Fake Street",
        }
        return locations
    def get_moves(self):
        pass
    def get_rentals(self):
        pass
    def get_repairs(self):
        pass
    def get_reservations(self):
        pass

def get_customer_data(customerID): 
    doc = db.collection('customerList').document(customerID).get()
    return doc.to_dict()

def get_customers_select():
    doc_list = []
    doc_list.append(('add', '+ New Customer'))
    docs = db.collection('customerList').stream()
    for doc in docs:
        doc_data = {}
        doc_data['id'] = doc.id
        doc_data['name'] = doc._data['name']
        formedData = (doc_data['id'], doc_data['name'])
        doc_list.append(formedData)
    doc_list.sort(key=lambda x: x[1])
    doc_list.insert(0,('', 'Select Customer'))
    return doc_list

def get_locations_select(customerID=None):
    if customerID != None:
        locationList = []
        customerData = db.collection('customerList').document(customerID).get().to_dict()
        customerName = customerData['name']
        try:
            for data in customerData['locations']:
                locationList.append(data)
        except:
            pass
        return locationList, customerName


    return None

def get_reservations():
    docs = db.collection('reservations').stream()
    doc_list = []
    for doc in docs:
        doc_data = doc.to_dict()
        doc_data['id'] = doc.id
        doc_data['doc_data'] = doc._data
        doc_list.append(doc_data)

    return doc_list

def create_location(data):
    pass

def create_customer(data):
    pass

def create_move(data):
    pass

def create_rental(data):
    pass

def create_repair(data):
    pass

def create_reservation(data):
    pass


   