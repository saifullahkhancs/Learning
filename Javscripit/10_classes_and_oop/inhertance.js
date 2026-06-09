
// with constructor

class User {
    constructor(username, email, password) {
        this.username = username
        this.email = email
        this.password = password
    }

    encryptPassword() {
        return `${this.password}`
    }
}

class role extends User {
    constructor(username, email, password, role) {
        super(username, email, password)
        this.role = role
    }
}

const user1 = new User("John", "john@example.com", "password123");

console.log(user1.username); // this will log the username of the user1 object

const admin1 = new role("Admin", "admin@example.com", "admin123", "admin");

console.log(admin1.username);

// check whether admin is instance of user
// ***********     instanceof     ************

console.log(admin1 instanceof User); // this will return true because the admin1 object is an instance of the User class, so it can access the properties and methods of the User class, so it can access the username property of the User class, so it can log the username of the admin1 object, so it can log "Admin" in the console.

// prototyping behaviour

function User(username, email, password) {
    this.username = username
    this.email = email
    this.password = password
}

User.prototype.encryptPassword = function() {
        return `${this.password}`
}


function role(username, email, password, role) {
    User.call(this, username, email, password)
    this.role = role
}

const user2 = new User("John", "john@example.com", "password123");

console.log(user2.username);

const admin2 = new role("Admin", "admin@example.com", "admin123", "admin");

console.log(admin2.username);








