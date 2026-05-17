// for loop
var num =1;
for (num ; num < 5; num++){
    console.log(num);    }

for (let i=1 ; i<=5 ; i++) {
    console.log(i);
}

// while loop
let count = 5;
while (count > 0){      // it will go upto 1
    console.log(count);
    count--;}

    // do_while loop
var num = 5;
do {
    console.log(num);
    num--;
}while(num >= 0);   // it will go upto 0


// for...  in loop
const li = [1,2,3,4,5 , 6 ,7 ,8]
for (let i in li){
    console.log(li[i]);
}

//  for ... of loop   
for (let any of li){    // off direct element ko utta laita ha 
    console.log(any);   // thats why it is only used with array which is not object
}

// extra
const person = {name:"ali" , age:33 , job:"eng"};  // end pa ";" mark atta ha object ka

for (let key in person){
    console.log(key+":" +person[key]);
}

// it will generate error as object is not iteratbale in way of off
// for (let any of person){    // off dyrect element ko utta laita ha 
//     console.log(any);
// }