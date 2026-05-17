// syntax    const functionName = (parameters) => expression;

///                        ========= 3 Function =======

function greet(name_param , lastname)  {           // <<== here it is called parameter
    console.log("hello" +" " + name_param , lastname);  // <<lastname== undefined
}
greet('ali')    ;
greet('mee' , 'khan');



// Traditional function expression
const add = function(x,y) {
    return x+y;
};


// arrow function
const addarrow =(x,y) => x+y;
const addarrow_withbracket =(x,y) =>{ return x+y};


console.log(add(3,5));
console.log(addarrow(4,5));
console.log(addarrow_withbracket(45,67));


/// template literalsss

// Template literals, introduced in ECMAScript 2015 (ES6),
//  are a way to work with strings in JavaScript that offers
//   several advantages over traditional string literals 
//   (enclosed in single or double quotes). 
//   Template literals are enclosed in backticks (` `) instead of quotes, 
//   and they allow you to embed expressions and create multi-line strings 
//   easily. Here's how they work:


//                                **syntax**  

// You can create a template literal using backticks, and you can
//    interpolate variables or expressions within ${} placeholders:

const name = "ali";
const friend = "hamza";
var friendship = `${friend} is a friend  of ${name}`;  // donot use single quoy=tes
        // use these  " `` " not " '' " thses ..pressent above tab and they are called bickticks

console.log(friendship);      

// multi line string with template literals (` `) backticks

const multiLine = `
    This is a
    multi-line
    string using template literals.`;
console.log(multiLine);

var multilin = " This is a multi_line\nstring \n using the slash n'"

console.log(multilin);


// taged Template literal
// You can use tagged template literals to process the template string
//  with a function, allowing for advanced string manipulation and formatting.
//   This is a more advanced feature and is often used in libraries 
//   and frameworks.

function customTag(strings, ...values) {
    // Process strings and values here
}

const someValue = 42;
const processed = customTag`The value is: ${someValue}`;