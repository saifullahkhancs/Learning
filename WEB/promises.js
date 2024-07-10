const promise = new Promise((resolve , reject) => {
            resolve("we did it");
})
promise.then((data)=> {
    console.log(data)
})

// to catch the error from the promsises

 
const promises = new Promise((resolve , reject) => {
            reject("we see the error");
})
promises.then((data)=> {
    console.log(data)
})
// if we do not catch the error provided by the promise so
// program will 
.catch( err => console.log(err))


/// more example with  objectss and real data


const promisess = new Promise((resolve , reject) => {
            resolve({user: "ali"});
})
promisess.then((data)=> {
    return user=data.user
})
 // as then ka return ko next then main usee karyain gyy
.then((user) => {
    console.log(user)
})
.catch( err =>{ 
    console.log(err)
}) 
//



const promis = new Promise((resolve , reject) => {
            resolve({user: "ali"});
})
promis.then((data)=> {
    return fetch("https://jsonplaceholder.typicode.com/todos/1")
})
 // as then ka return ko next then main usee karyain gyy
.then((todos) => {
    console.log(todos)
})
.catch( err =>{ 
    console.log(err)
}) 