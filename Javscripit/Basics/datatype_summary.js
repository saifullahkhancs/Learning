// Premitive data types

// 7 tyopes: String , Number, Boolean, null, undefined, symbol, bigint



const score= 100;
const scoreValue = 100.5;

// both are number data type in javascript, there is no separate data type for integers and floating-point numbers. 
// In javascript, all numbers are represented as 64-bit floating-point values, which means that they can represent both integers and floating-point numbers. 

const id  = Symbol("123");
const anotherId = Symbol("123");

// both id and anotherId are unique symbols, even though they have the same description "123".
// Symbols are often used to create unique property keys for objects,
// which can help to avoid naming conflicts and ensure that properties are not accidentally overwritten.


const bigNumber = 1234567890123456789012345678901234567890n; // it is a bigint data type, it can represent numbers larger than 2 to the power of 53

// BigInt is a built-in object in JavaScript that provides a way to represent whole numbers larger than 2^53 - 1, which is the largest number that can be represented by the Number data type. 
// BigInt values are created by appending "n" to the end of an integer literal, or by calling the BigInt() constructor function. 
// BigInt values can be used in arithmetic operations just like regular numbers, but they cannot be mixed with Number values without explicit conversion.




// Non-premitive data types or Reference data types

// Object, Array, Function


const heroes = ["Super  Man", "Batman", "Wonder Woman"];


let person = {
    name: "John Doe",
    age: 30,
    isStudent: true
}


// function ( ) {} simple function expression, it is a non-premitive data type because it is an object that can have properties and methods.

const  myFunction = function() {
    console.log("Hello, World!");
}



function greet(name) {
    return `Hello, ${name}!`;
}





// Javascript is a dynamically typed language, which means that we do not need to specify the data type of a variable when we declare it. The data type of a variable is determined at runtime based on the value assigned to it. This allows for flexibility in coding, but it also means that we need to be careful
//  when working with variables to avoid unexpected behavior.



