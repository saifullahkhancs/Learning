function multiplyby5(num) {
    return num * 5;
}


multiplyby5.power = 2;

// . is used to access the properties of an object and also to add new properties to an object
// this is due to concept that everything in javascript is an object, even functions are objects, so we can add properties to functions as well
// we can also add methods to functions as well, because functions are objects, we can add methods to them as well

console.log(multiplyby5(10)); // this will log 50
console.log(multiplyby5.power); // this will log 2
console.log(multiplyby5.prototype); // this will log the prototype of the function which is an object





function createUser(username, score) {
    this.username = username;
    this.score = score;
}


createUser.prototype.increaseScore = function() {
    this.score += 10;
};


createUser.prototype.printScore = function() {
    console.log(this.score);
};



// **** new importance ****

// new will create a new object instance and assign the this keyword to that object, so when we call the increaseScore method on the chai object, 
// it will increase the score of the chai object and not the tea object

const chai = new createUser("Chai", 50);
const tea = new createUser("Tea", 60);

chai.increaseScore();
chai.printScore();
tea.printScore();


// this is how we can create multiple objects using the same constructor function and also add methods to the constructor function using the prototype property, so that all the objects created using that constructor function can access those methods.
// so we can using the oop concept to create multiple objects and also add methods to those objects using the prototype property of the constructor function.


// Q:-  why we are not using the class syntax to create objects and methods??

// Answer:-  class syntax is just a syntactical sugar over the constructor function and prototype, it is not a new way of creating objects and methods,
//  it is just a more convenient way of creating objects and methods, it is easier to read and write, but under the hood it is still using the constructor function and prototype to create objects and methods.
 

// *** A new object created

// A new keyword is used to create an instance of a constructor function, 
// it creates a new object and assigns the this keyword to that object, 
// so that we can access the properties and methods of that object using the this keyword.


// *** A prototype is linked

// When we create a new object using a constructor function, 
// the new object is linked to the prototype of the constructor function,
// so that we can access the properties and methods of the prototype using the new object, 
// this is how we can add methods to the constructor function using the prototype property, so that all the objects created using that constructor function can access those methods.


// *** The constructor is called

//  When we create a new object using a constructor function,
//  the constructor function is called with the new object as the this keyword,
//  so that we can initialize the properties of the new object using the constructor function,
//  this is how we can create multiple objects using the same constructor function and also add methods to the constructor function using the prototype property, so that all the objects created using that constructor function can access those methods.



// ** the new object is returned

// When we create a new object using a constructor function,
// the new object is returned by default, so we don't need to explicitly return the new object from the constructor function,
// this is how we can create multiple objects using the same constructor function and also add methods to the constructor function using the prototype property, so that all the objects created using that constructor function can access those methods.




