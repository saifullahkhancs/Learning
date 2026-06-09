// ES6


class User {
    constructor(username, email, password) {
        this.username = username;
        this.email = email;
        this.password = password;
    }

    encryptPassword() {
        return `${this.password}abc`;
    }

    changeUsername() {
        return `${this.username.toUpperCase()}`;
    }

}


const user1 = new User("John", "john@example.com", "password123");

console.log(user1.username); // this will log the username of the user1 object
console.log(user1.email); // this will log the email of the user1 object
console.log(user1.password); // this will log the password of the user1 object






// behind the seen

function createUser(username, email, password) {
    this.username = username;
    this.email = email;
    this.password = password;

}

createUser.prototype.encryptPassword = function() {
    return `${this.password}abc`;
}

createUser.prototype.changeUsername = function() {
    return `${this.username.toUpperCase()}`;
}

const user2 = new createUser("John", "john@example.com", "password123");

console.log(user2.username); // this will log the username of the user2 object
console.log(user2.email); // this will log the email of the user2 object
console.log(user2.password); // this will log the password of the user2 object




