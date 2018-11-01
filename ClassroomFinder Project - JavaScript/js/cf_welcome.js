/* JS File for cf_welcome.html - Ronan Wallace */

/* This code, when executed, displays an image every three seconds at the top of the welcome page in a slideshow manner. */


// Creates an array that contains all of the image locations
var images=['images/clark_college_sign.jpg','images/bell_tower.jpg','images/logo.jpg'];
// Creates an initial index counter to cycle through the images array
var indexCount=0

// When the document is ready, execute the imageSwitch function every three seconds.
$(document).ready(function(){
    setInterval(imageSwitch,3000);
});

// Function that displays the images in the images Array
function imageSwitch(){
    // Grabs the image element with the id of "imageHook" and sets the source attribute to the current index position of the images array (which is the next image to display).
    $('#imageHook').attr('src',images[indexCount]);
    // When the index count reaches 2, set the value to negative one
    if (indexCount==2){
        indexCount=-1;
    }
    // After an image is displayed, add one to the current value of indexCount
    indexCount=indexCount+1;
}