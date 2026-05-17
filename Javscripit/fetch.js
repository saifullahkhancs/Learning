fetch("https://jsonplaceholder.typicode.com/todos/1")
.then((data)=> {
    return data.json()
})
.then((jasonedData) => {
    console.log(jasonedData);
})
.catch( (error) => {
    console.log("ohh no something wrong");
})

.finally( ()=> {
    console.log("well everthing is done, we tried")
})