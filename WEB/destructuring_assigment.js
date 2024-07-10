// ********  Destructuring assignment***
//  is a feature introduced in ECMAScript 2015 (ES6) that allows you to 
// extract values from arrays or properties from objects and assign 
// them to variables in a concise and readable way. It simplifies
//  working with complex data structures in JavaScript.


// There are two main aspects to destructuring assignment:
//  array destructuring and object destructuring.

//      Array Destrucutring

const numbers = [1,2,3,4];
const [a ,b , c]= numbers;

console.log(a); // 1
console.log(b); // 2
console.log(c); // 3

const [m,n]= numbers;
console.log(m); // 1
console.log(n); // 2

// You can also use array destructuring to skip elements:

const [first, ,third] = numbers;
console.log(first); // 1
console.log(third); // 3


// Object Destructuring

// Object destructuring works similarly but allows 
// you to extract properties from objects

const person = {
    firstName: "Alice",
    lastName: "Smith",
    age: 30,
};

const { firstName, lastName } = person;

console.log(firstName); // "Alice"
console.log(lastName);  // "Smith"


