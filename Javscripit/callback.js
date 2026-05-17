// Callback: A callback is a function that is passed as an argument
// to another function that executes the callback based on the result.
// They are basically functions that are executed only after a result
// is produced. Callbacks are an important part of asynchronous JavaScript.

//      basic example
  
                                 // without callbacks
function compute1(action, x, y){
    if(action === "divide"){
        return x/y
    }else if(action === "multiply"){
        return x*y
    }else if(action === "add"){
        return x+y
    }else if(action === "modulus"){
        return x%y
    }
}

console.log(compute1("divide",10,5))    // 2
console.log(compute1("multiply",10,5))  // 50
console.log(compute1("add",10,5))       // 15
console.log(compute1("modulus",10,5))   // 0

// ***********************************************************
                
                      //  with callbacks          
function divide(x,y){
    return x/y
}

function multiply(x,y){
    return x*y
}

function add(x,y){
    return x+y
}

function compute(callBack, x, y){
    return callBack(x,y)
}

console.log(compute(divide, 10, 5))    // 2
console.log(compute(multiply, 10, 5))  // 50
console.log(compute(add,10,5))         // 15


// ************************************  impppp ******************************

//  The most common examples of callback functions in JavaScript are 
// addEventListener, array functions (filter, map, reduce) etc

const arr = [2,3,4,6,8];
const laargnum = num=> num >3;

console.log(arr.filter(laargnum));

// In the above example for the filter function, the callback function gets 
// executed inside the filter function synchronously. Hence, 
// it is called a synchronous callback. The filter function has to wait 
// for the largeNum callback function to finish execution. Hence, 
// the callback function is also called ""blocking callbacks "" as it blocks
//  the execution of the parent function in which it was invoked.




console.log("the 1st linee");

 setTimeout( function()  {
    console.log("the 2nd linee");
    }, 3000);

console.log("the 3rd line");
