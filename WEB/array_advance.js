//   forEach Method
// Purpose: Iterates over each element in an array and executes 
//  a provided function for each element.

const numbers  = [1,2,3,4,5]

numbers.forEach((number) =>{
    console.log(number);
});

// map: 
//Purpose: Creates a new array by applying a provided function to
// each element in the original array

const square= numbers.map((number)=>{
  return number**2;
});  
console.log(square);


// filter:

// Purpose: Creates a new array containing elements that meet a 
// specified condition (determined by a provided function).

const even = numbers.filter((number)=>{
  return number%2 == 0;
});  

console.log(even);