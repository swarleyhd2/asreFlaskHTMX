const locationSelection = document.getElementById('location');
const customerSelection = document.getElementById('customer');


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
    document.querySelector('.customerID-input').value = customerSelection.value;
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
function formChange(htmxtarget) {
    let currentTab = document.querySelector('[aria-selected=true]')
    currentTab.setAttribute('aria-selected', 'false')
    currentTab.classList.remove('active')
    let newTab = htmxtarget
    console.log(newTab)
    newTab.setAttribute('aria-selected', 'true')
    newTab.classList.add('selected')
    newTab.classList.add('active')
    document.querySelector('.customerID-input').value = customerSelection.value;
}
