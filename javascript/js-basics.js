// define variables
x = 32; // global variable
var y = 10; // local variable
const z = 15; // constant, never changes
let w = 2; // declares block-scoped local var


// defining multiple var in one line
var animal1 = "cat", animal2 = "dog", animal3 = "duck";

var longMultiLineText = "This is a \
long \
sentence.";

var myString = "My string"

//----------------------------------------------------------------

// objects
var myEmptyObject = {};

var notEmptyObject = {
    "label": "value",
    "label2": "value2",
    "label3": 5
};

// adding new properties to objects (two ways)
notEmptyObject.newLabel4 = "value 4";
notEmptyObject["newLabel5"] = "value 5";

// remove property
delete notEmptyObkect.newLabel4;

// make a copy of an object safely
var object2 = JSON.parse(JSON.stringify(object1));

//----------------------------------------------------------------

// arrays (in js specifically, objects and arrays are the same)
// - order is preserved
// - keys are auto assigned as numbers starting with 0
var myArray = [];
var daysOfTheWeek = ['Sunday', 'Monday', 'Tuesday'];
var myNumbers = [0, 1, 2, 'string1', 'string2', true, false];
var counties = [
    'Belknap',
    'Strafford'
];

// example
var myObjectArray = [
    {'name': 'John', 'age': 25}, // can put objects in array
    [1, 2, 3], // can put array in array
    true,
    'random string'
];

myObjectArray[0] = "newValue";

// add a value onto the end of an array (two ways)
myObjectArray[myObjectArray.length] = "newValue";
myObjectArray.push("newValue");

// remove from end of an array
myObjectArray.pop(); // takes out last item

// delete from middle of array
// .splice(start index, # to remove)
myObjectArray.splice(2, 1) // removes the item at index 2

//----------------------------------------------------------------

// regular expressions : used when searching for patterns in text
var str1 = "This is the longest string ever.";
var str2 = "This is the shortest string ever.";
var str3 = "Is this the ting called Mount Everest?";
var str4 = "This is the Sherman on the Mount.";

// regular expression (case sensitive)
var regex = /this/;

// test : reports back true/false if "this" can be found in the strings
// using console.log() outputs to console if testing in browser
// e.g. console.log( regex.test(str1) );
regex.test(str1); // false
regex.test(str2); // false
regex.test(str3); // true
regex.test(str4); // false

// adding modifiers
var regex = /this/i; // i = case insensitive
var regex = /^this/i; // ^ = checks if value is at the BEGINNING of the variable
var regex = /this$/i; // $ = checks if value is at the END of the variable

var regex = /ever.$/i; // . = checks for ever followed by any single character
var regex = /ever\.$/i; // checks for "ever." (need an escape character for period)

//----------------------------------------------------------------

// comparisons

var one = 1, two = 2;

// strict equality + inequality (recommended to use this)
one === one; // true
one !== one; // false
one === "1"; // false

// equality + not equality (checks the same but not as strict)
one == one; // true
one != one; // false
one == "1"; // true

//----------------------------------------------------------------

// conditionals
//ex 1
var answer = window.confirm("Click OK, get true. Click cnacel, get false.");
answer;
if (answer === true) {
    console.log("You picked true.");
}
else {
    console.log("You said something else.");
}

// ex 2
var answer = window.prompt("Type YES, NO, or MAYBE. Then click OK.");
if (answer === "YES") {
    console.log("You typed YES.");
}
else if (answer === "MAYBE") {
    console.log("You typed MAYBE.");
}
else if (answer === "NO") {
    console.log("You typed NO.");
}
else {
    console.log("You didn't type any of the options.")
}

// switches
var answer = window.prompt("Type YES, NO, or MAYBE. Then click OK.");

switch(answer) {
    case "YES":
        console.log("You picked YES.");
        break;
    case "MAYBE":
        console.log("You typed MAYBE.");
        break;
    case "NO":
        console.log("You typed NO.");
        break;
    default:
        console.log("You didn't type any of the options.");
        break;
}

//----------------------------------------------------------------

// terse ifs
var cherub = "Cupid";

if (cherub === "Cupid") console.log("Cupid was the cherub.");
else console.log("Cupid was not the cherub.");

// ternary operator
var animal = "cat";
// animal = "dog";
animal === "cat"
    ? console.log("You will be a cat herder.")
    : console.log("You will be a dog catcher.");

//----------------------------------------------------------------

// sequential for loops
for (var i = 0; i < 10; i += 1) {
    console.log(i);
}

// enumerative for loops
// iterating over an array
var pageNames = [
    "Home",
    "About Us",
    "Contact Us",
    "JavaScript Playground",
    "News",
    "Blog"
];
for (var p in pageNames) {
    console.log(p, pageNames[p]);
}

// iterating over an object
var pages = {
    first: "Home",
    second: "About Us",
    third: "Contact Us",
    fourth: "JavaScript Playground",
    fifth: "News",
    sixth: "Blog"
};
for (var p in pages) {
    if (pages.hasOwnProperty(p)) {
        console.log(p, pages[p]);
    }
}

//----------------------------------------------------------------

// while
var i = 0;
while (i < 10) {
    console.log(i);
    i += 1;
}

//----------------------------------------------------------------

// functions

function myFunction() { // function with no parameters/arguments
    console.log("My");
    console.log("Function");
}

myFunction(); // call function
