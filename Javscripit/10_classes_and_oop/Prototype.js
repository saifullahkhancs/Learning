let myname = "saif    "

console.log(myname.length); // 4

// we can not use trim beacuse it is not goood method for repeatation 
// so  we can go with the adding a extra property or function to the string prototype, so that we can use that property or function on any string object.
// like   console.log(myname.truelength())


let myheroes = ["superman", "batman", "spiderman"];


let heropower = {
    superman: "super strength",
    batman: "intelligence",
    spiderman: "spider sense",

    getspiderpower: function() {
        console.log("spidy power is " + this.spiderman);
    }

}

// heropower.getNewPower()

// for now we do not have any method tot get the power but for now we know that 

// function/array/object -------> object--------> prototype --------> methods and properties 

// javascript is a prototype based language, it means that every object in javascript has a prototype, 
// and we can add methods and properties to the prototype of an object, 
// so that all the objects that are linked to that prototype can access those methods and properties.


//  ******* but object parent/prototype is null
// thats why above object we can not assign the getNewPower method to the heropower object because it is not linked to any prototype, it is a standalone object, so we can not add methods to it, but we can add methods to the Object.prototype because all the objects in javascript are linked to the Object.prototype, so we can add methods to the Object.prototype and all the objects will be able to access those methods.


Object.prototype.getNewPower = function() {
    console.log("the new power is " + this.superman);
}

heropower.getNewPower()


Array.prototype.herosayhi = function() {
    console.log("hi i am hero");
}

myheroes.herosayhi();
myheroes.getNewPower() // this will work because myheroes is linked to the Array.prototype and the Array.prototype is linked to the Object.prototype,
//  so it can access the getNewPower method because it is linked to the Object.prototype, but it can not access the herosayhi method because it is not linked to the Array.prototype, it is linked to the Object.prototype, so it can not access the herosayhi method, but it can access the getNewPower method because it is linked to the Object.prototype.
// heropower.herosayhi() // this will not work because heropower is not linked to the Array.prototype, it is linked to the Object.prototype, so it can not access the herosayhi method, but it can access the getNewPower method because it is linked to the Object.prototype.
// can we check in the array as we know parent/ prototype of array is also an object



// array      function      string 
//    \          |            /
//     \         |           / 
//      \        |          /
//       \       |         /
//        \      |        /
//         \     |       /
//          \    |      /
//             object  
//               |
//               |
//               |
//             null 
//

// but we can not suppose that adding the method to array will add in the function or vice versa because they are different prototypes, so we can not access the method of one prototype in the other prototype, but we can access the method of the Object.prototype in both the Array.prototype and Function.prototype because they are linked to the Object.prototype, so we can access the methods of the Object.prototype in both the Array.prototype and Function.prototype.



// Inheritance

const User = {
    name: "saif",
    email: "saif@example.com"
}



const Teacher = {
    makeVideo:true
}

const TeaachingSupport = {
    isAvailable:false
}

const TaSupport = {
    makeAssignment:"js assigment",
    fullTime:true,
    __proto__:TeaachingSupport

}


Teacher.__proto__ = User; // this will link the Teacher object to the User object, so that we can access the properties of the User object in the Teacher object, so that we can share information between these objects.

// ********* prototypical inheritance *********

// prototypical inheritance is a way of sharing information between objects,
//  it is a way of creating a new object that is linked to an existing object, 
// so that we can access the properties and methods of the existing object in the new object, 
// so that we can share information between these objects.




// how we share information between these objects, 
// we can use the prototype and __proto__ to share information between these objects, so that we can access the properties of one object in another object, so that we can share information between these objects.


// __ proto__ is a property of an object that points to the prototype of that object, 
// so that we can access the properties and methods of the prototype of that object,
// so that we can share information between these objects.



// Modern Suntax


Object.setPrototypeOf(TeaachingSupport, Teacher); 

// this will link the TeaachingSupport object to the Teacher object, so that we can access the properties of the Teacher object in the TeaachingSupport object, so that we can share information between these objects.

console.log(TeaachingSupport.makeVideo); // this will work because the TeaachingSupport object is linked to the Teacher object, so that we can access the properties of the Teacher object in the TeaachingSupport object, so that we can share information between these objects.



let anotherName = "saif    "


String.prototype.truelength = function() {
    console.log(this.trim().length);
}   


anotherName.truelength()

"hassan    ".truelength()
"ahsaan    ".truelength()






















