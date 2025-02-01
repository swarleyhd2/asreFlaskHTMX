function hxInterrupt(event) {
    if (customerSelection = document.getElementById('customer').value == "add") {
        event.preventDefault();
        new bootstrap.Modal(document.getElementById('newcustomermodal')).show();
    }

}
function openNewLocationModal() {
    const locationSelection = document.getElementById('rental-location');
    if(locationSelection.value == "add") {
        new bootstrap.Modal(document.getElementById('newlocationmodal')).show()
    }
}

function openNewCustomerModal() {
    const customerSelection = document.getElementById('customer');
    if(customerSelection.value == "add") {
        new bootstrap.Modal(document.getElementById('newcustomermodal')).show()
    }
}
function newCustomerClose(value) {
    if(!value) {
        value = "";
    }
    customerSelection.value = value;
}
function formChange(htmxtarget) {
    //so htmx and boostrap play well together
    let currentTab = document.querySelector('[aria-selected=true]')
    currentTab.setAttribute('aria-selected', 'false')
    currentTab.classList.remove('active')
    let newTab = htmxtarget
    newTab.setAttribute('aria-selected', 'true')
    newTab.classList.add('selected')
    newTab.classList.add('active')
}
