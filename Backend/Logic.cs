//Q:-  What is dofferent between add and append in the lists in the c#??
//Q :- Why append not work but add work??

Q:- Use of the thenInclude() ?
// _dbContext.service.Include(x=>x.branch_services).thenInclude(branch)  we can use that instead of texting Include _dbContext.service.Include("branch_service.branch")


Q :-   What is the difference between the count() and count?
// In C#, Count() and Count have different meanings and usage:

// Count(): This is a LINQ extension method used to count the number of elements in a collection that satisfies a certain condition. It is used with parentheses and can accept a predicate function to filter the elements.
//  For example:
// int count = myList.Count(x => x.SomeProperty == someValue);

// Count: This is a property available on collections in C#, such as arrays or lists. It returns the total number of elements in the collection. It does not accept any parameters and is accessed without parentheses. For example:
// int count = myList.Count;


Q:- What is the idenetity insert in tbe mysql?

// Identity Insert is a feature that allows you to explicitly insert values into an identity column of a table. By default, 
// when you insert a new row into a table with an identity column, 
// SQL Server automatically generates a unique value for that column. This is useful for ensuring uniqueness and maintaining referential integrity.

 Q:- What is meant by the partial class?
// For instance, when working with LINQ to SQL and creating a DBML file. When we copy and paste a table, it will create a partial class in designer.cs. 
// // So to not add new columns, we can create a separate source file for the class,which will act as a partial class.

// A partial class is a special feature of C#. It provides a special ability to implement the functionality of a single class into multiple files and all
// these files are combined into a single class file when the application is compiled. A partial class is created by using a partial keyword. This keyword
// is also useful to split the functionality of methods, interfaces, or structure into multiple files.

Q:- What is origin?
// In web development, an origin refers to the combination of the protocol (such as http or https), domain, and port number of a URL. This combination identifies the source 
// of a web page or web application. Here are some examples of origins:

// https://www.example.com: This is a secure origin (https://) with the domain www.example.com. It's accessed over the default HTTPS port (443).

// http://sub.example.com:8080: This is an insecure origin (http://) with the subdomain sub.example.com. It's accessed over a non-standard port (8080).


Q:- What is the different between the HTTP and HTTPS?

// The main difference between HTTP (Hypertext Transfer Protocol) and HTTPS (Hypertext Transfer Protocol Secure) lies in their security mechanisms:

// Security:

// HTTP: It transmits data in plain text format, making it susceptible to interception and manipulation by malicious parties. This lack of encryption 
//        means that sensitive information like passwords, credit card details, and personal data can be easily intercepted.
// HTTPS: It encrypts the data transferred between the client (browser) and the server using SSL/TLS (Secure Sockets Layer/Transport Layer Security) 
//        encryption protocols. This encryption ensures that even if intercepted, the data cannot be easily read or manipulated.

// Data Integrity:

// HTTP: Since data is transmitted in plain text, there's no inherent mechanism to verify if the data remains unchanged during transmission.
// HTTPS: The encryption ensures data integrity by providing mechanisms to detect if the data has been tampered with during transit. Any alteration 
// to the encrypted data would render it unreadable upon decryption.

// Authentication:

// HTTP: It does not provide any mechanism for server authentication. This means that a client can't be certain it's communicating 
//       with the intended server, making it vulnerable to man-in-the-middle attacks.
// HTTPS: It employs SSL/TLS certificates to verify the identity of the server. This provides assurance to the client that
//       it's communicating with the intended server and not an impostor.

q:- What is CORS??? Imp
// "CORS, or Cross-Origin Resource Sharing, is a security feature implemented by web browsers to protect users from malicious attacks.
//  It restricts web pages or web applications from making requests to a different origin than the one it was served from. 
//   An origin is essentially the combination of the scheme (like http or https), domain, and port number of a URL.

// For example, if your backend API is hosted at 'api.example.com' and your frontend is hosted at 'frontend.example.com', any requests made from the 
// frontend to the backend are considered cross-origin requests. If the backend doesn't explicitly allow requests
//  from the frontend domain, the browser will block these requests due to CORS policy.

// To handle CORS, you typically configure your backend server to include specific HTTP headers in its responses that inform the browser 
// that it's okay to allow cross-origin requests from certain domains. These headers include 'Access-Control-Allow-Origin', which specifies 
// the domains allowed to make requests, and other related headers like 'Access-Control-Allow-Methods' and 'Access-Control-Allow-Headers' 
// to further control the types of requests allowed.

Q:- What is the SQL Injection ?
// SQL injection, also known as SQLI, is a common attack vector that uses malicious SQL code for backend database manipulation to access 
// information that was not intended to be displayed. This information may include any number of items, including sensitive company data,
//  user lists or private customer details.
  examples 
//   1:- SELECT * FROM Users WHERE UserId = 105 OR 1=1;

//   2:- Here is an example of a user login on a web site:

//         Username: John Doe
//         Password: myPass

//         SELECT * FROM Users WHERE Name ="John Doe" AND Pass ="myPass" .

//   3:- A hacker might get access to user names and passwords in a database by simply inserting " OR ""=" into the user name or password
//   text box:

//         User Name:
//         " or ""="

//         Password:
//         " or ""="

//         The code at the server will create a valid SQL statement like this:

//         SELECT * FROM Users WHERE Name ="" or ""="" AND Pass ="" or ""=""


Q:- How we can avoid sql injection? 
// 1:- Use SQL Parameters for Protection
// To protect a web site from SQL injection, you can use SQL parameters.
// SQL parameters are values that are added to an SQL query at execution time, in a controlled manner.

//     txtUserId = getRequestString("UserId");
//     txtSQL = "SELECT * FROM Users WHERE UserId = @0";
//     db.Execute(txtSQL,txtUserId);
// Note that parameters are represented in the SQL statement by a @ marker.
// The SQL engine checks each parameter to ensure that it is correct for its column and are treated literally, and not as part of the SQL to 
// be executed.

// 2:- The first step is input validation (a.k.a. sanitization), which is the practice of writing code that can identify illegitimate user inputs.


