const name = "saif";
const repoCount = 50;

// console.log(name + " has " + repoCount + " repositories.");

// this is outdated way 

// we use backticks (``) to create template literals, which allow us to embed expressions inside string literals using ${} syntax.

console.log(`Hello my name is ${name} has ${repoCount} repositories.` );

// it is also called string interpolation, it is a more modern and convenient way to create strings that include variables and expressions. It makes the code more readable and easier to maintain.


const gameName = new String("The Legend of Zelda");

console.log(gameName) // it will return [String: 'The Legend of Zelda'] because it is an object created using the String constructor function, it is not a primitive string value.

// it is generally recommended to use string literals (e.g. "Hello") instead of the String constructor function (e.g. new String("Hello")) to create strings in JavaScript, 
// because string literals are more concise and easier to read, and they also have better performance than string objects created with the String constructor function.

// it is return as object and we can apply methods on it, but it is not recommended to use string objects created with the 
// String constructor function because they can lead to unexpected behavior and performance issues. It is better to use string literals for creating strings in JavaScript.

// values of the string are in the key value pair and the keys are the index of the characters in the string and the values are the characters themselves.


console.log(gameName[0]) 


console.log(gameName.__proto__)
// the __proto__ property is a reference to the prototype of the object, which is an object that contains properties and methods that are inherited by all instances of that object. In this case,
//  it will return the prototype of the String object, which contains methods like length, toUpperCase, toLowerCase, etc. that can be used on string objects.

console.log(gameName.length) // it will return 21 because the length property of a string object returns the number of characters in the string, including spaces and special characters. In this case, "The Legend of Zelda" has 21 characters.

console.log(gameName.toUpperCase()) // it will return "THE LEGEND OF ZELDA" because the toUpperCase() method of a string object returns a new string with all characters converted to uppercase. In this case, it converts "The Legend of Zelda" to "THE LEGEND OF ZELDA".

console.log(gameName.toLowerCase()) // it will return "the legend of zelda" because the toLowerCase() method of a string object returns a new string with all characters converted to lowercase. In this case, it converts "The Legend of Zelda" to "the legend of zelda".


console.log(gameName.charAt(0)) 
// it will return "T" because the charAt() method of a string object returns the character at the specified index. 
// In this case, it returns the character at index 0, which is "T".


console.log(gameName.indexOf("e"))


const subString = gameName.substring(0, 3) // it will return "The" because the substring() method of a string object returns a new string that is a subset of the original string, based on the specified start and end indices.

console.log(subString)


const anotherString = gameName.slice(4, 10) // it will return "Legend" because the slice() method of a string object returns a new string that is a subset of the original string, based on the specified start and end indices. The slice() method is similar to the substring() method, but it can also accept negative indices to count from the end of the string.

const NegativeSlice = gameName.slice(-6)  // it will return "Zelda" because the slice() method can accept negative indices to count from the end of the string. In this case, it returns the last 6 characters of the string, which is "Zelda".
console.log(NegativeSlice)

const anotherNegativeSlice = gameName.slice(-6, -1) // it will return "Zeld" because the slice() method can accept negative indices to count from the end of the string. In this case, it returns the characters from index -6 to index -1, which is "Zeld".

console.log(anotherNegativeSlice)


// **** imp  ****

// we can not use negative in the substring() method because it does not accept negative indices, it will treat them as 0 and return the entire string.

const anotherNegativeSubstring = gameName.substring(-6, -1) // it will return "The Legend of Zelda" because the substring() method does not accept negative indices, it will treat them as 0 and return the entire string.

console.log(anotherNegativeSubstring)


// trim method is used to remove whitespace from both ends of a string. It does not modify the original string, but returns a new string with the whitespace removed.

const stringWithWhitespace = "   Hello, World!   ";
const trimmedString = stringWithWhitespace.trim();

console.log(trimmedString) // it will return "Hello, World!" because the trim() method removes the whitespace from both ends of the string, but it does not modify the original string. In this case, it returns a new string with the whitespace removed, which is "Hello, World!".


// replace method is used to replace a specified value with another value in a string. It does not modify the original string, but returns a new string with the specified value replaced.

const originalString = "The quick brown fox jumps over the lazy dog.";
const newString = originalString.replace("fox", "cat");






