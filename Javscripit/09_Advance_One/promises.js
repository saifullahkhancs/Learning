
// Promises in JavaScript
// A Promise is an object that represents the eventual completion (or failure) of an asynchronous operation and its resulting value. It allows you to write asynchronous code in a more synchronous and readable manner.
// A Promise can be in one of three states:
// 1. Pending: The initial state, neither fulfilled nor rejected.
// 2. Fulfilled: The operation completed successfully, and the promise has a resulting value.
// 3. Rejected: The operation failed, and the promise has a reason for the failure.

// promises usually are used to consume asynchronous operations, such as fetching data from an API, reading files, or performing time-consuming tasks. 
// They provide a way to handle the success or failure of these operations without blocking the main thread of execution.

// but  promise can be created using the Promise constructor, which takes a function as an argument. 
// This function is called the executor function and it receives two arguments: resolve and reject. 
// You can call resolve(value) to fulfill the promise with a value, or reject(reason) to reject the promise with a reason.

// a promise usually reolve or rejcected

const promiseOne = new Promise(function(resolve, reject) {
            // we can do async tasks here      
            // DB calls , network calls, read files , cryptography of passwords etc

            setTimeout(() => {
                console.log("Async task completed");
            }, 100);

            // nothing happens here, so the promise is still pending

            resolve(); // this will change the state of the promise to fulfilled
});

promiseOne.then(function() {
    console.log("Promise resolved/consumed");

})

// then is related to the resolve and catch is related to the reject
// function in then is a call back function which will be called when the promise is resolved or rejected

// upper approach used the variable to store the promise and then consume it, but we can also create and consume the promise in one go without storing it in a variable

new Promise(function(resolve, reject) {
    setTimeout(() => {
        console.log("Async task 2");
        resolve();
        }, 1000);

}).then(function() {
    console.log("Promise 2 resolved/consumed");
})

// if i want to do a network call which return the data so we need to pass the data to the then block 
// because the return is always in the then block, so we can return the data from the then block and it will be available in the next then block

const promiseThree = new Promise(function(resolve, reject) {
    setTimeout(() => {
        console.log("Async task 3");

        resolve({name: "John", age: 30}); // this will change the state of the promise to fulfilled and pass the data to the then block
        }, 1500);

    });


promiseThree.then(function(data) {
    console.log("Promise 3 resolved/consumed");
    console.log(data); // this will log the data passed from the resolve function
});




const promiseFour = new Promise(function(resolve, reject) {
    setTimeout(() => {
        let error = true; // simulating an error
        if(!error) {
            resolve({name: "Jane", age: 25});
        } else {
            reject("Something went wrong"); // this will change the state of the promise to rejected and pass the reason to the catch block
        }
    }, 1500);
});

promiseFour.then(function(data) {
    console.log("Promise 4 resolved/consumed");
    console.log(data);
}).catch(function(error) {
    console.log("Promise 4 rejected");
    console.log(error);
});




// chaining of promises 
// return the username from the first promise and then use that username to fetch the user details in the second promise
new Promise(function(resolve, reject) {
    setTimeout(() => {
        resolve({username: "john_doe", email: "john@example.com"});
    }, 1000);
}).then(function(user) {
    console.log("User: " + user.username);
    console.log("Email: " + user.email);
    return user.username;
}).then(function(username) {
    console.log("Username: " + username);
});

// promises do not run for infinite time, they will run until they are resolved or rejected.

// we use finally block to execute some code after the promise is resolved or rejected, it will always execute regardless of the outcome of the promise


new Promise(function(resolve, reject) {
    setTimeout(() => {
        resolve({username: "john_doe", email: "john@example.com"});
    }, 1000);
}).then(function(user) {
    console.log("User: " + user.username);
    console.log("Email: " + user.email);
    return user.username;
}).then(function(username) {
    console.log("Username: " + username);
}).finally(function() {
    console.log("Finally block");
});



const promiseFive = new Promise(function(resolve, reject) {
    setTimeout(() => {
        let error = false; // simulating an error
        if(!error) {
            resolve({name: "javascript", age: 25});
        } else {
            reject("Something went wrong");
        }
    }, 1500);
});


// we can use the .then but we can use the async await syntax to consume the promise, it is more readable and easier to understand
// we are not ususally handling the catch gracefully in the async await syntax, we can use try catch block to handle the error gracefully

async function consumePromise(){
    try {
        
    const response = await promiseFive // this will wait until the promise is resolved or rejected
    console.log(response);
    }
    catch(error) {
        console.error("Promise rejected:", error);
    }

};
consumePromise();



async function getallusers() {
    try {
    const response = await fetch("https://jsonplaceholder.typicode.com/users");
    const data = await response.json(); // because data is return is in string format so we need to convert it to json format
    
    // **** important *****
    // we need to await the response.json() because it is also a promise, it will return a promise which will be resolved with the data in json format,
    //  so we need to await it to get the data in json format
    console.log("the data is: ", data);
    }
    catch(error) {
        console.log("the error is " + error);
    }

}

getallusers();





fetch("https://jsonplaceholder.typicode.com/users")    // its return a promise so we can use then to consume it
.then(function(response) {
    return response.json(); // this will return a promise which will be resolved with the data in json format
})
.then(function(data) {
    console.log("the data is: ", data[0]); // this will log the first user in the data array
})
.catch(function(error) {
    console.log("the error is " + error);
})

// the data return from the fetchh is comes first before all the functions 
// because the fetch is an asynchronous operation and it will be executed in the background 
// while the other functions are executed in the main thread, so the data will be returned 
// before all the functions are executed.


//  ****************  special que / micro task que / fetch que ***************

// The microtask queue, also known as the special queue or fetch queue, is a separate queue that holds tasks that are scheduled to run after the current task has completed but before the next task in the regular task queue is executed.
// When a promise is resolved or rejected, the associated callback functions are added to the microtask queue
// instead of the regular task queue.
// This means that the callbacks will be executed as soon as the current task is completed, before any other tasks in the regular task queue are executed.
// The microtask queue has a higher priority than the regular task queue, which is why promises are often considered high priority tasks in JavaScript.










