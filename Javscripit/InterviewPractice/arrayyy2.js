const fruits = ["Banana", "Orange", "Apple", "Mango"];

console.log(fruits.reverse());

const points = [40, 100, 1, 5, 25, 10];
points.sort(function(a, b){return a - b});

console.log(points);

// When the sort() function compares two values, 
// it sends the values to the compare function, and sorts 
//the values according to the returned (negative, zero, positive) value.

// #######  how to find max element #########

function myArrayMax(arr) {
    return Math.max.apply(null, arr);
}
console.log(myArrayMax(points));

// #######  how to find minelement #########

function myArrayMin(arr) {
    return Math.min.apply(null, arr);
}

console.log(myArrayMin(points));


const numbers = [45, 4, 9, 16, 25];
let index = 0;
const new_array = [];

numbers.forEach(function(num) {
        new_array[index] = num;
        index += 1;
} );

console.log(new_array);

mapSqueredArrayed = numbers.map(function(num) {
    return num*num
})

console.log(mapSqueredArrayed)

filteredArray = numbers.filter(function(num) {
    return  num%2 == 0 ;
})
console.log(filteredArray)

sum = numbers.reduce(function(total , num){
    return total + num ;
})

console.log(sum);

every_method = numbers.every(function(value){
    return value > 50 ;
})

console.log(every_method);

some_method = numbers.some(function(value){
    return value > 20 ;
})

console.log(some_method);