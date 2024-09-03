const fruits = ["Banana", "Orange", "Apple", "Mango"];
console.log(fruits);
console.log(fruits.toString());
console.log(fruits.length);
console.log(fruits.sort())

for (let i=0 ; i < fruits.length; i++ ) {
    console.log(fruits[i]);
}

//  The join() method also joins all array elements into a string
console.log(fruits.join(""))
console.log(fruits.join("***"))  // add 3 stars with each element

fruits.push("grapes"); // to add element to the array

fruits.push("random");

fruits.pop(); 


fruits.shift(); // The shift() method removes the first array element and "shifts" all other elements to a lower index.

fruits.unshift("random");   // The unshift() method returns the new array length:


const myGirls = ["Cecilie", "Lone"];
const myBoys = ["Emil", "Tobias", "Linus"];

const myChildren = myGirls.concat(myBoys);   // The concat() method creates a new array by merging (concatenating) existing arrays:

// The concat() method does not change the existing arrays. It always returns a new array.

const arr1 = ["Emil", "Tobias", "Linus"];
const arr1plus = arr1.concat("Peter"); 

console.log(arr1plus)

fruits.splice(2, 0, "Lemon", "Kiwi");  // The splice() method adds new items to an array
// this will add 2 elements and remove nothing  

// With clever parameter setting, you can use splice() to 
//remove elements without leaving "holes" in the array:

fruits.splice(0, 1);

// this will add nothong but remove the 1 element and it works as shift


const citrus = fruits.slice(1);

// The slice() method creates a new array.
// **** The slice() method does not remove any elements from the source array.  ****

citrus.push(fruits.slice(1, 3));  // slice the elements between 1 and 3 and create a new array 
console.log(citrus);
