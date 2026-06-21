fetch("https://jsonplaceholder.typicode.com/todos/1")
.then((data)=> {
    return data.json()
})
.then((jasonedData) => {
    console.log(jasonedData);
})
.catch( (error) => {
    console.error("Fetch failed:", error);
})

.finally( ()=> {
    console.log("well everthing is done, we tried")
})