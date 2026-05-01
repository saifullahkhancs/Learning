    What is the different between the flex and grid ?? 
// In the context of frontend development, "Flex" and "Grid" are both layout systems used in CSS to create responsive and flexible designs,
//  but they have different approaches and capabilities:

// Flexbox (Flex):
//         Flexbox is a one-dimensional layout model that is best suited for laying out items in a single row or column. It's designed to 
//        distribute space along a single axis (either horizontally or vertically) and allows for easy alignment, ordering, and sizing of items within a container.

//        Flexbox is ideal for building components like navigation menus, card layouts, or any UI elements where you need to control the layout along a single axis.

//        Key properties include display: flex to create a flex container, flex-direction to specify the direction of the main axis, justify-content to align items 
//        along the main axis, and align-items to align items along the cross axis.

// CSS Grid (Grid):

//   CSS Grid is a two-dimensional layout system that allows you to create grid-based layouts with rows and columns. It provides more control over both the rows 
//   and columns of the layout, allowing you to define precise grid lines and position items anywhere within the grid.

//   Grid is suitable for creating complex layouts with multiple rows and columns, such as full-page layouts, magazine-style designs, or any UI 
//   that requires precise control over the placement of items.

//   Key properties include display: grid to create a grid container, grid-template-columns and grid-template-rows to define the size and number of columns and rows, 
//   grid-column and grid-row to position items within the grid, and grid-gap to add space between grid items.


 Relational Databases: 
//      Relational databases store data in tables consisting of rows and columns. Each row represents a record, and each column represents an attribute or 
//       field of that record. Data in relational databases is organized in a structured manner, and relationships between tables are established using keys.

 Object-Oriented Programming (OOP): 
//      In object-oriented programming languages like Python, Java, or C#, data is organized into objects, each containing attributes 
//       (properties or fields) and methods (functions or behaviors). Objects can represent real-world entities and encapsulate both data and behavior.
  
    //  ^^^
    //  |||
Q:- What id ORM ??
// ORM stands for Object-Relational Mapping. It's a programming technique used in software development to facilitate the conversion between the data in 
//relational databases and the objects in object-oriented programming languages.


// ORM bridges the gap between these two paradigms by providing a mechanism to map database tables to classes and objects in code. 
// It allows developers to interact with the database using high-level programming constructs like objects, methods, and queries, rather
//  than dealing directly with SQL (Structured Query Language) statements and database-specific APIs.

// Key features and benefits of ORM include:

// Abstraction: 
//     ORM abstracts away the details of the underlying database, allowing developers to work with objects and classes instead of directly manipulating database tables.

// Simplified Data Access:
//       ORM provides a simplified and intuitive way to perform CRUD (Create, Read, Update, Delete) operations on database records using object-oriented constructs.

// Portability:
//      ORM frameworks often support multiple database systems, allowing developers to switch between different databases without changing the application code significantly.

// Increased Productivity: 
//      ORM reduces the amount of boilerplate code required for database interaction, resulting in faster development cycles and increased productivity.

// Popular ORM frameworks in various programming languages include:

// Python: SQLAlchemy, Django ORM
// Java: Hibernate, JPA (Java Persistence API)
// C#: Entity Framework Core, NHibernate

// Overall, ORM simplifies database access and management in object-oriented applications, making it easier for developers to work with relational databases
//  while leveraging the benefits of object-oriented programming.

What is an AVL ?

// An AVL tree is a self-balancing binary search tree named after its inventors Adelson-Velsky and Landis. It's designed to maintain a balanced structure,
//  ensuring that the height difference between the left and right subtrees of any node (known as the "balance factor") is at most 1. 
//  This property helps to ensure efficient search, insertion, and deletion operations with a time complexity of O(log n), where n is the number of nodes in the tree.

// Here are some key characteristics of AVL trees:

// Binary Search Tree Property: 
//     Like all binary search trees, an AVL tree maintains the binary search tree property, where for each node, the values in the left subtree 
//      are less than the value of the node, and the values in the right subtree are greater than the value of the node.

// Balanced Structure: 
//     In addition to the binary search tree property, AVL trees are balanced in such a way that the height difference between the left and right 
//     subtrees of any node is at most 1. This ensures that the tree remains balanced and prevents degeneration into a linked list, which would result in degraded performance 
//     for search operations.

// Balancing Operations:
//    When an insertion or deletion operation causes the balance factor of a node to become greater than 1 or less than -1, the tree needs 
//    to be rebalanced to maintain the AVL property. This is typically achieved through rotation operations, such as single rotations (left or right) and 
//    double rotations (left-right or right-left), which preserve the binary search tree property while restoring balance.

// Complexity: 
//   The time complexity of search, insertion, and deletion operations in an AVL tree is O(log n), where n is the number of nodes in the tree. 
//   This is because AVL trees maintain a balanced structure, ensuring relatively uniform depths for nodes and efficient search paths.

// AVL trees are widely used in scenarios where efficient search, insertion, and deletion operations are required, and the dataset is expected to undergo 
// frequent modifications. They are commonly used in database indexing, where quick search operations are essential for efficient query processing. However, 
// the overhead of maintaining balance through rotations can sometimes make AVL trees less efficient than simpler data structures like binary search trees for 
// datasets with relatively stable access patterns.

Q:- What is thee difference between the Session Storage and Local Storage?

//   In web development, both Session Storage and Local Storage are mechanisms provided by web browsers to store data locally on the client-side. 
//   They are part of the Web Storage API and offer ways to persist data beyond the current browsing session. However, they have some key differences:

// Local Storage:

// Scope:
//     Data stored in Local Storage persists indefinitely until explicitly cleared by the user or the application.
// Storage Limit: 
//       Local Storage typically allows more storage space (usually up to 5MB or more) compared to Session Storage.
// Access:
//      Data stored in Local Storage is accessible across browser windows and tabs and persists even after the browser is closed and reopened.
// Use Cases: 
//      Local Storage is suitable for storing user preferences, settings, cached data, or any other data that needs to be retained across multiple sessions.


// Session Storage:

// Scope: 
//     Data stored in Session Storage persists only for the duration of the current browsing session. Once the session ends
//     (i.e., when the user closes the browser window or tab), the data is cleared.
// Storage Limit: 
//     Session Storage typically has a smaller storage limit (usually up to 5-10MB) compared to Local Storage.
// Access:
//      Data stored in Session Storage is scoped to the current browser window or tab. Each new window or tab will have its own separate Session Storage.
// Use Cases:
//      Session Storage is useful for storing temporary data, such as shopping cart items, form data, or authentication tokens, that is only needed for the current session.

// todo  
Q:-  What is the sql injection and their approaches?
Ans:- 