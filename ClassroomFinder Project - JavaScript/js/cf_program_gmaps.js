/* JS file for cf_program.html - Ronan Wallace */

/* This code, when exceuted, will ask for the user's class (in the form of an item number) and then display the location and summary of that class. */


// INFORMATION ARRAYS //
// buildingLocation array is a multidimensional array that contains a building name and its corresponding GPS coordiates.
var buildingLocation=[['BHL (Bauer Hall)',45.632874,-122.652795],['FAC (Frost Arts Center)',45.634716,-122.653792],['FHL (Foster Hall)',45.635111,-122.652330],['HHL (Hanna Hall)',45.635468,-122.652514],['JSH (Joan Stout Hall)',45.632984,-122.650635],['SBG (STEM)',45.637844,-122.650356],['SCI (Science Building)',45.634163,-122.650691],['SHL (Scarpelli Hall)',45.634333,-122.651987]];
// classToBuilding array is a multidimensional array that contains a building name and the class numbers that are located in that building.
var classToBuilding=[['BHL (Bauer Hall)',0000],['FAC (Frost Arts Center)',1000],['FHL (Foster Hall)',2000],['HHL (Hanna Hall)',3000],['JSH (Joan Stout Hall)',4000],['SBG (STEM)',5000],['SCI (Science Building)',6000],['SHL (Scarpelli Hall)',7000]];
// itemNumberToClassInfo array is a multidimensional array that contains a class number and key information that corresponds to that class.
var itemNumberToClassInfo=[[0000,"Calculus I","Marci Bohac",124],[1000,"Painting I","Grant Hottle",205],[2000,"Sociology II","Carlos Castro",122],[3000,"American and National Government","Michael Ceriello",118],[4000,"Lifespan Psychology","Mika Maruyama",120],[5000,"General Chemistry with Lab","April Mixon",309],[6000,"Environmental Biology","Caroline Swansey",111],[7000,"Javascript","Bruce Elgort",125]];



// CREATES MAP //
// Creates an undefined variable of "map"
var map;
// Using the Maps Javascript API, a map is created and display in the empty div with the id of "map". The map is centered on Clark College and has a zoom of 16.9. The map type is set to a hybrid of satellite imaging and addresses.
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 45.6352086, lng: -122.653381},
    zoom: 16.9,
    mapTypeId: 'hybrid'
    });
}
 


// WHEN THE DOCUMENT IS READY, PERFORM A SERIES OF FUNCTIONS //
$(document).ready(function(){
    // Grabs the form element with the id of "formBlock" and performs an anonymous function when the submit button is clicked.
    $('#formBlock').submit(function(evt){
        // Prevents the submit button, when clicked, from refreshing the page.
        evt.preventDefault();
        // Assigns the user input in the textbox to a variable of "classNumber". This input is key information to identify what class is being located.
        var classNumber=$('#classNumber').val();
        // Calls the updateMap function passing in the user input as a parameter. The returned value is an array containing the building name, the latitude coordinate, and the longitude coordinate.
        var classInfoArray=updateMap(classNumber);
        // Calls the classInfoEdit function and passes in two parameters of the classNumber and the previously defined classInfoArray. The returned value is an array containing the building name, latitude coordinate, longitude coordinate, class title, class instructor, and room number.
        var classInfoArray2=classInfoEdit(classNumber,classInfoArray);
        // Calls the classDisplay function, passing in the classNumber and previously defined classInfoArray2. This injects a summary of the class information into an emptied div for the user to review.
        classDisplay(classNumber,classInfoArray2);
    });
});



// UPDATES MAP MARKER //
// Creates an initial "marker" variable
var marker;

function updateMap(classNumber){
    // If the marker variable is defined, use the setMap() method to set the marker to null. This will delete the previously placed marker on the map.
    if (marker!=undefined){
        marker.setMap(null);
    }
    // Calls the coordGrabber function, passing in the class number as a parameter. Returns an array containing the building name and it's corresponding coordinates.
    var coordinates=coordGrabber(classNumber);
    // Creates a new marker and sets the position to the retrieved coordinates and sets the title as well.
    marker = new google.maps.Marker({
        position: {lat: coordinates[1], lng: coordinates[2]},
        map: map,
        title: coordinates[0]
    });
    // Takes the previously defined marker and sets it on the map
    marker.setMap(map);
    // Returns the coordinates array
    return coordinates;
}



// GRABS COORDINATES FROM INFORMATION ARRAYS //
function coordGrabber(classNumber){
    // An error variable is defined to catch if the user gave an input that is not a valid class number.
    var errCount=0;
    // Initial buildingName is created as undefined 
    var buildingName;
    // Nested loops are used to find the building that the class is located in (Iterates through classToBuilding array).
    for (let i=0;i<classToBuilding.length;i++){
        for (let j=0;j<classToBuilding[i].length;j++){
            // Iterates through the classToBuilding multidimensional array, and when the class number is located, the corresponding class building is grabbed.
            if (classNumber==classToBuilding[i][j]){
                var buildingName=classToBuilding[i][0];
                break;
            // ERROR COUNTER //
            // For every value that is not equal to the class item number, add one to the first error counter.
            } else if (classNumber!=classToBuilding[i][j]) {
                errCount=errCount+1;
                // If the error counter reaches the maximum values in the array, then an error will be displayed and reset any information.
                if (errCount==classToBuilding.length*2){
                    alert("Oops! No class with that item number. Please enter a valid class item number.");
                    $('#classInfo').empty().append("<h2 id='classInformation'>Class Information:</h2><p>No information to display.</p>");
                }
            } else {
                continue;
            }
        }
        // Stops loop after buildingName is defined.
        if (buildingName!=undefined){
            break;
        }
    }
    // Finds the building name and its corresponding coordiantes (Iterates through the buildingLocation array).
    for (let i=0;i<buildingLocation.length;i++){
        // When the building location array is located, that specific array is assigned to the defined variable. The array is then returned and the loop stops.
        if (buildingName==buildingLocation[i][0]){
            var coordArray=buildingLocation[i];
            return coordArray;
            break;
        } else {
            continue;
        }
    }
}



// INJECTS CLASS INFORMATION INTO EMPTY DIV //
function classDisplay(classNumber,classInfo2){
    // Empties the element with the id of "classInfo" and then appends information of the class into that element. This creates a summary of the class that the user is wanting to find.
    $('#classInfo').empty().append("<h2 id='classInformation'>Class Information:</h2><p>Item Number: #"+classNumber+"<br>Class: "+classInfo2[3]+"<br>Instructor: "+classInfo2[4]+"<br>Location: "+classInfo2[0]+"<br>Room Number: #"+classInfo2[5]);
}



// ADDS KEY CLASS INFO INTO ARRAY //
function classInfoEdit(classNumber,classInfoArray){
    // Iterates through the itemNumberToClassInfo array that contains specific information regarding the class (title, instructor, and room number).
    for (let i=0;i<itemNumberToClassInfo.length;i++){
        // If the class number is equal to the 0th index position of one of the arrays, take the rest of the information in that array and push it into the classInfoArray using the push() method. This array now contains the building name, the building coordiantes, class title, instructor, and room number.
        if (itemNumberToClassInfo[i][0]==classNumber){
            classInfoArray.push(itemNumberToClassInfo[i][1],itemNumberToClassInfo[i][2],itemNumberToClassInfo[i][3]);
            return classInfoArray;
        }
    }
}