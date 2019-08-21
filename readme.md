# Python Essential Training
=========================
Lynda.com
=========================
Instructor: Bill Weinman
=========================

## Introduction

Python is a modern, object-oriented scripting language. It was developed in late 1980s by Dutch researcher Guido van Rossum, who is referred to as "BDFL: Benevolent Dictator For Life" by python developer community. 

One key note: Python uses whitespace and indentation to seperate blocks of code. In other languages, curly braces are used to seperate blocks of codes. However, in python it is done through indentation. So, same block should have the same indentation.

Anther key note: Blocks do not specify scope in python. However, functions, objects, and modules define scopes.

## Core Philosophies

	* Beautiful is better than ugly
	* Explicit is better than implicit
	* Simple is better than complex
	* Complex is better than complicated
	* Readability counts

## Statement vs Expression

Statement is a unit of execution. In python statement, statement is line of code.
Experssion is a unit of evaluation. 
	Example:		
          ```python
          x = y
					x * y
					true
					f()
					(x, y)
          ```

## Loops

There are two basic types of loops in python:
	while loop:		tests a conditional expression and the body of the loop is executed as long the conditional expression remains true.
	For loop:		it iterates over a sequence. The body of the loop is executed for each element of the sequence.

### Additional Controls for Loops

There are three additional controls for a loop:
	continue:		shortcut a loop and restart a loop from next step
	break:			break out of a loop
	else:			executes only loop ends normally

## Functions

Function definitions start with the keyword 'def' followed by the name of the function, which is followed by a set of parenthesis that includes all the paramters. In the following line, indent the code and start putting in the code block.

To call a function, just type the name of the function and put in the arguments inside the parenthesis.

All functions return a value. If we don't anything explicitly from a function, the function returns 'None'.

We can put a default value for a parameter in the function declaration. Like this:
	def kitten(a, b = 1)
Here, parameter 'b' has a default value of '1'. So, when calling the function, if we don't provide an argument for 'b', the value of 'b' will be considered '1'. 

Note to remember: default parameter CAN'T be followed by non-default parameter. 

In python, when a parameter is passed, it can be passed in two method:
	1. Pass-by-value: A copy of the object is created and passed to the function. However, to manage its memory, Python doesn't create new objects, rather point to the same object, unless the value of an IMMUTABLE object is changed from within that function. If the value of that immutable object is changed, then python creates that object in the memory and reassigns to the variable.
	2. Pass-by-reference: If an object is mutable, then uses pass-by-reference. In this case, it just replaces the old object with the new object.

Other types of arguments can include:
	1. List arguments: a list/tuple or simply variable number of arguments can be passed to a function. To receive this arguments list, we need to type '*args' in the function declaration.
	2. Keyword arguments: These type of arguments uses 'dictionary' instead of tuples/lists. To receive this arguments keyword list, we need to type '**kwargs' in the function declaration.

## Decorator Function

In Python everything is an object, including the functions. So, we can pass around functions into another function. This is used in Decorators. Decorator function is a feature of Python that lets the developer add features to an already developed function. 

In a Decorator function, there are at least two functions:
	1. Wrapper function: This is the function that receives another function as parameter. Then does something with that function.

	2. Core function: This is the function that is actually passed to the wrapper function and that got its functionality enhanced. After implementing the Decorator, this function can't be called on stand-alone basis anymore. Rather, everytime it is called the wrapper function is called, which in turn calls this core function from within.

## Class and Object

Class is a definition and object is the instance of class. 

While creating methods for the class, the first argument in each of the method should be self. This is to access the object itself from within the method.

To create an object from the class, we call the name of the class and put parenthesis after that.
	donald = Duck()

The definition of Constructor is done by __init__ keyword:
	```python
  def __init__(self, **kwargs):
	    self._type = kwargs['type'] 
	    self._name = kwargs['name']
	    self._sound = kwargs['sound']
  ```
In this type of constructor, the constructor is passed a dictionary-type constructor. In the constructor, we are filtering out the name of the property and assigning the parameters to the properties. In this scenario, the properties can be passed to the constructor in any order as long as the names of the properties are in used.

In this way, the properties can also be given default values, like this:
	```python
  def __init__(self, **kwargs):
	    self._type = kwargs['type'] if 'type' in kwargs else 'tiger'
	    self._name = kwargs['name'] if 'name' in kwargs else 'hunter'
	    self._sound = kwargs['sound'] if 'sound' in kwargs else 'roar'
  ```
There is no way in python to declare variables as private. So, we can assign the variables in constructors and methods. These variables are 'Object Variables', which change from object to object. However, if we want 'Class Variables', which doesn't change from object to object (same for a class), we need to declare the variable outside any method by inside the class declaration.

Reference: [Special Methods](https://docs.python.org/3/reference/datamodel.html#special-method-names)

Classes can be inherited from other classes. The class from which another class is inherited is called 'Base Class'. When working with a base class, we don't need to assign values to object variables. The constructor of the base class can be defined like this:
	def __init__(self, **kwargs):
	    if 'type' in kwargs: self._type = kwargs['type']
	    if 'name' in kwargs: self._name = kwargs['name']
	    if 'sound' in kwargs: self._sound = kwargs['sound']
The class that inherits from the base class is called, 'Derived Class'. In the derived class definition, we need to pass the name of the base class to class like this:
	class DerivedClass(BaseClass):

Then in the constructor of the derived class, we need to invoke the base class constructor with the arguments that the derived class need to pass to the base class. 
	super().__init__(**kwargs)

Data Types

In python all types are classes. If we use the 'type' function to print out the type of the data, we would see something like this:
	<class 'int'>

Python uses a form of Dynamic Typing, sometimes called DucTyping. In this method, the type of the variable is determined by the value itself.

There are different type of data, including:
	* 'int' for integer
	* float
	* 'str' for string
	* 'None' for nothing
	* 'bool' for boolean

String

String in python can be surrounded by single quote or double quote. Both carry the same meaning. If you want to write multiple line string, you can use three single quotes at the begining and three single quotes at the end of the string, like this:
	x = """ This is the first line
	This is the second line
	This is the third line
	"""

String class has some built-in methods:
	.upper() 		to make whole string upper case
	.lower()		to make whole string lower case
	.capitalize()	to make the first letter upper case
	.format()		to format the string, like this:
		x = 'seven "{1:<9}" "{0:>9}"'.format(8,9)
			In this string, the first placeholder {1:<9} inserts the first paramter '8' then left aligns it and makes the width of the field 9. In the second placeholder, {0:>9}, the second parameter '9' was inserted and have a width of 9.

Numeric Types

There are two basic numeric types in python, int and float. Numberics types are automatically casted (promoted or narrowed) based on the results.

While working with the floating point number type, the python interpreter may sacrifice accuracy for precision. This also has to do with the way computer keeps track of floating-point numbers. So, if we do this:
	0.1 + 0.1 + 0.1 - 0.3
we might not '0' rather we might see some gibberish number. To get around this problem, we can import the 'decimal' library into the program, like this:
	from decimal import *
Then create objects of the Decimal classes by passing strings of numbers to it, like this:
	a = Decimal('.01')
	b = Decimal('.03')
Then we can do this:
	a + a + a - b
and we will get '0' as answer. Also, if you check the type of the variable, you will get 'decimal.Decimal'

Boolean type

Bool type is for logical tests. Boolean variable can be either True or False. There are certain things that are considered as False in python:
	* None Type
	* number zero
	* empty string

Sequence/Data Structure

Python provides some sequence types, including:
	* Lists: mutable/changeable, assigned using []
	* Tuples: immutable/non-changeable, assigned using ()
	* Range: immutable, creats values in a sequence. this has three overloaded functions:
		1. range(end_point): starts at 0 and ends at end_point
		2. range(start, end): start at 'start' and ends at 'end'
		3. range(start, end, step): start at 'start', ends at 'end' and steps each number by 'step'
	* Dictionary: mutable, key-value pair. Dictionaries can be created using either of the two ways:
		* Basic way:
			animals = { 'kitten': 'meow', 'puppy': 'ruff', 'lion': 'grrr', 'giraffe': 'I am giraffe', 'dragon': 'rawr' }
		* Constructor way:
			animalsAlt = dict(kitten='meow', puppy='ruff', lion='grrr', giraffe='I am giraffe', dragon='rawr')

Conditional Statement

Python uses if..elif..else statements. This works just like any other if..else statements. The syntax of if statement looks like:
	if True:
		print('True')
	elif False:
		print('False')
	else:
		print('neither True or false')

However, there is no 'switch..case' statement in python.

Comparison Operators

Python has the following operators:
	==		equal
	!=		not equal
	<		less than
	>		more than
	<=		less than or equal
	>=		greather than or equal

Logical Operators

	and 	and operator
	or 		or operator
	not 	not operator

Identity Operator

	is  	true if same object
	is not 	true if not same object

Membership Operator

	in 		True if 'left' is a member of 'y'
	not in 	True if 'left' is not a member of 'y'

Ternary Opertor

	x = [true_statement] if [condition] else [false_statement]

Arithmatic Operators

	+ 		addition
	- 		subtraction
	* 		multiplication
	/		division
	//		integer division
	% 		modulo
	**		exponent
	-		unary negative
	+		unary positive
	
Bitwise Operator

	&		bitwise and
	| 		bitwise or
	^ 		bitwise Xor
	<<		shift left
	>>		shift right

Operator Precedence

Higher to lower precedence:
	** 				Exponent
	+x, -x 			Positive, Negative
	*, /, //, %		Multiplication, division, remainder
	+, -			Addition, subtraction
	<<, >> 			Bitwise shifts
	& 				Bitwise AND
	^ 				Bitwise XOR
	| 				Bitwise OR
	in, not in,
	is, is not, 
	<, <=,
	>, >=,
	!=, == 			Comparisons, membership test, identity test
	not x 			Boolean NOT
	and 			Boolean AND
	or 				Boolean OR
REFERENCE: https://docs.python.org/3/reference/expressions.html#operator-precedence

Error Handling

When ever we are running a program, we may face different types of errors. Our programs may stop working because of some errors. To keep continue running the program, we can handle the error with try...except block, like this:
	try:
		x = 5 / 0
	except ValueError:
		print('I caught a ValueError')
	except ZeroDivisionError:
		print("don't divide by zero")
	except:
		print('unknown error')
	else:
		print('good job')
		print(x)

In the try block, we put in the piece(s) of code that we think may generate an error. This is followed by 'except' block with the type of error we are expecting (except ValueError:) followed by the piece of code that we want to run to handle the error. If we don't know the type of the error, we can use the generic except (except:). If we want to execute a piece of code when there is no error in the execution, we can put that in the 'else' block (else:). To know more about the error, we can import the 'sys' library, like this:
	import sys
Then we get some additional information about any error, like: sys.exc_info().

File I/O

Python can be used to read from and write to files. For this we need to first 'open' the file, like this:
	f = open('lines.txt')
This function also takes a second argument, which would be either 'r' for read, 'w' for write, or 'a' for append. There is an optional '+' sign after these letters, which enable both read and write for the file. There is also an optional 't' for text files or 'b' for binary files.

The 'open' method will return a iterator file object. So, we can loop over that item to read each of the lines, like this:
	for line in f:
		print(line.rstrip())

The 'rstrip' method removes any whitespace or line ending characters from the end of the line.


To 'write' lines to another file, we first need to create a file object with the output file, like this:
	outfile = open('lines_copy.txt', 'wt')
Then, we can simply put a print function inside the for-loop, like this:
	print(line.rstrip(), file=outfile)

We can also use the 'writelines()' method of the file object to write the lines to the files:
	outfile.writelines(line)

After reading from or writing to a file, we need to close that file with the "close" method of the file object:
	outfile.close()

While reading the binary files and writing to the binary file we need to read in chunks. like this:
	buf = infile.read(10240)
Then check if the 'buf' exists. If it does, "write" the 'buf' to the output file:
	if buf:
		outfile.write(buf)

