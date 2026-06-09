

function SetUserName(username) {
    // complex db calls
    this.username = username;
}


function createUser(username, score ,email) {
    
    // SetUserName(username);   // this will call actually it just pass the reference mean its references is passed and it is called
    // when it is called it is removed from the executional context and it is added to the call stack and when it is executed it is removed from the call stack and it is added to the executional context, so that we can access the properties of the SetUserName function in the createUser function, so that we can set the username property of the chai object, so that we can access it using the chai object.
    SetUserName.call(this, username); // this will call the SetUserName function and pass the this keyword of the createUser function to the SetUserName function, so that we can set the username property of the chai object, so that we can access it using the chai object.

    this.score = score;
    this.email = email;

}


// **********  this and call passing the executional context ************
// when we call the SetUserName function inside the createUser function,
//  it is called with the this keyword of the createUser function, 
// so that we can set the username property of the chai object, 
// so that we can access it using the chai object, so that we can share information between these objects.

const chai = new createUser("Chai", 50, "chai@example.com");
console.log(chai.username);      // this will not work because the username property is not defined in the createUser function, 
// it is defined in the SetUserName function, so we need to call the SetUserName function 
// inside the createUser function to set the username property of the chai object, so that we can access it using the chai object.


// interview question:- Why we use call and how we use this with it?

// Answer:-  call is a method that is used to call a function with a given this value and arguments provided individually, 
// it is used to set the this keyword of a function to a specific value, 
// so that we can access the properties of that value using the this keyword in the function, 
// so that we can share information between these objects.












