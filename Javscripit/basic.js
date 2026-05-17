//  1:-               variablesss
let name;
console.log(name);

let interestrate= 0.3;  
// value can be changed
interestrate = 1;
console.log(interestrate);

const interestrat= 0.3;  
// const value can not be reassigned and change
// interestrat = 1; // it generate the error
//  console.log(interestrat);

// 2:- jvasciript has 2 data types
//         Primmitive and Reference (objects , array ,function )
         
// Primitive and Value Types

let names = 'ali'            // String Literal
let age =30;                  // Number Literal
let isApproved = false;       // Boolean literal
let firstName = undefined;   // undefined literal
let selectedColor = null;     // null literal

console.log(typeof names);
names = 1                      // javasciript is a dynamic launguage
console.log(typeof names);     // so its type is changed

console.log(typeof firstName);   // undefined is also value
// and it is also a tyoe


console.log(typeof selectedColor);   // it is an object

///  ===>>>>>>>> Reference Data typess
//              =====1 Objects====

//  {} the paranthesis is called object literals 

let person = {
    name: 'ali',
    age: 30,
};
console.log(person)

//                       acessing the value and change it
// 1 => Dot notation
person.name = 'mee'
console.log(person.name)


// 2 => bracket notation
person['name'] = 'jhon'
console.log(person['name'])

//              ==== 2 Arrays ====
// length of array and type of array can be changed as java is dynamoc launguage
let selectedColors = ['red','green']
console.log(selectedColors)
console.log(selectedColors[1])

selectedColors[2] = 'yellow'

// unlike other launguages arrays javascripta arrays can store diffenet data types

selectedColors[3] = 1
console.log(selectedColors)
console.log(typeof(selectedColors))

// array is an object in javascript
// build in properties of the array
console.log(selectedColors.length)


///                        ========= 3 Function =======

function greet(name_param , lastname)  {           // <<== here it is called parameter
    console.log("hello" +" " + name_param , lastname);  // <<lastname== undefined
}
//   last name do  not assigned any value then it is undefined

greet('ali')    // <<=== Argument is actual value passed
greet('mee' , 'khan')


