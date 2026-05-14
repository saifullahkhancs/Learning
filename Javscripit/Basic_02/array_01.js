// array 
// array is a data structure that can hold multiple values at once.
// array is a non-premitive data type because it is an object that can have properties and methods.

const myArray = [1, 2, 3, 4, 5]; // it is an array literal, it is a non-premitive data type because it is an object that can have properties and methods.

// ********** array copy operation ***********
// when we assign an array to another variable, it creates a reference to the same array in memory, 
// which means that if we change the value of one variable, it will also change the value of the other 
// variable because they are both referencing the same array in memory.


const myArray2 = myArray; // this creates a reference to the same array in memory



// Array Methods


myArray.push(6); // it will add the value 6 to the end of the array, 
// it modifies the original array because it is a non-premitive data type that is stored in heap.

myArray.pop(); // it will remove the last value from the array, it modifies the original array because it is a non-premitive data type that is stored in heap.

myArray.shift(); // it will remove the first value from the array, it modifies the original array because it is a non-premitive data type that is stored in heap.

myArray.unshift(0); // it will add the value 0 to the beginning of the array, it modifies the original array because it is a non-premitive data type that is stored in heap.


const newStringArray = myArray.join(","); // it will return a string that is the concatenation of all the values in the array, separated by the specified separator (in this case, a comma). It does not modify the original array because it returns a new string.


// slice and splice 

const myNewArray1 = myArray.slice(1, 4); // it will return a new array that is a subset of the original array, based on the specified start and end indices.
//  It does not modify the original array because it returns a new array.

const myNewArray2 = myArray.splice(1, 3); // it will remove the values from index 1 to index 3 (not including index 3) from the original array and return a new array that contains the removed values.
//  *****It modifies the original array***** because it removes the values from the original array.

// splice include the end index while slice does not include the end index, it is important to keep this in mind when using these methods to avoid unexpected results.
