const person = {
    firstName: "ali",
    lastName: "khan",
    id : 45,
    fullName: function(){
        console.log(this.firstName + " " +this.lastName);
    }
};

person.fullName()




