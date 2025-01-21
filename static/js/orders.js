const locationSelection = document.getElementById('location');
const customerSelection = document.getElementById('customer');
const fuelPrice = document.getElementById('fuelprice');
const fuelSwitch = document.getElementById('fuelswitch');

fuelSwitch.addEventListener("click", () => {
    if (fuelSwitch.checked == true) {
        fuelPrice.setAttribute('disabled', true)
    }
    else {
        fuelPrice.removeAttribute('disabled')
    }
})

function openNewLocationModal() {
    if(locationSelection.value == "add") {
        new bootstrap.Modal(document.getElementById('newlocationmodal')).show()
    }
}

function openNewCustomerModal() {
    new bootstrap.Modal(document.getElementById('newcustomermodal')).show()
}

function locationSelectionChange(value) {
    if(!value) {
        value = "";
    }
    locationSelection.value = value;
}

function saveLocation() {

}

function loadLocations(customerID) {
    console.log(customerID)
    //Remove old options but keep the new location and selected options
    while (locationSelection.options.length > 2) {
        locationSelection.remove(2);

    }
    const optionElement = document.createElement('option');
    const optionText = document.createTextNode('New Location');
    optionElement.appendChild(optionText);
    optionElement.setAttribute('value', '0');
    locationSelection.appendChild(optionElement);
}

function customerChange() {
    console.log(customerSelection.value);
    if(customerSelection.value == "add") {
        console.log("New Customer");
        openNewCustomerModal();
    }
    else {
        loadLocations(customerSelection.value);
    }
}
function saveCustomer() {

}
function newCustomerClose(value) {
    if(!value) {
        value = "";
    }
    customerSelection.value = value;
}

