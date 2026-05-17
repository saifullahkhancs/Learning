// console.log("2">1)
// console.log("02">1)

// in the first case it will return true because it will convert the string "2" to the number 2 and then compare it with 1



// we avoid the below comparisons because they can lead to unexpected results due to type coercion in javascript, 
// it is always better to use strict equality operator (===) instead of loose equality operator (==) to avoid such issues.

console.log(null > 0)
console.log(null == 0)
console.log(null >= 0)

// in the first case it will return false because null is considered as 0 in number conversion and 0 is not greater than 0
// in the second case it will return false because null is not equal to 0
// in the third case it will return true because null is considered as 0 in number conversion and 0 is greater than or equal to 0


// comparison and equality operators in javascript can be confusing because of type coercion, it is always better to use strict
//  equality operator (===) instead of loose equality operator (==) to avoid unexpected results.


console.log(undefined > 0)
console.log(undefined == 0)
console.log(undefined >= 0) 


// in the first case it will return false because undefined is considered as NaN in number conversion and NaN is not greater than 0
// in the second case it will return false because undefined is not equal to 0
// in the third case it will return false because undefined is considered as NaN in number conversion and NaN is not greater than or equal to 0





// ****** Strict checking of equality ******

console.log(0 === false) // it will return false because 0 is a number and false is a boolean, they are of different types

console.log("" === false) // it will return false because "" is a string and false is a boolean, they are of different types   

console.log(null === undefined) // it will return false because null is a primitive data type and undefined is also a primitive data type, but they are of different types

console.log(null === null) // it will return true because both null are of the same type and have the same value



