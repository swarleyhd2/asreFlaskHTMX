from wtforms import StringField, IntegerField, SelectField, DateField, validators, HiddenField, TextAreaField
from flask_wtf import FlaskForm
from form_select_options import equipmentTypes, customers, locations

class moveForm(FlaskForm):
    customer = HiddenField('customerID')
    pickup = SelectField('Pickup', choices=locations.items())
    delivery = SelectField('Delivery', choices=locations.items())
    equipment = StringField('Equipment')
    date = DateField('Date', format='%m/%d/%Y', validators=[validators.InputRequired()])
    requestor = StringField('Requested By')
    notes = TextAreaField('Notes')

class rentalForm(FlaskForm):
    customer = IntegerField('customerID')

class repairForm(FlaskForm):
    customer = IntegerField('customerID')

class newCustomerForm(FlaskForm):
    name = StringField('Name')
    address = StringField('Address')
    contactName = StringField('Contact Name')
    phone = StringField('Phone')
    email = StringField('Email')

class newLocationForm(FlaskForm):
    name = StringField('Name')
    address = StringField('Address')
    address2 = StringField('Address2')
    city = StringField('City')
    state = StringField('State')
    zip = StringField('Zip')
    customerName = StringField('Customer Name')


