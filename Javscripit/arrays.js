 let fruits = ["apple", "banana", "orange"];
console.log(fruits , fruits[0]);

//  Adding the elemnt 

fruits.push("grape");  // adding in the Last

fruits.unshift('strawbery'); // adding at the start

console.log(fruits);

// Removing elment from the array

fruits.pop(); // remove the last element

fruits.shift(); // remove the first element

console.log(fruits);



console.log(fruits.length);


for (let n = 0; n < fruits.length; n++) {
  console.log(fruits[n]);
}

for (let i of fruits) {
    console.log(i);
}
