# Intro to Relational Databases
###### SQL, DB-API, and More!
***

## Course Summary

This course is a quick, fun introduction to using a relational database from your code, using examples in Python. You’ll learn the basics of SQL (the Structured Query Language) and database design, as well as the Python API for connecting Python code to a database. You’ll also learn a bit about protecting your database-backed web apps from common security problems.

After taking this course, you’ll be able to write code using a database as a backend to store application data reliably and safely.

## Why Take This Course?

If you look under the hood of a lot of major web sites — from Wikipedia to Reddit — you’ll find a relational database somewhere.

Database systems such as PostgreSQL and MySQL have been part of the web developer’s toolkit for many years, and remain some of the most powerful tools available for storing and manipulating structured data.

If you’re planning to continue on in full-stack development, knowing about databases is essential background. Even though many toolkits hide the details of the database from your application code, being able to interact with the database will serve you well in designing, debugging, and maintaining your applications.

## Prerequisites and Requirements

You can read and write basic code in Python. This course uses programming exercises in Python. If you haven’t worked with Python before, check out our course [Programming Foundations with Python](https://www.udacity.com/courses/ud036).

If you can understand this code (maybe with the help of the [**random** module documentation](https://docs.python.org/2/library/random.html#random.choice)), you know enough Python for this course:

```
import random

def ChooseTwice(items):
    a = random.choice(items)
    b = random.choice(items)
    return a, b

names = ["Alice", "Bob", "Charlie", "Debra"]
(one, two) = ChooseTwice(names)
if one == two:
    print "%s is happy!" % one
else:
    print "%s likes %s!" % (one, two)
```
**You can use a command-line interface (terminal).** Some of the exercises in this course involve using a Unix-style command-line interface to enter commands, run Python programs, and navigate directories.

If you have taken our course on [Git and Github](https://www.udacity.com/course/ud775), the level of command-line use in this course is similar.

**You don’t need to be a Web programmer.** This course does include a small Web application and some HTML and JavaScript in examples, but you will not need to make changes in these languages.

**You don’t need any previous database experience.** This course is an entry-level introduction to relational databases.

**You need a programming text editor**(such as [Sublime Text](http://www.sublimetext.com/)) installed on your computer. You should be able to use it to open and edit files of Python code.

See the [Technology Requirements](https://www.udacity.com/tech-requirements) for using Udacity.
***

# Syllabus

## Lesson 1: Data and Tables
***

In this lesson, you’ll learn about how relational databases let you structure data into tables. You’ll learn about the importance of unique keys and relationships between tables.
***
### Welcome to RDB
***
* **Relational Concepts**
***

What's a database, anyway?

How do we structure application data?

**In memeory:**

* Simple variables:

	* numbers, strings
	
* data structures:

	* lists, dictionaries, objects
	
* *Ephemeral, temporary*

**Durable Storage:**

* flat file on disk:

	* text, XML, JSON
	
* database:

	* key-value store
	* navifational DB
	* relational DB

* *Persistent, Durable*

### Relational database features:
** All DBs**

* persistem storage
* Safe concurrent access by multiple programs/users

** Relational only**

* _flexible query language with aggregation and join operations_
* _constraints - rules for protecting consistency of your data_

**Notes:**

* In relational databse the data is storage in form of tables.

* Data type and meaning  

* Data tables hold are composed of the **table header** and **table body**
	* **table header** 
	
	* **table body**
		* rows
		* columns
		
		**Note:** And each row hold a value for each column.
		
### Aggregation

**Aggragation** is simple database operation that summerize multiples rows into a single row.
	
### Common Aggregations in SQL
	
Questions and its equivalents Aggregations values.

1. Hom many rows? -> **count**
2. What's the average? -> **avg**
3. what's the greatest? -> **max**
4. what's the least? -> **min**

### Queries and Results 

1. **Querie definition and what it means in databases?**

2. **Table Structue**

3. **How Queries Happen?**
	* **Your Code** ->  _Query [SQL]_ -> **database** -> _result [table]_ -> **your code**

**Note:** Depending the enviroment the database can be talking to a database over the network or or can be calling a library in a local disk.

**Database**
 
* mySql
* postgreSQL
* oracle, etc
	* [**Your code**] --> query -- **_TCP/IP Network_** --> [**DB Server**]=[**Data on disk**] --> result **_TCP/IP Network_** --> [**Your code**]
	
* sqlite
	* [**Your Code**] -> <- [**DB library**]=[**Data on disk**]

**NOTE:** All the Databases work the same, no matter how the different environments are implemented. They all have the same Relational Databases **RDB** principles.

**Related Tables** queries that combined two tables with some piece of information from both tables make another table or **joined quierie/table**

**Uniqueness and Keys** 

* we need unique values to relate rows in one table to another.

* A column that uniquely identifies the rows in a table can be called a **Primary key**, so _Numerical IDs_.

**Joining Tables**

```
SQL
	select
		animals.name,
		animals.species,
		diet.food
	from animals join diet
	on animals.species = diet.species;
	
	where food = 'fish';

```

***
* **SQL Queries**
***

***
* **Python DB-API**
***

***
* **More SQL**
***

***
* **Final Project**
***

## Lesson 2: _Elephants_ Elements of SQL

In this lesson, you’ll begin learning SQL, the Structured Query Language used by most relational databases. You’ll learn about the select and insert statements, the basic operations for getting data out of a database and putting data into a database. You’ll learn about the operators and syntax available to get the database to scan and join tables for you.
***

```
	# Try out this query! You'll see the results below.
	# You'll be seeing many more pages like this in the rest of this lesson.
	# For now, just test it out.

QUERY = '''
select name, birthdate from animals where species = 'gorilla';
'''
```
[Lesson-2 Reference](https://www.udacity.com/wiki/ud197/lesson-2)

### Data type in SQL World

There are lots of types in SQL. Just to name a few data types:

**text** - a string of any length, like **Python's** _str_ type. Values are written in 'single quotes'.

## SQL Data Types

Here's just a sampling of the many data types that SQL supports. We won't be using most of these types in this course, though.

The exact list of types differs from one database to another. For a full list of types, check the manual for your database, such as this one for PostgreSQL.

### Text and string types

* **text** — a string of any length, like Python **str** or **unicode** types. 
* **char(n)** — a string of exactly n characters. 
* **varchar(n)** — a string of up to n characters.

### Numeric types

* **integer** — an integer value, like Python **int**. 
* **real** — a floating-point value, like Python **float**. Accurate up to six places. 
* **double precision** — a higher-precision floating-point value. Accurate up to 15 decimal places. 
* **decimal** — an exact decimal value.

### Date and time types

* **date** — a calendar date; including year, month, and day. 

* **time** — a time of day. 

* **timestamp** — a date and time together.
***

### Select statement

The most basic form of the **select** statement is to select a single scalar value:

**select** 2 + 2 ;

More usefully, we can select one or more columns from a table.  With no restrictions, this will return all rows in the table:

**select** name, species **from** animals ;

Columns are separated by commas; use * to select all columns from the tables.

Quite often, we don't want all the data from a table.  We can restrict the rows using a variety of select clauses, listed below. There are also a wide variety of functions that can apply to columns; including aggregation functions that operate on values from several rows, such as **max** and **count**.

#### where

The **where** clause expresses restrictions — filtering a table for rows that follow a particular rule. **where** supports equalities, inequalities, and boolean operators (among other things):

* **where species = 'gorilla'** — return only rows that have 'gorilla' as the value of the species column.
* **where name >= 'George'** — return only rows where the name column is alphabetically after 'George'.
* **where species != 'gorilla' and name != 'George'** — return only rows where species isn't 'gorilla' and name isn't 'George'.

#### limit / offset

The **limit** clause sets a limit on how many rows to return in the result table. The optional **offset** clause says how far to skip ahead into the results. So **limit 10 offset 100** will return 10 results starting with the 101st.

#### order by

The **order by** clause tells the database how to sort the results — usually according to one or more columns. So **order by species, name** says to sort results first by the species column, then by name within each species.

Ordering happens before limit/offset, so you can use them together to extract pages of alphabetized results. (Think of the pages of a dictionary.)

The optional **desc** modifier tells the database to order results in descending order — for instance from large numbers to small ones, or from Z to A.

#### group by

The **group by** clause is only used with aggregations, such as **max** or **sum**. Without a **group by** clause, a select statement with an aggregation will aggregate over the whole selected table(s), returning only one row. With a group by clause, it will return one row for each distinct value of the column or expression in the **group by** clause.

#### having

The **having** clause works like the **where** clause, but it applies after **group by** aggregations take place. The syntax is like this:

**select** columns **from** tables **group by** column **having** condition ;

Usually, at least one of the columns will be an aggregate function such as **count**, **max**, or **sum** on one of the tables' columns. In order to apply **having** to an aggregated column, you'll want to give it a name using **as**. For instance, if you had a table of items sold in a store, and you wanted to find all the items that have sold more than five units, you could use:

***select name, count('*Asterids') as num from sales having num > 5;**

You can have a **select** statement that uses only **where**, or only **group by**, or g**roup by** and **having**, or **where** and **group by**, or all three of them!

But it doesn't usually make sense to use **having** without **group by**.

If you use both **where** and **having**, the **where** condition will filter the rows that are going into the aggregation, and the having condition will filter the rows that come out of it.

You can read more about **having** here:

http://www.postgresql.org/docs/9.4/static/sql-select.html#SQL-HAVING

## All the tables in the zoo database

**animals**

This table lists individual animals in the zoo. Each animal has only one row. There may be multiple animals with the same name, or even multiple animals with the same name and species.

* name — the animal's name (example: 'George')
* species — the animal's species (example: 'gorilla')
* birthdate — the animal's date of birth (example: '1998-05-18')

## diet

This table matches up species with the foods they eat. Every species in the zoo eats at least one sort of food, and many eat more than one. If a species eats more than one food, there will be more than one row for that species.

species — the name of a species (example: 'hyena')
food — the name of a food that species eats (example: 'meat')
## taxonomy

This table gives the (partial) biological taxonomic names for each species in the zoo. It can be used to find which species are more closely related to each other evolutionarily.

* name — the common name of the species (e.g. 'jackal')
* species — the taxonomic species name (e.g. 'aureus')
* genus — the taxonomic genus name (e.g. 'Canis')
* family — the taxonomic family name (e.g. 'Canidae')
* t_order — the taxonomic order name (e.g. 'Carnivora')

If you've never heard of this classification, don't worry about it; the details won't be necessary for this course. But if you're curious, Wikipedia articles [Taxonomy](https://en.wikipedia.org/wiki/Taxonomy_(biology)) and [Biological classification](https://en.wikipedia.org/wiki/Taxonomy_(biology)) may help.

## ordernames

This table gives the common names for each of the taxonomic orders in the taxonomy table.

* t_order — the taxonomic order name (e.g. 'Cetacea')
* name — the common name (e.g. 'whales and dolphins')
***
## Insert statement

The basic syntax for the **insert** statement:

**insert into** table ( column1, column2, ... ) **values** ( val1, val2, ... );

If the values are in the same order as the table's columns (starting with the first column), you don't have to specify the columns in the insert statement:

**insert into** table **values** **(** val1, val2, ... **);**

For instance, if a table has three columns **(a, b, c)** and you want to insert into **a** and **b**, you can leave off the column names from the **insert** statement. But if you want to insert into b and c, or a and c, you have to specify the columns.

A single **insert** statement can only insert into a single table. (Contrast this with the **select** statement, which can pull data from several tables using a join.)






## Lesson 3: Python DB-API

In this lesson, you’ll learn how to access a relational database from Python code. You’ll use a virtual machine (VM) running on your own computer to run a Python web application, and adapt that application to use a database backend. Then you’ll learn about some of the most common security pitfalls of database-backed applications, including the famous [Bobby Tables](http://xkcd.com/327/). This lesson also covers the SQL **update** and **delete** statements.

## Lesson 4: Deeper Into SQL

In this lesson, you’ll learn how to design and create new databases. You’ll learn about normalized design, which makes it easier to write effective code using a database. You’ll also learn how to use the SQL **join** operators to rapidly connect data from different tables.

## Lesson 5: Final Project

In this project, you’ll use your Python and SQL knowledge to build a database-backed Python module to run a game tournament. You’ll design the database schema and write code to implement an API for the project.