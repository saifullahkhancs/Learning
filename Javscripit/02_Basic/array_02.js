const marvel_heroes = ["thor", "iron man", "hulk", "captain america"];

const dc_heroes = ["superman", "batman", "wonder woman", "flash"];


const new_array = marvel_heroes.push("black widow"); // it will add "black widow" to the end of the marvel_heroes array
// push will add the array completely instead of adding the element to the end of the array, it will add the entire array as a single element to the end of the marvel_heroes array, which is not what we want. To add an element to the end of an array, we should use the push() method with the element as an argument, like this: marvel_heroes.push("black widow").
console.log(marvel_heroes) // it will return ["thor", "iron man", "hulk", "captain america", "black widow"]
console.log(new_array) // it will return 5 because the push() method returns the new length of the array after adding the new element.

const new_array2 = marvel_heroes.concat(dc_heroes); // it will return a new array that is the concatenation of the marvel_heroes and dc_heroes arrays, it does not modify the original arrays because it returns a new array.

console.log(new_array2) // it will return ["thor", "iron man", "hulk", "captain america", "black widow", "superman",

// simple way of concate instead of assiging doesnot change the actual
// so concate return the new array without modifying so we need to assign it



const some_array = [1, 2, 3, [4, 5, 6 , [7, 8, 9 ] ] ] ;

const flattened_array = some_array.flat(2); // it will return a new array that is a flattened version of the original array, with a depth of 2. It does not modify the original array because it returns a new array.

console.log(flattened_array) // it will return [1, 2, 3, 4, 5, 6, 7, 8, 9] because the flat() method flattens the nested arrays in the original array up to the specified depth (in this case, 2), and returns a new array with all the values in a single level. In this case, it flattens the nested arrays [4, 5, 6] and [7, 8, 9] into a single level array.

const flattened_array2 = some_array.flat(Infinity); // it will return a new array that is a flattened version of the original array, with an infinite depth. It does not modify the original array because it returns a new array.

console.log(flattened_array2) // it will return [1, 2, 3, 4, 5, 6, 7, 8, 9] because the flat() method flattens the nested arrays in the original array up to the specified depth (in this case, Infinity), and returns a new array with all the values in a single level. In this case, it flattens all the nested arrays in the original array into a single level array.




// isArray

