'''
This file is made up of alternating blocks of comments (such as these lines)
and blocks code. 

To run the blocks of code you are best copying the block you want to run into
a separate file and running that, overwriting the previous contents at each 
time.

The following 3 lines of code are just here to prevent you from running this
file by accident. You can ignore these 3 lines for the time being.
'''

import sys
print("Don't try to run this file")
sys.exit()

'''
For most of the course we'll work in Python files, as opposed to the REPL (when
you type "python" in the terminal).

When Python executes a file, it will compile it in memory.
If the code in the file does not follow Python's syntax rules, this step will fail, none of the code will even run, and you will get a SyntaxError indicating
which line the error is on.

Line numbers are sometimes misleading (e.g.  you forgot a closing bracket, that
only becomes an error when it reaches a line where it definitely expected it)

If there are no syntax errors, Python will execute each line from top to bottom
until:
  - An error occurs (in which case it prints out the error type, the line where
    it occured, and an informative message)
  - There is a prompt for input (which pauses execution)
  - You explictly ask it to exit (like we did with the 3 lines of code above)
  - It reaches the end of the file (nothing special happens at this point)

Let's look at some Python code:
'''

print(99)

'''
Here we simply told Python to print the number 99, which it will do and
then exit because there are no more lines.

"print" is a function (more on this later) which prints values to the output
(usually the terminal, or a tab in your IDE). It is useful for examining
what's inside a variable, whether for learning or debugging.

If you are using Python2 the brackets are optional. In Python3 they are 
mandatory.

Let's do something more interesting:
'''

a = 2
b = 3
print(a)
print(b)

'''
Here we created 2 variables and then told Python to print them.

Running this should have printed this:
2
5

Variables are how we keep track of values or "data". A computer program is 
simply a bunch of operations on data (some of which gets sent to other places
like to the hard drive so it can be stored, or to the screen which displays graphics)

To keep track of values, we need to give them names. Or rather, we need register
names that we want to use (in this case a and b) and point them to the value.

Whenever we use that name elsewhere, such as in the calls to print, Python know
which value to use.

You can overwrite the variable by assigning another value to it:
'''

a = 2
print(a)
a = 3
print(a)


'''
Using the = sign assigns the value on the right, to the variable on the left,
which either create the variable if it wasn't previously defined, overwrites
the previous value if it was. 

What you are actually doing under the hood is telling Python to "point" the
variable to a different value. They are called variables exactly because you
can change what value they point to, else they would be constants, which we
don't really have in Python.

If you try to access a name which you haven't declared, you get an error:
'''

a = 2
print(c) 

'''
Here we tried to print c, however c was never defined, so we get a NameError.

Some programming languages require you to declare all the variables names up 
front before you can save values to them. In Python a variable pops into 
existence as soon as we we assign a value to it.

Every value also has a "type", so far we have only used integers. There 
are many types, the main ones being:

  - string (i.e. text, or a "string" of characters)
  - float (number with a floating point decimal)
  - boolean (True or False)
  - tuple (an array of values, immutable)
  - list (like a tuple, but mutable)

We'll look at these in more detail later.

What you can do with variables depends on their type. Let's look at some 
things we can do with integers:
'''

a = 2
b = 3
d = a + b
print(d)

'''
Here we performed an addition, and saved the result to a new variable.

Note that we could have printed the result directly, without saving to a
variable:
'''

a = 2
b = 3
print(a + b)

'''
Study the code carefully. What this shows us is that wherever we require
a value (such as in the brackets for print) we can supply a named variable,
or an operation which will result in a variable.

Why would we choose one over the other? 
 - Perhaps we want to reuse that value later without repeating the add
 - Perhaps it helps keep code clear

Let's look at why we might want to do the latter: 
'''

a = 2
b = 3
print(a + b * 2)

'''
Here we wanted to print the result of adding a and b, then multiplying that
by two.

The problem is that the multiplication operand (*) takes precedence over
the addition operand (+) so it give 8 instead of 10.

One solution would be to use brackets:
'''

a = 2
b = 3
print((a + b) * 2)

'''
Another solution would be to save the result of adding a & b to a variable
before multiplying it by two:
'''

a = 2
b = 3
total = a + b
print(total * 2)

'''
Why would we choose one over the other?

Python doesn't care, so long as it's correct (in fact, when you used brackets
Python converted that to a variable internally, we just never got access to it)

The whole point of Python is READABILITY. Code that is easy to read is easy
to follow, less likely to hide bugs, and easier to fix if you find there
is a bug.

Create variables with good names wherever it helps make your code easier to
follow.

You can also use brackets to make your code easier to follow, even when they
are not necessary:
'''

a = 2
b = 3
print(a + b - 8 / 2 * 2)

'''
What are we trying to achieve with the above?

It could be that Python interprets this the exact way we want it... 

But it's hard to follow, and if things go wrong you will question whether it is
doing what it is intended, and you can only answer that if you know what was
intended in the first place!

Therefore, always make your code a unambiguous as you can. Either one of the
following is an improvement on the previous:
'''

print(a + b - (8 / 2) * 2)
print(a + b - ((8 / 2) * 2))

'''
Remember, Python doesn't care so long as it's correct. The difference between
good code and bad code is how easy it is for the human to avoid or make mistakes

Let's look at more operations:
'''

a = 3
b = 3
print(a > 3)
print(a == 3)
print(a != 3)
print(a >= 3)

'''
These operands don't produce integers like add or multiply do, but return
a boolean value (i.e. true or false).

Note how the equality operand is == as opposed to = which is used for assigning
a value to a variable. 

You can assign a boolean value to a variable directly too, just remember that
python calls them True and False not true and false (case matters everywhere
in Python)
'''

a = True
b = False

'''
Booleans are most often used for conditional logic, which mostly involves
running, skipping or repeating lines of code depending on whether some
codition is true or false.

The most basic for is the if statement:
'''

a = True
b = False
if a:
    print("a is True")
if b:
    print("b is True")

'''
As it stands, the snippet above will only print "a is True". Try changing the
values of a and b and you will see different output.

The "if" keyword requires a value (or a variable, or an operation which returns
a value) which it will evaluate to True or False.

If True, then the "indented block" of code will run.

An indented block is one or more lines of code following a lines which ends
with a colon ":" symbol (every line with "if" must end with ":") and that all
start with the same amount of whitespace characters.

Let's look at this in more detail:
'''

a = True
if a:
    print("a is True")
    print("Yep, most definitely True")
print("All done now.")

'''
Here the indented block consists of two lines (the first two print statements).
It starts immediately after the ":" symbol, and includes all lines with the
same indentation, and finishes when we reach a line whose indentation returns
back to the same point where the initating "if" line started.

So if a is True, all 3 print statements fire, if a is False, the first two are
skipped and it jumps straight to the last print statement.

Technically, Python doesn't care how many whitespace characters there are,
so long as it is the same for every line in the block.

Why do we talk about "whitespace characters", why not just say "spaces"?

Tab is a whitespace character (so are line breaks and new line markers, but by
definition you'll never find these before the text in a line). It is hard
to tell if "    " is a tab or 4 spaces.

Use your keyboard arrows to move the cursor around the whitespace preceding
the following lines, note how the cursor jumps over tabs.

	<<< This is 1 tab character (total: 1 character)
    <<< This is 4 space characters (total: 4 characters)
        <<< This is 8 space characters (total: 8 characters)
    	<<< This is 1 tab and 4 spaces (total: 5 characters)

So visually the first two and last two lines above look indented the same
as each other, but Python sees it differently, and will give you an
IndentationError

As you can see, using a mix of tabs and spaces will wreak havoc on your code, 
so it is best to stick to one or the other. But because you will be copying 
code from the Internet and other sources it makes sense if everyone sticks
to one camp, so the decision was made to use 4 spaces, and REALLY SHOULD
stick to that.

Using 2 spaces instead of 4, which some people do, makes it very difficult to
copy & paste in and out of your code. 

Of course, no one wants to hit the space bar 4 times for each line, so the trick
is to set your editor to conver tab keys to 4 spaces automatically. Most editors
allow this, and many allow it just for python files. Python IDEs will typically
do this by default.

You can have indented blocks within indented blocks, technically to ridiculous
depths, but if it gets too deep you should really think about restructuring
your code.
'''

a = True
b = False
if a:
    if b:
        print("Both a and b are True")
    print("Only a is True")
if b:
    print("Only b is True")

'''
A good way to follow the code above is to think of water flowing down a 
series of pipes, where the valves can be open or closed, in which case
the water flows back up the pipe and tries the next path down.

Let's recap what kind of expressions you can use in an if statement

You can use any operation which returns a boolean value:
'''

a = 6
if a > 4:
    print("whatever")

if a == 6:
    print("whatever")

'''
Or you can save the boolean to a variable as we have done so far:
'''

a = 6
b = a > 4
if b:
    print("whatever")

'''
Do not rely on integers, always use booleans (or None, see later)

See what happens with these examples, it might surprise you.
'''

a = 1
if a:
    print("whatever")
a = 0
if a:
    print("whatever")
a = -1
if a:
    print("whatever")

'''
Note that there is no need check if boolean == True:
'''

a = 6
b = a > 4

# bad:
if b == True:
    print("whatever")

# good:
if b:
    print("whatever")

'''
Nor should you check if boolean == False. Use "not" instead:
'''

a = 6
b = a == 6

# bad:
if b == False:
    print("whatever")

# good:
if not b:
    print("whatever")

'''
The "not" keyword converts True into False and vice versa.

There are other logical operators, the first is "and" which returns
True if the expressions on either side are BOTH True:
'''

a = 7
if a > 5 and a < 10:
    print("a is greater than 5 but less than 10")

'''
This is how you check if a number is between two values in Python.

The next operator is "or", which returns True if EITHER of the expressions
on either side is True:
'''

a = 7
b = 5
if a > 5 or b > 5:
    print("One of those is greater than 5")

'''
Be very careful with what you are asking Python to do with this.

Many people make the following mistake:
'''

a = 7
b = 5
if a or b > 5:
    print("One of those is greater than 5")

'''
Here we are asking Python to evaluate two things:

whether a is True (which it will be if it is anything other than 0)
whether b is greater than 5

This code will behave correctly with some inputs, but incorrectly with others
and this is a situation you really want to avoid as it is hard to spot.
We say this "works by coincidence" and you'd be amazed how often this happens.

A variation on the above mistake is this:
'''

a = 7
if a == 5 or 10:
    print("a is 5 or 10")

'''
Here we are asking Python to evaluate two things:

whether a is equal to 5
whether 10 is True (which it always is)

Be sure to read through your code carefully, and check it with various
variables, especially the bordeline cases, so with numbers you want to 
check these in particular: 1, 0, -1

You can combine logical operations:
'''

a = 7
if a < 5 or a > 10 and a < 20:
    print("a is less than 5 or between 10 and 20")

'''
The above code works because of the way Python evaluates it, but to the
reader it is possibly ambiguous. 

As with operations, you can use brackets to make things clearer:
'''

a = 7
if a < 5 or (a > 10 and a < 20):
    print("a is less than 5 or between 10 and 20")

'''
Or save these to variables:
'''

a = 7
less_than_5 = a < 5
between_10_and_20 = a > 10 and a < 20
if less_than_5 or between_10_and_20:
    print("a is less than 5 or between 10 and 20")

'''
The more complex your code, the more worthwhile saving things to variables
for clarity. Aim to make your code simple, rather than complex or clever.

The if statement has a counterpart called "else":
'''

x = -4
if x > 0:
    print("x is positive")
else:
    print("x is negative")

'''
The same rules of ending the line with the ":" symbol and indenting lines
underneath to form a block apply.

An if/else statement guarantees that one (and only one) of the indented blocks
will run.

You can have indented blocks within else statements too:
'''

x = -4
if x > 0:
    print("x is positive")
else:
    print("x is negative")
    if x < -100:
        print("like, really negative")

'''
Every else statement must correspond to an if statement at the same level of
indentation.

Look at the following example:
'''

x = 15
if x > 10:
    print("x is big")
    if x > 100:
        print("like, really big")
    else:
        print("it is between 10 and 100")

'''
Here the else statement is triggered if x is not greater than 100.
If we unindented it all the way back, it would trigger if x is not greater
than 10 instead:
'''
x = 15
if x > 10:
    print("x is big")
    if x > 100:
        print("like, really big")
else:
    print("it is less than 10")

'''
The else statement does not take an expression, it's just "else" followed
straight by a colon. 

If you want conditions, you can use the elif (short for else if) statement:
'''

x = 15
if x > 100:
    print("x is more than 100")
elif x > 10:
    print("x is more than 10")
elif x > 5:
    print("x is more than 5")
else:
    print("x is less than 5")

'''
You can chain as many of these together, and it does not need to finish
with an else, but it's good practice to do so.

Note that elif expressions will only be evaluated if the previous if statement
is false. In our example, if x is more than 100, it won't check the rest.

Consider this snippet:
'''

x = 150
if x > 100:
    print("x is more than 100")
elif x > 1000:
    print("x is more than 1000")
else:
    print("x is less than 100")

'''
The above will not work, because if x is greater than 100, the "if" is true,
so the "elif" never gets evaluated

Try changing it to get it do work correctly.

One thing to be careful of is assigning variables inside conditional blocks
as they will not exist if the block does not run:
'''

x = 10
if x > 10:
    message = "a is more than 10"
elif x > 100:
    message = "a is more than 100"
print(message)

'''
The above will throw a NameError if x is not greater than 10, because Python
never hits any of the lines which assigns a value to the variable "message".

Either make sure you include an else statement, or initialise the variable:
'''

message = ""
x = 10
if x > 10:
    message = "a is more than 10"
elif x > 100:
    message = "a is more than 100"
print(message)

'''
This is not useful, but it avoids the NameError. 

A common convention is to initialise variables to None, which is Python's
way of indicating the absence of any value (the variable exists, but it 
contains nothing, or rather it points to a special value called None, which
Python understands to mean "no value").
'''

message = None

'''
To check if a value is None, you can use == or "is".
'''

message = None
x = 10
if x > 10:
    message = "a is more than 10"
elif x > 100:
    message = "a is more than 100"

if message is None:
    pass
else:
    print(message)

'''
Here we used the keyword "pass" which does nothing, and just allows us to
place an indented block because Python requires it, even though we don't
want to do anything in it.

It is also a useful place holder for when you're deciding how to structure
your code.

A better way to write the above however, would be this:
'''

message = None
x = 10
if x > 10:
    message = "a is more than 10"
elif x > 100:
    message = "a is more than 100"

if message is not None:
    print(message)