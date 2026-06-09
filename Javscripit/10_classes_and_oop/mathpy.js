//  we have to change the value of pi to 4
console.log(Math.PI) // 3.141592653589793
// we have object and its property    standard and prototype methods and properties


let firstValue = Object.getOwnPropertyDescriptor(Math, 'PI') // we can change the value of pi to 4 but it is not recommended

console.log(firstValue) // it is not writable and it is not configurable












