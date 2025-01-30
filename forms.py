from wtforms import StringField, IntegerField, SelectField, DateField, validators, HiddenField, TextAreaField, Form, FieldList, FormField, BooleanField
from flask_wtf import FlaskForm
from form_select_options import equipmentTypes, customers

class customerSelect(FlaskForm):
    customer = SelectField('Customer', choices=customers.items())

class newCustomer(FlaskForm):
    name = StringField('Name')

class newLocation(FlaskForm):
    customer = HiddenField('customerID')

class moveForm(FlaskForm):
    customer = SelectField('Customer', choices=customers.items())
    pickup = SelectField('Pickup')
    delivery = SelectField('Delivery')
    equipment = StringField('Equipment')
    date = DateField('Date', format='%m/%d/%Y', validators=[validators.InputRequired()])
    requestor = StringField('Requested By')
    notes = TextAreaField('Notes')

class equipmentTypeForm(Form):
    equipment_type = SelectField('Equipment', choices=equipmentTypes.items())
    quantity = SelectField('Quantity', choices=[1,2,3,4,5,6,7,8,9,10])
    day_rate = IntegerField('Day Rate')
    week_rate = IntegerField('Week Rate')
    month_rate = IntegerField('4 Week Rate')

class rentalForm(FlaskForm):
    customer = SelectField('Customer', choices=customers.items())
    equipment = FieldList(FormField(equipmentTypeForm), min_entries=1)
    start_date = DateField('Start Date')
    delivery = IntegerField('Delivery')
    delivery_return = IntegerField('Return')
    fill_on_return = BooleanField('Fill on Return ($7.98/G)')
    prepay_fuel = IntegerField('Fuel/Propane')
    environmental = BooleanField('Environmental Fee ($19)')
    insurance = BooleanField('Insurance 13%')
    notes = TextAreaField('Notes')


class repairForm(FlaskForm):
    customer = SelectField('Customer', choices=customers.items())

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


