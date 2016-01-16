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

