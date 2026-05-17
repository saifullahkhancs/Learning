const person = {
  name: "John",
  age: 30,
  city: "New York"
};

// accessing the objects

console.log(person.name); // "John"
console.log(person["age"]); // 30

// Adding and Modyfing Property

person.job = "Engineer"  // adding the new property
person.age = "34"   // modying existing properties

// Deleting properties
// You can remove properties from an object using the delete

delete person .city;

// Iterating Over Object Properties:

for (let key in person) {
    console.log(key + ": " + person[key]); 
}

/// checking if a property 

if (person.hasOwnProperty("name")){
    console.log("Property exists")
}

/// Object Methods

const car = {
  brand: "Toyota",
  start: function() {
    console.log("Engine started");
  }
};
car.start(); // "Engine started"

////    Object Destructuring

const { name, age } = person;
console.log(name); // "John"
console.log(age); // 31
