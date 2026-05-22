// control flow /logic flow 
//        this means the order in which the code is executed
//        by default, the code is executed from top to bottom
//        but we can change the order of execution using control flow statements

// if statement
//        if statement is used to execute a block of code if a specified condition is true

const age = 18;
if (age >= 18) {
    console.log("You are an adult");
} else {
    console.log("You are a minor");
}

// comparison operators
//        comparison operators are used to compare two values and return a boolean value (true or false)
//        ==, it will compare the values of the two operands and return true if they are equal, it will perform type coercion if the operands are of different types, which can lead to unexpected results. For example, 0 == false will return true because 0 is considered falsy in JavaScript, and false is also considered falsy, so they are considered equal when using the == operator.
//        ===, it will compare the values and types of the two operands and return true if they are equal
//        !=, it will compare the values of the two operands and return true if they are not equal, it will perform type coercion if the operands are of different types, which can lead to unexpected results. For example, 0 != false will return false because 0 is considered falsy in JavaScript, and false is also considered falsy, so they are considered equal when using the != operator.
//        !==, it will compare the values and types of the two operands and return true if they are not equal
//        >, it will return true if the left operand is greater than the right operand
//        <, it will return true if the left operand is less than the right operand
//        >=, it will return true if the left operand is greater than or equal to the right operand
//        <=, it will return true if the left operand is less than or equal to the right operand



if  (2=="2") {
    console.log("This is true");
} else {
    console.log("This is false");
}
// it will return "This is true" because the == operator performs type coercion, which means it converts the operands to the same type before comparing them. In this case, the string "2" is converted to the number 2, and since 2 is equal to 2, the condition evaluates to true.

if  (2==="2") {
    console.log("This is true");
} else {
    console.log("This is false");
}

// it will return "This is false" because the === operator does not perform type coercion, which means it compares both the value and the type of the operands. In this case, the number 2 is not equal to the string "2" because they are of different types, so the condition evaluates to false.



// ***********short hand notation*************

//        we can use short hand notation to write shorter and cleaner code

const isAdult = age >= 18 ? "You are an adult" : "You are a minor";
console.log(isAdult) // it will return "You are an adult" because the condition age >= 18 is true, so the expression after the ? operator is returned. If the condition were false, the expression after the : operator would be returned instead.


if (age >= 18 && age < 65) console.log("You are an adult"); // it will return "You are an adult" because the condition age >= 18 && age < 65 is true, so the block of code inside the if statement is executed. If the condition were false, the block of code would not be executed and nothing would be printed to the console.



//else if statement
//        else if statement is used to specify a new condition to test, if the first condition is false
balance = 150;
if (balance > 100) {
    console.log("You have a good balance");
} else if (balance > 0) {
    console.log("You have a positive balance");
} else {
    console.log("You have a negative balance");
}


// logical operators
//        logical operators are used to combine multiple conditions and return a boolean value (true or false)
//        &&, it will return true if both operands are true
//        ||, it will return true if at least one of the operands is true
//        !, it will return true if the operand is false, and false if the operand is true





const haveBalance = true
const canBuy = true

if (haveBalance && canBuy) {
    console.log("You can buy the product");
} else {
    console.log("You cannot buy the product");
}



const googleLogin = true
const facebookLogin = false
const twitterLogin = false


if (googleLogin || facebookLogin || twitterLogin) {
    console.log("You are logged in");
} else {
    console.log("You are not logged in");
}


weekend = false

if (!weekend) {
    console.log("It's a weekday");
} else {
    console.log("It's a weekend");
}




// Nulish Coalescing Operator (??)
//        The nullish coalescing operator (??) is a logical operator that returns the right-hand side operand when the left-hand side operand is null or undefined, 
//        and otherwise returns the left-hand side operand. It is often used to provide a default value for a variable that may be null or undefined. For example:



// mostly used when the data is return from api or database and we want to provide a default value if the data is null or undefined
defaultValue = "Guest"
const userid = null;
const username = null;
const displayName = username ?? userid ?? "Guest";
console.log(displayName) // it will return "Guest" because the left-hand side operand (username) is null, so the right-hand side operand ("Guest") is returned. If username were not null or undefined, 
//                        then its value would be returned instead.


// **** ternary operator (?:) ****
//        The ternary operator (?:) is a shorthand for an if-else statement. It takes three operands: a condition, an expression to execute 
//         if the condition is true, and an expression to execute if the condition is false. For example:


const isLoggedIn = true;
const greeting = isLoggedIn ? "Welcome back!" : "Please log in.";
console.log(greeting) // it will return "Welcome back!" because the condition isLoggedIn is true, so the expression after the ? operator is returned. If isLoggedIn were false, the expression after the : operator would be returned instead.


const score = 85;
const grade = score >= 90 ? "A" : score >= 80 ? "B" : score >= 70 ? "C" : score >= 60 ? "D" : "F";
console.log(grade) // it will return "B" because the condition score >= 80 is true, so the expression after the ? operator is returned. If score were less than 80, the next condition would be evaluated, and so on until a true condition is found or the default value "F" is returned.




