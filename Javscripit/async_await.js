 async function gettodo(){
    try {
    const responce = await fetch("https://jsonplaceholder.typicode.com/todos/1");
    const data = await  responce.json()
    console.log(data);
    console.log("other code execution")
    } catch(err){
        console.error("Fetch failed:", err);
    }
 }

 gettodo()