// everything with the value is the true 

console.log(Boolean(100));

console.log(Boolean(3.12));

console.log(Boolean(-15));

console.log(Boolean("Helloo"));

console.log(Boolean("false"));

console.log(Boolean(7+2-4));


// everything without the value is the false

console.log(Boolean(0));

console.log(Boolean(-0));

console.log(Boolean(""));

let x; // undefined are also false
console.log(Boolean(x));


console.log(Boolean(null));  // null is also false


let y = 10/"hello";   // NaN:- not a number is also false by nature
console.log(Boolean(y)); 