//Q:-  What is dofferent between add and append in the lists in the c#??
//Q :- Why append not work but add work??

Q:- Use of the thenInclude() ?
// _dbContext.service.Include(x=>x.branch_services).thenInclude(branch)  we can use that instead of texting Include _dbContext.service.Include("branch_service.branch")


// Q :-   What is the difference between the count() and count?

// In C#, Count() and Count have different meanings and usage:

// Count(): This is a LINQ extension method used to count the number of elements in a collection that satisfies a certain condition. It is used with parentheses and can accept a predicate function to filter the elements.
//  For example:
// int count = myList.Count(x => x.SomeProperty == someValue);

// Count: This is a property available on collections in C#, such as arrays or lists. It returns the total number of elements in the collection. It does not accept any parameters and is accessed without parentheses. For example:

// int count = myList.Count;

// Q:- What is the idenetity insert in tbe mysql?

// Identity Insert is a feature that allows you to explicitly insert values into an identity column of a table. By default, 
// when you insert a new row into a table with an identity column, 
// SQL Server automatically generates a unique value for that column. This is useful for ensuring uniqueness and maintaining referential integrity.

Q:- What is meant by the partial class?

