

// ************ Switch statement  ************

//       switch statement is used to perform different actions based on different conditions

// basic structure of switch statement


// switch (statement) {
//   case value1:
//     // code to be executed if statement === value1
//     break;
//   case value2:
//     // code to be executed if statement === value2
//     break;
//  ...
//   default:
//     // code to be executed if statement doesn't match any of the cases
//     break;
// }



const month = "3";


switch (month) {
    case "1":
        console.log("January");
        break;
    case "2":
        console.log("February");
        break;
    case "3":
        console.log("March");
        break;
    case "4":
        console.log("April");
        break;
    case "5":
        console.log("May");
        break;                          

    case "6":
        console.log("June");
        break;
    case "7":
        console.log("July");
        break;
    case "8":
        console.log("August");
        break;
    case "9":
        console.log("September");
        break;
    case "10":
        console.log("October");
        break;
    case "11":
        console.log("November");
        break;
    case "12":
        console.log("December");
        break;

    default:
        console.log("Invalid month");
        break;
}




const day = "Monday";

switch (day) {
    case "Sunday":
        console.log("its a weekend");
        break;
    
    case "Saturday":
        console.log("its a weekday")


    default:
        console.log("its a weekday");
        break;

}

