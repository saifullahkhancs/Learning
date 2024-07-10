let num = 10;

if (num >10) {
    console.log("number is greater then 10");
}
else if (num == 10){
    console.log("the number is equal to 10");
}
else {
    console.log("num is less then 10")
}


let fruit = "orange"

switch (fruit) {
    case "apple":
        console.log("you chose the apple");
        break                               // imp point to remeber
    case "orange":
        console.log("you chose the orange");
        break
    case "banana":
        console.log("you chose the banana");
        break
    default:
        console.log("unknown fruit");
}