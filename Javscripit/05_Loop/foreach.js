// forEach loop

// forEach loop is used to iterate over the elements of an array and execute a provided function once for each element in the array. 
// it takes a callback function as an argument and executes that function for each element in the array. 
// the callback function can take three arguments: the current element, the index of the current element, and the array itself.


const coding = [ "JavaScript", "Python", "Java", "C++" ];


// simple function defination   
//  const function_variable = function name() {}
// arrow function defination
// const function_variable = () => {}
   
   
   // but in call back function we can use anonymous function and arrow function as well
   // for example
   
coding.forEach(function (language) {
    console.log(language);
});

coding.forEach( (language) => { 
    console.log(language);
});



// forEach has array items , array indices and the array itself as an argument in the callback function

coding.forEach(function (language, index, array) {
    console.log(`Language: ${language}, Index: ${index}, Array: ${array}`);
});


const students = ["alice", "bob", "charlie"];

const stud = students.forEach((student) =>    {

    return student.toUpperCase();
});

console.log(stud) // it will return undefined because forEach does not return anything, it only executes the provided function for each element in the array.


