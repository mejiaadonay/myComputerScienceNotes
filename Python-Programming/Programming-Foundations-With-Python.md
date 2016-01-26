# Programming Foundations with Python
###### Learn Object-Oriented Programming
***
[**Read about Python Standard Library**](https://docs.python.org/2.7/library/index.html) but it is important to read the documentation for you Python version installed.

### Download Python (Mac)

# Installing Python
Hi there! These instructions will walk you through all of the steps needed to install Python onto your computer. This particular page contains instructions for Mac OS X.

_If you have a Windows PC, please click Previous or otherwise navigate to the previous page in order to find instructions for your particular platform! If you already have Python installed, proceed to the next lesson by clicking on Next._

1. Navigate to the [website](https://www.python.org/downloads/release/python-2710/) that holds downloads for the most recent version of Python 2, which is currently [2.7.10](https://www.python.org/downloads/release/python-2710/).

2. Download the [64-bit/32-bit installer](https://www.python.org/ftp/python/2.7.10/python-2.7.10-macosx10.6.pkg) if you're running Mac OS X 10.6 or later. Otherwise, download the [32-bit i386/PPC installer](https://www.python.org/ftp/python/2.7.10/python-2.7.10-macosx10.5.pkg).

3. Open the file that you downloaded. It should either be called `python-2.7.10-macosx10.6.pkg` or `python-2.7.10-macosx10.5.pkg`. **Note:** The images below show Python 2.7.9, but the process is unchanged for Python 2.7.10.

![alt text](http://lh6.ggpht.com/zNpKRb2WbyM7RP_Fv6BxZMlij9aD0Vewhe0_x-te33x151b_lq5UxVdgXgicTTgwsXjF-wz1Ns6M7nmvgaPm=s0#w=1486&h=920)

4. Follow the steps in the Python Installer to successfully install Python.

 ![alt text](http://lh4.ggpht.com/96REtVzkd0VRjmS2rzxIqEz8rVBTIKklVbs21N5QtdmF4iC00Ku6t33TScrpgItU--SXiOP6vgQ8Y7KH9g=s0#w=1240&h=876)

5. To confirm that your installation was successful, open IDLE, a program installed by Python that makes it easy to edit and run Python code.

	a) It should be in your Applications folder.

	![alt text](http://lh5.ggpht.com/pl_K1cZQuieaDIaCic6hsDbrlJbgCaTLtu6sfg2Zqq7GSyoOgoApTdsn99uE-ohADzMhyfcRIJP0UPgc1SA=s0#w=1540&h=874)

	b) You can also use Spotlight by pressing ⌘+Space and typing in "idle" to find it.

6. Here's a picture of it running on our computer!
  	![alt text](http://lh4.ggpht.com/KDiz0VsocUG7M5dBApNTZ6eQL9oZPCWKli-kX4i8uiI2pe_kYoQBXeikX58Ysfp6ey0OzP1GjYeXulpRqw=s0#w=1022&h=900)

7. Hooray, you're done!

***

**Helpful Tutorials**

[**- If Statements**](http://www.tutorialspoint.com/python/python_if_else.htm)

[**- Loops**](http://www.tutorialspoint.com/python/python_while_loop.htm)

[**- Functions**](http://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html)

**More Helpful Tutorials**

[**-If Statements**](https://www.udacity.com/course/viewer#!/c-cs101/l-48753036/e-48734356/m-48692680)

[**- Loops**](https://www.udacity.com/course/viewer#!/c-cs101/l-48753036/e-48686708/m-48480488)

[**- Functions**](https://www.udacity.com/course/viewer#!/c-cs101/l-48753036/m-48713484)

**Course Map**
***
*	**Functions** for example a greating function funct(){ print("Hello World!");

*	**Classes**: and object oriented programming.

***

# Lession 1 (Use Functions)

***NOTE:*** In phyton the closing semicolon is not need it as use in C/C++ and JAVA. But the include or import file is similar to JAVA imports.
***

For Windows user 

```
import os

dif rename_files():
	
	os.listdir(r"C:\OOP\prank")
```
NOTE: is important to add `r` before the path to tell python to take the string as it is and don't interpreter as other way.

[Documentation for the module os](https://docs.python.org/2/library/os.html)

[Exceptions.](http://www.tutorialspoint.com/python/python_exceptions.htm)

### Abstraction
is really powerful in programming, abstraction is when the implentation of a given function, or class is hidden from us as developer and as a user.

***
## LESSION 2a (Use Classes): Draw Turtles

**Note:** it important to use range() function in a `for loop` 
to avoid the 'int' interator problems.

```
for i in range(total)
	i++ 
```
### Change Turtle Shape, Color, and Speed

[1) Changing Turtle's Shape](https://docs.python.org/2/library/turtle.html#turtle.shape)

[2) Changing Turtle's Color](https://docs.python.org/2/library/turtle.html#turtle.color)

[3) Changing Turtle's Speed](https://docs.python.org/2/library/turtle.html#turtle.speed)

[Making Turtle Code Better](http://discussions.udacity.com/t/making-turtle-code-better-f/16123)

**What is a Class?**
a class is like a blueprint can hold certain pieces of information. An object or instad of a class is like a example or copy of a class and can hold it own information.

[Twilio Sample Code](https://www.twilio.com/docs/python/install)
(if you scroll down to the "Testing your installation" section of this page, you can copy the code we used in this video)
***

[Twilio Sign up Page](https://www.twilio.com/docs/python/install)

If you can't find the SID and Auth Token, check out the Dashboard page, then click the link, "Show API Credentials"

[How does Python Keyword from work](http://www.tutorialspoint.com/python/python_modules.htm)
[Read the actual Twilio code on Github](https://github.com/twilio/twilio-python)

[Exploring Built-In Functions](https://docs.python.org/2/library/functions.html) - Use this discussion thread to post your response.

Built-in functions in Python

**Note:** Look for twilio python on Github. 

1) [Download the movie_quotes.txt file](https://s3.amazonaws.com/udacity-hosted-downloads/ud036/movie_quotes.txt)
 
Please note that in order to download this file, you may need to right click on the link and select "Save Link As".

2) [Get the path or location of a file on a Mac](https://s3.amazonaws.com/udacity-hosted-downloads/ud036/How+to+get+the+address+of+a+file+on+a+Mac.pdf)

1) Using What Do You Love to check curse words
- http://www.wdyl.com/profanity?q=shot

2) In case you are curious about the things we are adding after the ? in the link or URL 
- http://en.wikipedia.org/wiki/Query_string

1) What Do You Love - http://www.wdyl.com/profanity?q=shot
(this website will help detect curse words in a text)

2) Pirate speech - http://isithackday.com/arrpi.php?text=friend
(this website will convert normal text into Pirate speech

[How to use list or arrays in Python](https://docs.python.org/2/tutorial/introduction.html#lists)

# Advanced Ideas in OOP
***
*Advanced Ideas in OOP*
* class variables
* 

# Vocabulary 

* class
* instance
* constructor
* self **Note** Read about self that take the default constructor.
* Instance Variables
* Instance methods

# Resoucers
**Important Note:** For every languege you use try to find a good style guide for the language like for example [Google Style Guide for Python.](https://google.github.io/styleguide/pyguide.html) You can google style guides.

*	[Pymotw.com Python Program open Webbrowser](https://pymotw.com/2/webbrowser/)
	
*	[Stackoverflow - Make Python Program Wait](http://stackoverflow.com/questions/15472707/make-python-program-wait)


*	[How to use a loop in Python](http://www.tutorialspoint.com/python/python_while_loop.htm)

*	[tack Overflow Help Page](http://stackoverflow.com/questions/3207219/how-to-list-all-files-of-a-directory-in-python)	

*	[TutorialPoint](http://www.tutorialspoint.com)


















