class User {
    constructor(name , age) {
    this.name = name;
    this.age = age;
    }

    LogMe()
    {
        console.log(this.name , this.age);
    };
    // if we want to stop creating id again and afain so we use static
    
    static createId() {
        return `${this.name}${this.age}`;
    }
}

class Teacher extends User {
    constructor(name , age , experince)
    {
        super(name , age);
        this.experince = experince;
    }

}



let user = new User("saif", 29);
console.log(user.name)


const teacher = new Teacher("ali", 39 , 10)

console.log(teacher.createId())   // it will not return anything because the createId method is static and it is not accessible by the instance of the class, so we need to call the createId method by the class name, so that we can access the static method of the class, so that we can get the id of the teacher object.

console.log(User.createId()) // this will return the id of the user object because the createId method is static and it is accessible by the class name, so that we can access the static method of the class, so that we can get the id of the user object.


