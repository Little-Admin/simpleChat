var modal_outer = document.getElementsByClassName('modal_outer')[0];
var modal_middle = document.getElementsByClassName('modal_middle')[0];

// Forms
var FormsList = document.getElementsByTagName('form');

var usernameForm_visibility = document.getElementById('usernameForm_visibility').value;
var emailForm_visibility = document.getElementById('emailForm_visibility').value;
var passwordForm_visibility = document.getElementById('passwordForm_visibility').value;
var visibilityForms = [usernameForm_visibility, emailForm_visibility, passwordForm_visibility];

var timeZoneForm_selectedValue = document.getElementById('timeZoneForm_selected').value;

// Buttons
var buttonsList = document.getElementsByClassName('activateFormButton');
buttonsList = [].slice.call(buttonsList);

function resetForms() {
    FormsList[0].style.display = 'none';
    FormsList[1].style.display = 'none';
    FormsList[2].style.display = 'none';
    FormsList[3].style.display = 'none';
}

modal_outer.onclick = function(event){
    if (event.target == modal_middle){
        modal_outer.classList.remove('change');
    }
};


// Show Forms
function showForm(formIndex){
    FormsList[formIndex].style.display = 'block';
    modal_outer.classList.add('change');
};

var button = buttonsList[1] 
buttonsList[0].addEventListener('click', function(){
    resetForms();
    showForm(0);
});
buttonsList[1].addEventListener('click', function(){
    resetForms();
    showForm(1);
});
buttonsList[2].addEventListener('click', function(){
    resetForms();
    showForm(2);
});

buttonsList[3].addEventListener('click', function(){
    resetForms();
    showForm(3);
});

// Change Defaults Inputs Values
document.getElementById('timeZoneSelect').value = timeZoneForm_selectedValue;

window.onload = function(e){    
    // Show Current Form
    for (i in visibilityForms){
        if (visibilityForms[i] === 'True'){
            showForm(i);
            break
        }
    }
};