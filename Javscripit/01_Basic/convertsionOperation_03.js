let score = null

console.log(typeof score);
console.log(typeof(score));

let valueInNumber = Number(score); // it will convert the string "33" to the number 33

console.log(typeof valueInNumber);
console.log(valueInNumber);



// for simple 33 it will convert to number 33 
// but for "33abc" it will return NaN because it cannot convert the string to a number
// for null it will convert to 0 because null is considered as 0 in number conversion
// for undefined it will convert to NaN because undefined cannot be converted to a number
// for true it will convert to 1 and for false it will convert to 0 because in boolean conversion 
// true is considered as 1 and false is considered as 0



let isLoggedIn = 1

let booleanIsLoggedIn = Boolean(isLoggedIn); // it will convert the number 1 to true because in boolean conversion

console.log(typeof booleanIsLoggedIn);
console.log(booleanIsLoggedIn);

// for 0 it will convert to false because in boolean conversion 0 is considered as false
// "" => false
// " " => true because it is not an empty string
// null => false
// undefined => false
// NaN => false



//   **************** Operations in JavaScript ****************

let value = 3

let negativeValue = -value; // it will convert the number 3 to -3

console.log(negativeValue);


console.log(2+2)
console.log(2-2)
console.log(2*2)
console.log(2/2)
console.log(2%2) // it will return the remainder of the division, in this case it will return 0 because 2 is divisible by 2
console.log(2**3) // it will return 8 because it is 2 to the power of 3


console.log("2"+1)
console.log(1+"2")

console.log("2" + 2 + 1) // it will return "221" 
                        // because it will first concatenate the string "2" with the number 2 to get "22" and then it will concatenate the string "22" with the number 1 to get "221"

console.log(2 + 1 + "2") // it will return "32" because it will first add 2 and 1 to get 3 and then it will concatenate the string "2" to get "32"


console.log(+true) // it will return 1 because in number conversion true is considered as 1
console.log(+false) // it will return 0 because in number conversion false is considered as 0

console.log(+"") // it will return 0 because in number conversion an empty string is considered as 0

let num1 , num2, num3


// this is not good behaviour so avoid this
num1 = num2 = num3 = 2 + 2 // it will assign the value 4 to num1, num2 and num3 because the expression 2 + 2 
// will be evaluated first and then the result will be assigned to num1, num2 and num3


gameCounter = 100

gameCounter++

console.log(gameCounter); // it will return 101 because the post-increment operator will first return the value of gameCounter and then it will increment the value of gameCounter by 1


// prefix increment operator will first increment the value of gameCounter by 1 and then it will return the value of gameCounter

// post-increment operator will first return the value of gameCounter and then it will increment the value of gameCounter by 1
gameCounter = 100

gameCounter--

console.log(gameCounter); // it will return 99 because the post-decrement operator will first return the value of gameCounter and then it will decrement the value of gameCounter by 1



