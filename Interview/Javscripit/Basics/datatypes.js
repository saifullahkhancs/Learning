"use strict"; // treat all js code as newer version
// if we do not use strict mode, it will not throw an error 
// when we assign a value to an undeclared variable, but in strict mode it will throw an error

// alert(3 + 4); // we are using node js not browser, so alert will not work, it will throw an error
console.log(3 + 4); // use console.log instead of alert to print output in node js


console.log("Hello, World!");  console.log("ali");

// it will work but it is not recommended to write multiple statements in one line because it 
// reduces readability and can lead to confusion for other developers who may read the code in the future. 
// It is better to write each statement on a new line for better readability and maintainability of the code.



// mdn and tc39 are good resources to learn about javascript and its features.


let name = "John Doe"; // it is string data type
let age = 30; // it is number data type
let isStudent = true; // it is boolean data type


// premitive data types in javascript are:

// number => range is 2 to power 53
// bigint => range is 2 to power 1024
// string => sequence of characters , ""
// boolean => true or false
// null => represents the intentional absence of any object value
           // it is standalone value and has a type of its own
// undefined => represents the value of a variable that has not been assigned a value
              // it is also a standalone value and has a type of its own
// symbol => represents a unique identifier, it is used to create unique property keys for objects


console.log(typeof null); // it will return "object" because of a bug in javascript, but it is actually a primitive data type
console.log(typeof undefined); // it will return "undefined" because it is a primitive data type




