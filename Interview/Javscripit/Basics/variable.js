console.log('Hello, World!');


// syntax is defined by the compiler (nodejs or browser) and not by the programmer

const accountId = 12345;

let accountEmail = "user@example.com";

var accountPassword = "password123";

accountCity = "New York";

// accountId = 2   not allowed because accountId is a constant

accountEmail = "newemail@example.com";

accountPassword = "newpassword456";

// variables that are only declared but not initialized will have the value of undefined
let accountState;


// variable can be declared without var, 
// let or const but it is not recommended because it becomes a global variable and can lead to unexpected behavior
accountCity = "Los Angeles";

console.log(accountId);


// use [] to print multiple variables in a table format
console.table([accountId, accountEmail, accountPassword, accountCity, accountState]);


/* 
Prefer not to use var because of the 
issue in the block scope and function scope.
var is function scoped and can lead to unexpected behavior when used inside loops or functions.
let and const are block scoped and do not have this issue.
*/

