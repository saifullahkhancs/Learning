Q:- What is SQL?
Ans:- It is an standard programming language that is designed specifically for storing and managing the data in the
	  relational database management systems(RDBMS) using all kinds of operations.

Q:-  What are different type of SQL statement?
Ans:- There are 3 different CATEGORIES of SQL statemnets which are DDL , DML and DCL
	DDL (DATA DEFINATION LANGUAGE)               DML (DATA MODIFICATION LANGUAGE)                   DCL (DATA CONTROL LANGUAGE)
		CREATE											INSERT                                             COMMIT
		ALTER											UPDATE											   ROLLBACK
		TRUNCATE										MERGE										       SAVEPOINT
		DROP  										    SELECT												GRANT
																											REVOKE

Q:- What is database and database managment system?
Ans:- DATABASE: It is structured collection of data that is orgaized and stored in the way that makes it easy to reterive and manage.
	  Databases are used to store , manage and retrieve information efficiently.

	  DATABASE MANAGEMENT SYSTEM(DBMS) :- Is software designed to interact with the users , applications and the database itself to capture and analyze the data.
	  It provide the interface for definng , creating , querying, updating and administering the database.
	  The primary purpose of a DBMS is to provide an efficient and secure way to manage and organize data.

Q:- What are the E_R model?
Ans:- It is derived as entity relationship model. Define the conceptual view of databases
for example: ali is entity , student is the entity type , class is the entity group.
Attributes:- Properties and characteristics of the enetity.
Relations:- two_dimensional structure containing number of rows  where eachcrow rpresent the record


--Q1:- What is the difference between the realtional and non_realtional databases?
--Relational-Database:-
--					It is structured mean the data present in it is in the form of tables, Many times the data within these tables have relationship
--					with one another or dependencies

--Non-Realtional-Database:-
--						It will store the data in the variety of the models including JSON(Javascript Object Notation) BSON (Binary JSON) key_value pairs , tables with rows with 
--						dynamic coloumns , and nodes and edges and graps and documnets.
--						It does not use the traaditional table based realtional_structure .
--						Distributed and unstructured data 

Q:- What are database transcatios?
	Sequence of operations performed which change the consistent state of the database to the another is known as the database transcation.

Q:- What are joins?
	Deriving the relationship between different tables by combining columns from one or more tables having common values.

	INNER JOIN :- Rtuern only the rown where there is a match in both tables
	Select * from table1 innner join table2 On table1.column_name = table2.column_name

	**** inner join and join both retrun the same values ***********************   important 

	LEFT JOIN(LEFT OUTER JOIN)
	
--Q2:-  Difference between DELETE , TRUNCATE and DROP?
--	DELETE:-
--			(DML) After execution , Commit and rollback statement can be performed to retrieve lost data.
--			delete rows (only 1 or more) // slower then truncate
--	TRUNCATE:-
--			(DDL) After execution , Commit and rollback statement can not be performed to retreive the data.
--			drop all the data not the structure
--	Drop:- 
--			(DDL) It is used to drop the table or key like , primary key/ foregin key / 


--for example :-  Drop table / database / index

		

Select id , CONCAT_WS('  ,  ' ,price , vat , discount) As financial_details from booking

--SELECT * FROM branch LIMIT 5;   LIMIT IS ONLY USED IN MySql and PostegralSql  

SELECT TOP 5 * FROM booking;
--Select * from booking offset 2; we can not use it in that way but we use it in the way given below

SELECT * FROM booking
ORDER BY id
OFFSET 2 ROWS
FETCH NEXT 5 ROWS ONLY;

Select price , status_id , payment_status_id from booking where price > 300 Group by status_id order by price 


SELECT price, status_id, payment_status_id
FROM booking
WHERE price > 300
GROUP BY price, status_id, payment_status_id
ORDER BY price;

Select status_id, AVG(net_price) as avarage_price from booking
group by status_id;

Select payment_status_id, 
Sum(price) as total_price,
Sum(discount) as total_discount 
from booking
Group by payment_status_id 
Having  total_price > 200 
order by total_discount;
 
     --imp imp imp 

--keep in mind their is differnent in between ,mssql nad mysql
SELECT
  payment_status_id,
  SUM(price) AS total_price,
  SUM(discount) AS total_discount
FROM
  booking
GROUP BY
  payment_status_id
HAVING
  SUM(price) > 200
ORDER BY
  total_discount;

  --Difference between having and where?

--HAVING:-  
		--Used in database systems to fetch the data from teh groups according to the given condition
		--The having clause is alwaus executed with groupby clause
		--We can only use select statement with having
		--The having clause is used in sql queries after the group by clause;
		--Used in columns to filters groups
		--It is a post filter.
		 
--WHERE
		--The where clause is used in database system to fetch data values from the table according to the given condition.
		--The where clause can be exacuted without the groupby clause
		--We can use select , update and delete with the where clause.
		--The Where clause is always used before used before the group by clause  in the sql queries.
		--Used in rows operations to filter the single record.
		--It is a pre_filter

 Q:- What is idenetity?
 Typically associated with the integer data types e.g int , biginit
 Automatically increment by a specifiied value each time a new row is inserted into teh table.
 Unique within the scope of a table , but not guranteed to be gloablly unique.
 Often used for primary key columns where an auto-increment integer is sufficient for uniquness.

 Q:- What is Guid?
 GUID stand for Globaly Unique Identifier. 
 Assocaite with the "UNIQUEIDENTIFIER" data type
 Universally unique idenetifier that is typically generated using algorathims that make it extremely unlikely
 to generate the same identifier on different machines.
 Globally unique, making it suitable for scenarios where uniqunes across different databases or systems is required.
 Useful in distributed the systems  ,replicate scenarios , or when the uniqueness of identifiers needs to be guranteed globally.


Q:- What is view?
Defination:-	It is a virtualtable based on the result set of an sql statement.
	
Query:- 	Create view [Brazil Customer] as select cust_name, contact_num from customer where country = "Brazil"

Benefits:-
		Limit the degree of expoure.
		Permission only to view not to the central database.
		Simplify and join multiple tables into a single virtual table.
		Hide the complexity of data.
		View take very little space to store , the database only contain defination , not a copy of all the data
		View can provide extra security.

Q:- What is trigger? 
Ans:- A code associated with insert , update ,delete operations. The code is executed automatically
	  whenever the associated query is executed. They can not be called directly.

Q:- What are stored procedures?
Ans:- It contains set of operations that are commonly used in an applications to do some common 
	  database tasks.

Q:- What are transcations?
Ans:- A database transcations is a set of databse operations that ust be traeted as a whole , which means
	  either all operations are executed or none of them. An example of bank transcation from one account to the other bank 
	  .Either the both the credit and debit operations must me perormed/executed or none of them.

Q:- What are acid properties?
Ans:- First of all acid is stand for ATOMICITY , CONSISTENCY , INTEGRITY  and DURABILITY. These are all the set of properties 
that gurantee that database transcations are processed reliably.

ATOMICITY : - All transcations units must be executed successfully. IF one is failed whole transcation will be oborted , it goes roll back
				to the precious state.
					.. Commit statement 
					.. Rollback statement

CONSISTENCY:- The databse changes state only when a transcation will be committed successfully , protecting the data from crashing

ISOLATION:- Operations in the transcations can  operates independently 
			.. set isolation level

DURABILITY:- This property generates the resily of committed transacations persists permentaly even  if the system carashes or failed 

9. How do you implement pagination in SQL queries?
Pagination in SQL queries can be implemented using the LIMIT and OFFSET clauses (in MySQL, PostgreSQL) or the FETCH NEXT and OFFSET clauses (in SQL Server, Oracle 12c+). For example, to retrieve the second set of 10 records:

MySQL/PostgreSQL:sql

SELECT * FROM table_name
LIMIT 10 OFFSET 10;

SQL Server:sql

SELECT * FROM table_name
ORDER BY column_name

OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;





Select * from booking inner join booking_detail on 
booking.id = booking_detail.booking_id ;

In SQL, joins are used to combine rows from two or more tables based on a related column between them. There are several types of joins, each serving a different purpose. Here are the main types of joins with examples:

Inner Join:

Retrieves records that have matching values in both tables.

SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
INNER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;


Left (Outer) Join:

Retrieves all records from the left table (table1) and the matched records 
from the right table (table2). The result is NULL from the right side if there is no match.

SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
LEFT JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

Right (Outer) Join:

Retrieves all records from the right table (table2) and the matched records from 
the left table (table1). The result is NULL from the left side if there is no match.

SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
RIGHT JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

Full (Outer) Join:

Retrieves all records when there is a match in either left (table1) or right (table2) table records.
It returns NULL for unmatched rows from both tables.

SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
FULL OUTER JOIN Customers ON Orders.CustomerID = Customers.CustomerID;

Cross Join:

Produces the Cartesian product of the two tables, meaning every row in the first table is combined with every row in the second table.

SELECT Orders.OrderID, Customers.CustomerName
FROM Orders
CROSS JOIN Customers;


Self Join:

A join where a table is joined with itself. 
Useful for hierarchical data or finding relations within the same table.


Natural join:

A natural join is a type of join that automatically matches columns between
the two tables based on columns with the same name and 
compatible data types. Unlike other types of joins, it 
does not require you to specify the columns to join on explicitly.

SELECT *
FROM Employees
NATURAL JOIN Departments;

Functions and stored procedures are both programmable objects in SQL used to encapsulate logic and operations, but they have different purposes, capabilities, and limitations. Here’s a detailed comparison:

### Functions

1. **Purpose**:
   - Functions are designed to return a single value (scalar functions) or a table (table-valued functions).
   - Used for computations and return values that can be used in SQL statements.

2. **Return Type**:
   - Must return a value (scalar or table).

3. **Syntax**:
   ```sql
   CREATE FUNCTION FunctionName (@param1 DataType, @param2 DataType)
   RETURNS DataType
   AS
   BEGIN
       -- Function logic
       RETURN SomeValue;
   END;
   ```

4. **Usage**:
   - Can be used in SELECT statements, WHERE clauses, JOIN conditions, etc.
   - Can be called directly from SQL statements.
   - Can be used in computed columns in tables.

5. **Side Effects**:
   - Should not have side effects; typically, they do not modify database state.
   - Cannot perform operations that modify the database (e.g., INSERT, UPDATE, DELETE).

6. **Transactions**:
   - Cannot manage transactions.

7. **Performance**:
   - Generally optimized for performance when used within queries.

### Stored Procedures

1. **Purpose**:
   - Stored procedures are designed to perform a series of operations, including complex business logic, and can include multiple statements like SELECT, INSERT, UPDATE, DELETE, and control-of-flow constructs.
   - Used for batch processing, complex operations, and encapsulating business logic.

2. **Return Type**:
   - Can return zero or more result sets and can also return output parameters.

3. **Syntax**:
   ```sql
   CREATE PROCEDURE ProcedureName
       @param1 DataType,
       @param2 DataType OUTPUT
   AS
   BEGIN
       -- Procedure logic
       SELECT SomeValue;
       -- Optional: SET @param2 = SomeValue;
   END;
   ```

4. **Usage**:
   - Executed using the EXECUTE or EXEC statement.
   - Can include calls to other stored procedures and functions.
   - Cannot be used directly in SQL statements like SELECT or WHERE.

5. **Side Effects**:
   - Can have side effects and perform operations that modify the database.
   - Can include transactions to ensure data consistency.

6. **Transactions**:
   - Can manage transactions, allowing for complex transactional operations.

7. **Performance**:
   - Can be optimized for batch processing and complex operations, though performance depends on the specific implementation.

### Summary

- **Functions** are best for computations and returning values within SQL statements without modifying database state.
- **Stored Procedures** are best for executing a series of operations, including data modifications, complex business logic, and transaction management.

### Example of Function

```sql
CREATE FUNCTION GetEmployeeAge (@EmployeeID INT)
RETURNS INT
AS
BEGIN
    DECLARE @Age INT;
    SELECT @Age = DATEDIFF(YEAR, BirthDate, GETDATE())
    FROM Employees
    WHERE EmployeeID = @EmployeeID;
    RETURN @Age;
END;
```

### Example of Stored Procedure

```sql
CREATE PROCEDURE UpdateEmployeeSalary
    @EmployeeID INT,
    @NewSalary DECIMAL(10, 2)
AS
BEGIN
    UPDATE Employees
    SET Salary = @NewSalary
    WHERE EmployeeID = @EmployeeID;

    IF @@ROWCOUNT = 0
    BEGIN
        PRINT 'Employee not found';
    END
    ELSE
    BEGIN
        PRINT 'Salary updated successfully';
    END;
END;
```


Clustered Indexing
A clustered index determines the physical order of data in a table. The table rows are stored on disk in the same order as the index. There can be only one clustered index per table because the data rows themselves can be stored in only one order.

Non-Clustered Indexing
A non-clustered index creates a separate structure from the table that includes a sorted list of values and pointers to the corresponding data rows. This type of index does not alter the physical order of the data in the table. A table can have multiple non-clustered indexes.


