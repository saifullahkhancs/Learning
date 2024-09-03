// The JavaScript Math object allows you to perform mathematical tasks on numbers.


// Unlike other objects, the Math object has no constructor.
// The Math object is static.
// All methods and properties can be used without creating a Math object first

// Math Properties (Constants)
// The syntax for any Math property is : " Math.property "


Math.E        // returns Euler's number
Math.PI       // returns PI
Math.SQRT2    // returns the square root of 2
Math.SQRT1_2  // returns the square root of 1/2
Math.LN2      // returns the natural logarithm of 2
Math.LN10     // returns the natural logarithm of 10
Math.LOG2E    // returns base 2 logarithm of E
Math.LOG10E   // returns base 10 logarithm of E


// #################################

// Math Methods
// The syntax for Math any methods is : Math.method(number)


// Math.round(x)	Returns x rounded to its nearest integer
console.log(Math.round(6.4))

// Math.ceil(x)	Returns x rounded up to its nearest integer

console.log(Math.ceil(6.4))

// Math.floor(x)	Returns x rounded down to its nearest integer
console.log(Math.floor(6.4))

// Math.trunc(x)	Returns the integer part of x (new in ES6)
console.log(Math.trunc(6.4))


//Math.sign(x) returns if x is negative, null or positive:

console.log(Math.sign(-4));  // return -1   "negative value"
console.log(Math.sign(0));  // return 0    "null value"
console.log(Math.sign(4));  // return 1    "positive value "



console.log(Math.pow(4,2));

console.log(Math.sqrt(64));

console.log(Math.abs(-9.5));  // returns the absolute positive value 



// ############  random number genration concept

//   Math.random() returns a random number between 0 (inclusive),  
//     and 1 (exclusive):

console.log(Math.random());


// JavaScript Random Integers
// Math.random() used with Math.floor() can be used to return random integers.

// Returns a random integer from 0 to 10:
console.log(Math.floor(Math.random() * 11));


// Returns a random integer from 1 to 100:
Math.floor(Math.random() * 100) + 1;