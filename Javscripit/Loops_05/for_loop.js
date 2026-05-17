// for loop

for (let i = 0; i < 5; i++) {
  console.log(i);
}   

// double for loop
for (let i = 0; i < 3; i++) {
    for (let j = 0; j < 3; j++) {
        console.log(`i: ${i}, j: ${j}`);
    }
}


// for in loop
const person1 = {fname:"John", lname:"Doe", age:25};
for (let x in person1) {
  console.log(x);   // it print key
}

// for of loop
const cars = ["BMW", "Volvo", "Mini"];
for (let x of cars) {
  console.log(x);
}

const greeting = "Hello";
for (let x of greeting) {
  console.log(x);
}




// break and continue
for (let i = 0; i < 10; i++) {
    if (i === 5) {
    break;
  }
  console.log(i);
}


for (let i = 0; i < 10; i++) {
    if (i === 5) {
    continue;
  }
  console.log(i);
}

