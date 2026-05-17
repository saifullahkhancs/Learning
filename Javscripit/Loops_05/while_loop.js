let index = 0 ;

while (index < 5) {
    console.log(index);
    index++;
}


let myarray = [1, 2, 3, 4, 5];

index = 0;
while (index < myarray.length) {
    console.log(myarray[index]);
    index++;
}


// ***** do while loop *****

// in this we do work first then check condition so it will run at least once even if condition is false


let score = 0;

do {
    console.log(score);
    score++;
} while (score < 5);

// as compared to below it print 5 mean it add first then check

while (index < 5) {
    console.log(index);
    index++;
}