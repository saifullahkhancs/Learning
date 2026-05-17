// for of 
// used to loop through the values of an iterable object, such as an array, string, map, set, etc.

cars = ["BMW", "Volvo", "Mini"];
for (let x of cars) {
  console.log(x);
}

const greeting = "Hello";
for (let x of greeting) {
  console.log(x);
}

// Map object in JavaScript is a collection of key-value pairs where the keys can be of any data type. 
// It is similar to an object, but it provides additional features such as**** maintaining the order of elements ****
// and allowing keys of any type.

const map = new Map();

map.set("name", "John");
map.set("age", 30);
map.set("isStudent", true);
//console.log(map); // it will return Map(3) {"name" => "John", "age" => 30, "isStudent" => true}
console.log(map.get("name")); // it will return "John"



for (const key of map)
{
    console.log(key); // it will return ["name", "John"] , ["age", 30] , ["isStudent", true]
}

// so we use destructuring to get key and value separately
for (const [key, value] of map)
{
    console .log(`key: ${key}, value: ${value}`); // it will return key: name, value: John , key: age, value: 30 , key: isStudent, value: true
}




// ****** important ******


for(const key in map)
{
    console.log("here iam " + key); // it will not return anything because map is not an object and for in loop is used to loop through the properties/keys of an object, including inherited properties.
}
// when did in loop is used with map object it will return the keys of the map object but when we use for of loop with map 
// object it will return the key-value pairs of the map object as an array.

// *** imp ***
// map object are iteratable and they maintain the order of elements, so we can use for of loop to iterate over the map object.
// but simple object are not iteratable and they do not maintain the order of elements, so we cannot use for of loop to iterate
// over the simple object, we have to use for in loop to iterate over the simple object.

// like

const obj = {
    name: "John",
    age: 30,
    isStudent: true
}

for (const key in obj) {
    console.log(key); // it will return name , age , isStudent
}

// if we do that both it will throw an error because simple object are not iteratable
// 1:- 
//  for (const [key, value] of obj) {
//     console.log(`key: ${key}, value: ${value}`);
// }

// 2:- 
// for (const key of obj) {
//     console.log(key);
// }    


// for in 
// used to loop through the properties/keys of an object, including inherited properties.

const programmingLanguage = [ "JavaScript", "Python", "Java", "C++" ];

for (let index in programmingLanguage) {
  console.log(index); // it will return 0 , 1 , 2 , 3
}