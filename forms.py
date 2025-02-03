from wtforms import StringField, IntegerField, SelectField, DateField, validators, HiddenField, TextAreaField, Form, FieldList, FormField, BooleanField
from flask_wtf import FlaskForm
from form_select_options import equipmentTypes, customers
from firestore_db import get_customers_select, get_locations_select
from datetime import date


class customerSelect(FlaskForm):
    customer = SelectField('Customer', choices=get_customers_select(), id="customer-select")

class newLocationForm(FlaskForm):
    customer = HiddenField('customerID', [validators.DataRequired(message="Please select a customer before adding a location")], id="new-location-customer-field")
    jobsite = StringField('Jobsite')
    address = StringField('Address', [validators.DataRequired(message="Please enter an address")])
    city = StringField('City', [validators.DataRequired(message= "Please enter a city")])
    state = SelectField('State', choices=['CT', 'MA', 'RI', 'NY'], default='CT')

class moveForm(FlaskForm):
    customer = SelectField('Customer', choices=get_customers_select(), id="customer")
    pickup = SelectField('Pickup', id="pickup", choices=get_locations_select(), validate_choice=False)
    delivery = SelectField('Delivery', id="delivery", choices=get_locations_select(), validate_choice=False)
    equipment = StringField('Equipment')
    date = DateField('Date', default=date.today)
    requestor = StringField('Requested By')
    notes = TextAreaField('Notes')

class equipmentTypeForm(Form):
    equipment_type = SelectField('Equipment', choices=equipmentTypes.items(), validate_choice=False)
    quantity = SelectField('Quantity', choices=[1,2,3,4,5,6,7,8,9,10], default=1)
    day_rate = IntegerField('Day Rate')
    week_rate = IntegerField('Week Rate')
    month_rate = IntegerField('4 Week Rate')

class rentalForm(FlaskForm):
    customer = SelectField('Customer', id="customer", choices=get_customers_select())
    location = SelectField('Location', choices=get_locations_select(), validate_choice=False)
    equipment = FieldList(FormField(equipmentTypeForm), min_entries=1)
    start_date = DateField('Start Date', id="startdate", default=date.today)
    delivery = IntegerField('Delivery', id="delivery", default=180)
    delivery_return = IntegerField('Return', id="delivery_return", default=180)
    fill_on_return = BooleanField('Fill on Return ($7.98/G)', id="fuelswitch")
    prepay_fuel = IntegerField('Fuel/Propane', id="fuelprice")
    environmental = BooleanField('Environmental Fee ($19)', id="environmentalswitch")
    insurance = BooleanField('Insurance 13%', id="insuranceswitch")
    po = StringField('Purchase Order', id="po")
    notes = TextAreaField('Notes', id="notes")


class repairForm(FlaskForm):
    customer = SelectField('Customer', choices=get_customers_select())

class newCustomerForm(FlaskForm):
    name = StringField('Name')
    address = StringField('Address')
    contactName = StringField('Contact Name')
    phone = StringField('Phone')
    email = StringField('Email')



