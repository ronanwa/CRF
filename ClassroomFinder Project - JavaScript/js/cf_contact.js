/* JS File for cf_contact.html - Ronan Wallace */

/* This code, when executed, will validate the feedback form and make sure that all fields are filled out before submitting */

// When the document is done loading, place the cursor focus on the first field.
$(document).ready(function(){
    $('#first').focus();
});

// Defines errorBucket with the value of an empty array.
var errorBucket=[];

// Defines variables that will help check to see if the submit button needs to be disabled or enabled.
var submitCounter=0;
// Each variable represents a different field. These variables connect the field to its own "switch"
var a='a',b='b',c='c',d='d',e='e',f='f',g='g',h='h',j='j';
var a2=true,b2=true,c2=true,d2=true,e2=true,f2=true,g2=true,h2=true,j2=true;

// Function that acts as a board of switches for every field. If a variable is set to true, then the field still needs to be filled out. Once the submit counter reaches a certain value (8 in this case), the submit button is enabled.
function submitCount(x){
    if (x==a && a2==true){
        submitCounter=submitCounter+1;
        a2=false;
    } else if (x==b && b2==true){
        submitCounter=submitCounter+1;
        b2=false;
    } else if (x==c && c2==true){
        submitCounter=submitCounter+1;
        c2=false;
    } else if (x==d && d2==true){
        submitCounter=submitCounter+1;
        d2=false;
    } else if (x==e && e2==true){
        submitCounter=submitCounter+1;
        e2=false;
    } else if (x==f && f2==true){
        submitCounter=submitCounter+1;
        f2=false;
    } else if (x==g && g2==true){
        submitCounter=submitCounter+1;
        g2=false;
    } else if (x==h && h2==true){
        submitCounter=submitCounter+1;
        h2=false;
    }
}

// Once there is a keypress in the field with the id of "first", the css reverts back to normal.
$('#first').keypress(function(){
    $('#first').css("border","1px solid #dadada");
    $('#firstErr').css('display','none');
    // Calls submitCount (with a parameter of a) to turn off the connect switch and add a value of one to the submit count. Once submit count variable reaches a value of eight, then the submit button will be enabled.
    submitCount(a);
});
// Once there is a keypress in the field with the id of "last", the css reverts back to normal.
$('#last').keypress(function(){
    $('#last').css("border","1px solid #dadada");
    $('#lastErr').css('display','none');
    // Calls submitCount function with a parameter of b
    submitCount(b);
});
// Once there is a keypress in the field with the id of "address", the css reverts back to normal.
$('#address').keypress(function(){
    $('#address').css("border","1px solid #dadada");
    $('#addressErr').css('display','none');
    // Calls submitCount function with a parameter of c
    submitCount(c);
});
// Once there is a keypress in the field with the id of "city", the css reverts back to normal.
$('#city').keypress(function(){
    $('#city').css("border","1px solid #dadada");
    $('#cityErr').css('display','none');
    // Calls submitCount function with a parameter of d
    submitCount(d);
});
// Once there is a click in the field with the id of "state", the css reverts back to normal.
$('#state').click(function(){
    $('#state').css("border","1px solid #dadada");
    $('#stateErr').css('display','none');
    // Calls submitCount function with a parameter of e
    submitCount(e);
});
// Once there is a click in the field with the id of "yes", the css reverts back to normal.
$('#yes').click(function(){
    $('#reuseErr').css('display','none');
    // Calls submitCount function with a parameter of f
    submitCount(f);
});  
// Once there is a click in the field with the id of "no", the css reverts back to normal.
$('#no').click(function(){
    $('#reuseErr').css('display','none');
    // Calls submitCount function with a parameter of f
    submitCount(f);
}); 
// Once there is a keypress in the field with the id of "feedback", the css reverts back to normal.
$('#feedback').keypress(function(){
    $('#feedback').css("border","1px solid #dadada");
    $('#feedbackErr').css('display','none');
    // Calls submitCount function with a parameter of g
    submitCount(g);
});
// Once there is a click in the field with the id of "terms", the css reverts back to normal.
$('#terms').click(function(){
    $('#termsErr').css('display','none');
    // Calls submitCount function with a parameter of h
    submitCount(h);
});


// Once the submit button is pressed in the form with the id of "contactForm", a series of if statements will go through the fields to make sure that each field is submitted before submitting the form. 
$('#contactForm').submit(function(evt){
    // If the value in the field with id of "first" is equal to an empty string (blank), add an error meesage to the errorBucket and change the css to indicate that the field is required.
    if ($('#first').val().trim()=='') {
        errorBucket.push('The first name field is required');
        $('#first').css("border","solid 3px red");
        $('#first').focus();
        $('#firstErr').css('display','inline-block');
    }
    // If the field is left blank, indicate that the field is required.
    if ($('#last').val().trim()=='') {
        errorBucket.push('The last name field is required');
        $('#last').css("border","solid 3px red");
        $('#lastErr').css('display','inline-block');
    }
    // If the field is left blank, indicate that the field is required.
    if ($('#address').val().trim()=='') {
        errorBucket.push('The address field is required');
        $('#address').css("border","solid 3px red");
        $('#addressErr').css('display','inline-block');
    }
    // If the field is left blank, indicate that the field is required.
    if ($('#city').val().trim()=='') {
        errorBucket.push('The city field is required');
        $('#city').css("border","solid 3px red");
        $('#cityErr').css('display','inline-block');
    }
    // If the field does not have a chosen value, indicate that the field is required.
    if ($('#state').val()=='-') {
        errorBucket.push('The state field is required');
        $('#state').css("border","solid 3px red");
        $('#stateErr').css('display','inline-block');
    } 
    // If the field does not have a chosen value, indicate that the field is required.
    if (!$('input:radio[name=contact]:checked').val()) {
        errorBucket.push('Select an option');
        $('#reuseErr').css('display','inline-block');
    } 
    // If the field is left blank, indicate that the field is required.
    if ($('#feedback').val().trim()=='') {
        errorBucket.push('The feedback field is required');
        $('#feedback').css("border","solid 3px red");
        $('#feedbackErr').css('display','inline-block');
    }
    // If the field is not checked, indicate that the field is required.
    if (!$('input:checkbox[name="terms"]:checked').val()) {
        errorBucket.push('Accept the terms and conditions');
        $('#termsErr').css('display','inline-block');
    } 

// There are any errors in the errorBucket array, display them for the user.
if (errorBucket.length>0) {
    // Prevents the form from being submitted and refreshing the page.
    evt.preventDefault();
    // Resets the errors by emptying the element.
    $('#errorDisplay').empty();
    // Appends a title for the errors to the element with the id of "errorDisplay".
    $('#errorDisplay').append('<h3>Please fill out the following fields:</h3>');
    // Appends an unordered list tag with the id of "errorList".
    $('#errorDisplay').append('<ul id="errorList">');
    // Iterates through the errorBucket array and takes each error message and appends it to the previously created unordered list.
    for ( var i=0; i<errorBucket.length; i++) {
        $('#errorList').append('<li>'+errorBucket[i]);
    };
    // Resets the errorBucket to an empty array.
    errorBucket=[];
    // Gets a handle to the submit button with the id of "submitButton" and disables it.
    $('#submitButton').attr("disabled", true);
    // This calls the submitChecker function every quarter of a second. It is called at this interval to be ready to enable the submit button when the user successfully fills out all of the fields.
    setInterval(submitChecker,250);
}
    
});

// This function is called to check the value of the submitCounter variable.
function submitChecker(){
    // If the submitCounter variable is greater than 7, then enable the button.
    if (submitCounter>7){
        $('#submitButton').attr("disabled", false);
    }
}