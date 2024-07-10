// The spread (...) and rest (...) operators are powerful features
//  introduced in JavaScript (ES6) for working with arrays and 
//  function parameters. They have similar syntax but are used 
//  in different contexts, and their behavior depends on how 
//  and where they are used.

//        *********Spread Operator (...)*************

// The spread operator is used to expand an 
// iterable (like an array or string) into individual elements.


//  ########Copying Arrays:
// You can use the spread operator to create a shallow copy of an array:
//  shallow  copy changes doesnot reflect to the main array but
// deep copy changes may show in the main array
const orgArray= [1,2,3]
const copiedArray = [...orgArray]
console.log(copiedArray);
orgArray.push(6)
console.log(orgArray)
console.log(copiedArray);


//   ######   concateing array

const array1 = [1, 2, 3];
const array2 = [4, 5, 6];
const concatArray = [...array1, ...array2];
console.log(concatArray);


//  #### Passing the argument to function

const sum = (a,b,c) => a+b+c;

const numbers = [1, 2, 3];
const result = sum(...numbers)
console.log(result);



// ********************   Rest Operator ****************
// The rest parameter is used in function parameter lists to collect a
//  variable number of arguments into an array. It allows you to work
//   with an arbitrary number of arguments as an array:

function summ(...numberr) {
    return numberr.reduce((total, num) => total + num, 0);
}

console.log(summ(4, 5, 6, 7, 8)); // 30

function length(...alphabets) {
    return alphabets.length;
}

console.log(length("a","b","c","f"));




// The spread operator is used to split an iterable (e.g., an array) 
// into individual elements.
// The rest parameter is used in function parameter 
// lists to collect a variable number of arguments into an array.