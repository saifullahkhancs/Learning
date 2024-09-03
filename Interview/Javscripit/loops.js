// for (var val = 0; val < 10; val++) {
//     // console.log(val);
//     setTimeout(function() {
//         console.log(`The number is ${val}`);
//     }, 1000);
// }

// for (let i = 0; i < 10; i++) {
//     // console.log(i);
//     setTimeout(function() {
//         console.log(`The number is ${i}`);
//     }, 1000);
// }


var array = [1, 2, 3, 4, 5]
for(var i = 0; i < array.length; i++) {
  delay(i)
}
function delay(i) {
  setTimeout(() => {
    console.log(array[i])
  }, 1000);
}


for (key in array){
  console.log(key);
}

const person = {fname:"John", lname:"Doe", age:25};

let text = "";
for (let x in person) {
  text += person[x];
}

console.log(text);



const cars = ["BMW", "Volvo", "Mini"];

for (let x of cars) {
  console.log(x);
}

let language = "JavaScript";
for (let x of language) {
  console.log(x);
}

i = 0;  // because i is var efined and so we redefined it

while (i < 10) {
  console.log(i);
  i++;
}

do {
  console.log(i);
  i++;
}
while (i < 20);