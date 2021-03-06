# -*- coding: utf-8 -*-
"""d2pm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/ardhiraka/FSDS_Guidelines/blob/master/p0/w1/d2pm.ipynb

# Week 1: Day 2 PM // Python: Looping

**Iteration** means executing the same block of code over and over, potentially many times. A programming structure that implements iteration is called a loop.

In programming, there are two types of iteration, indefinite and definite:

- With **indefinite iteration**, the number of times the loop is executed isn’t specified explicitly in advance. Rather, the designated block is executed repeatedly as long as some condition is met.
- With **definite iteration**, the number of times the designated block will be executed is specified explicitly at the time the loop starts.

## Python "while" Loops

Let’s see how Python’s while statement is used to construct loops. We’ll start simple and embellish as we go.

The format of a rudimentary while loop is shown below:

```py
while <expr>:
    <statement(s)>
```

`<statement(s)>` represents the block to be repeatedly executed, often referred to as the body of the loop. This is denoted with indentation, just as in an if statement.

The controlling expression, `<expr>`, typically involves one or more variables that are initialized prior to starting the loop and then modified somewhere in the loop body.

When a while loop is encountered, `<expr>` is first evaluated in Boolean context. If it is true, the loop body is executed. Then `<expr>` is checked again, and if still true, the body is executed again. This continues until `<expr>` becomes false, at which point program execution proceeds to the first statement beyond the loop body.

Consider this loop:
"""

n = 5
while n > 0:
    n -= 1
    print(n)

i = 1
while i < 6:
  print(i)
  i += 1

"""Here’s what’s happening in this example:

- n is initially 5. The expression in the while statement header on line 2 is n > 0, which is true, so the loop body executes. Inside the loop body on line 3, n is decremented by 1 to 4, and then printed.

- When the body of the loop has finished, program execution returns to the top of the loop at line 2, and the expression is evaluated again. It is still true, so the body executes again, and 3 is printed.

- This continues until n becomes 0. At that point, when the expression is tested, it is false, and the loop terminates. Execution would resume at the first statement following the loop body, but there isn’t one in this case.

### The Python break and continue Statements

In each example you have seen so far, the entire body of the while loop is executed on each iteration. Python provides two keywords that terminate a loop iteration prematurely:

- The Python break statement immediately terminates a loop entirely. Program execution proceeds to the first statement following the loop body.

- The Python continue statement immediately terminates the current loop iteration. Execution jumps to the top of the loop, and the controlling expression is re-evaluated to determine whether the loop will execute again or terminate.

The distinction between break and continue is demonstrated in the following diagram:

<img src='https://files.realpython.com/media/t.899f357dd948.png' />
"""

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break # Break Statement
    print(n)
print('Loop ended.')

"""When n becomes 2, the break statement is executed. The loop is terminated completely, and program execution jumps to the print() statement on line 7.

The next script, continue, is identical except for a continue statement in place of the break:


"""

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')

"""This time, when n is 2, the continue statement causes termination of that iteration. Thus, 2 isn’t printed. Execution returns to the top of the loop, the condition is re-evaluated, and it is still true. The loop resumes, terminating when n becomes 0, as previously.

### The else Clause
Python allows an optional else clause at the end of a while loop. This is a unique feature of Python, not found in most other programming languages. The syntax is shown below:

```py
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
```
The `<additional_statement(s)>` specified in the else clause will be executed when the while loop terminates.
"""

n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')

"""In this case, the loop repeated until the condition was exhausted: n became 0, so n > 0 became false. Because the loop lived out its natural life, so to speak, the else clause was executed. Now observe the difference here:"""

n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('Loop done.')

"""This loop is terminated prematurely with break, so the else clause isn’t executed.

### Infinite Loops

Suppose you write a while loop that theoretically never ends. Sounds weird, right?

Consider this example:

```py
while True:
    print('foo')
```

### Nested while Loops

In general, Python control structures can be nested within one another. For example, if/elif/else conditional statements can be nested:

```py
if age < 18:
    if gender == 'M':
        print('son')
    else:
        print('daughter')
elif age >= 18 and age < 65:
    if gender == 'M':
        print('father')
    else:
        print('mother')
else:
    if gender == 'M':
        print('grandfather')
    else:
        print('grandmother')
```

Similarly, a while loop can be contained within another while loop, as shown here:
"""

a = ['foo', 'bar']

while len(a):
    print(a.pop(0))
    
    b = ['baz', 'qux']
    
    while len(b):
        print('>', b.pop(0))

"""A break or continue statement found within nested loops applies to the nearest enclosing loop:

```py
while <expr1>:
    statement
    statement

    while <expr2>:
        statement
        statement
        break  # Applies to while <expr2>: loop

    break  # Applies to while <expr1>: loop
```

Additionally, while loops can be nested inside if/elif/else statements, and vice versa:

```py
if <expr>:
    statement
    while <expr>:
        statement
        statement
else:
    while <expr>:
        statement
        statement
    statement
while <expr>:
    if <expr>:
        statement
    elif <expr>:
        statement
    else:
        statement

    if <expr>:
        statement
```

### One-Line while Loops

As with an if statement, a while loop can be specified on one line. If there are multiple statements in the block that makes up the loop body, they can be separated by semicolons (;):
"""

n = 5
while n > 0: n -= 1; print(n)

"""_____

## A Survey of Definite Iteration in Programming

Definite iteration loops are frequently referred to as for loops because for is the keyword that is used to introduce them in nearly all programming languages, including Python.

Historically, programming languages have offered a few assorted flavors of for loop. These are briefly described in the following sections.

**Numeric Range Loop**

The most basic for loop is a simple numeric range statement with start and end values. The exact format varies depending on the language but typically looks something like this:

```py
for i = 1 to 10
    <loop body>
```

Here, the body of the loop is executed ten times. The variable i assumes the value 1 on the first iteration, 2 on the second, and so on. This sort of for loop is used in the languages BASIC, Algol, and Pascal.

**Three-Expression Loop**

Another form of for loop popularized by the C programming language contains three parts:

- An initialization
- An expression specifying an ending condition
- An action to be performed at the end of each iteration.

This type of has the following form:

```py
for (i = 1; i <= 10; i++)
    <loop body>
```

This loop is interpreted as follows:

- Initialize i to 1.
- Continue looping as long as i <= 10.
- Increment i by 1 after each loop iteration.

Three-expression for loops are popular because the expressions specified for the three parts can be nearly anything, so this has quite a bit more flexibility than the simpler numeric range form shown above. These for loops are also featured in the C++, Java, PHP, and Perl languages.

**Collection-Based or Iterator-Based Loop**

This type of loop iterates over a collection of objects, rather than specifying numeric values or conditions:

```py
for i in <collection>
    <loop body>
```

Each time through the loop, the variable i takes on the value of the next object in `<collection>`. This type of for loop is arguably the most generalized and abstract. Perl and PHP also support this type of loop, but it is introduced by the keyword foreach instead of for.

## The Python for Loop

Of the loop types listed above, Python only implements the last: collection-based iteration. At first blush, that may seem like a raw deal, but rest assured that Python’s implementation of definite iteration is so versatile that you won’t end up feeling cheated!

Shortly, you’ll dig into the guts of Python’s for loop in detail. But for now, let’s start with a quick prototype and example, just to get acquainted.

Python’s for loop looks like this:

```py
for <var> in <iterable>:
    <statement(s)>
```

`<iterable>` is a collection of objects—for example, a list or tuple. The <statement(s)> in the loop body are denoted by indentation, as with all Python control structures, and are executed once for each item in `<iterable>`. The loop variable `<var>` takes on the value of the next element in `<iterable>` each time through the loop.

Here is a representative example:
"""

a = ['foo', 'bar', 'baz']
for i in a:
    print(i)

"""In this example, `<iterable>` is the list a, and `<var>` is the variable i. Each time through the loop, i takes on a successive item in a, so print() displays the values 'foo', 'bar', and 'baz', respectively. A for loop like this is the Pythonic way to process the items in an iterable."""

d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

for k in d:
    print(d[k])

for k in d.values():
    print(k)

for k, v in d.items(): 
    print(k, ":", v)

"""### Iterating Through a Dictionary

What happens when you loop through a dictionary? Let’s see:

```py
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)
```

As you can see, when a for loop iterates through a dictionary, the loop variable is assigned to the dictionary’s keys.

To access the dictionary values within the loop, you can make a dictionary reference using the key as usual:

```py
for k in d:
    print(d[k])
```

You can also iterate through a dictionary’s values directly by using .values():

```py
for v in d.values():
    print(v)
```

### The range() Function

In the first section of this session, you saw a type of for loop called a numeric range loop, in which starting and ending numeric values are specified. Although this form of for loop isn’t directly built into Python, it is easily arrived at.

For example, if you wanted to iterate through the values from 0 to 4, you could simply do this:

```py
for n in (0, 1, 2, 3, 4):
    print(n)
```

This solution isn’t too bad when there are just a few numbers. But if the number range were much larger, it would become tedious pretty quickly.

Happily, Python provides a better option—the built-in range() function, which returns an iterable that yields a sequence of integers.

range(`<end>`) returns an iterable that yields integers starting with 0, up to but not including `<end>`:

```py
x = range(5)
```

Note that range() returns an object of class range, not a list or tuple of the values. Because a range object is an iterable, you can obtain the values by iterating over them with a for loop:

```py
for n in x:
    print(n)
```

### Altering for Loop Behavior

You saw in the previous section in this session how execution of a while loop can be interrupted with break and continue statements and modified with an else clause. These capabilities are available with the for loop as well.

**The break and continue Statements**

break and continue work the same way with for loops as with while loops. break terminates the loop completely and proceeds to the first statement following the loop:
"""

for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i)

"""continue terminates the current iteration and proceeds to the next iteration:"""

for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        continue
    print(i)

"""**The else Clause**

A for loop can have an else clause as well. The interpretation is analogous to that of a while loop. The else clause will be executed if the loop terminates through exhaustion of the iterable:
"""

for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('Done.')  # Will execute

"""The else clause won’t be executed if the list is broken out of with a break statement:"""

for i in ['foo', 'bar', 'baz', 'qux']:
  if i == 'bar':
    break
  print(i)
else:
  print('Done.')