# -*- coding: utf-8 -*-
"""d2am.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/ardhiraka/FSDS_Guidelines/blob/master/p0/w1/d2am.ipynb

# Week 1: Day 2 AM // Python: Conditions, Control Flow

## Conditional

Python supports the usual `logical conditions` from mathematics:

- Equals: a == b
- Not Equals: a != b
- Less than: a < b
- Less than or equal to: a <= b
- Greater than: a > b
- Greater than or equal to: a >= b
- These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the `if` keyword.

In a Python program, the `if statement` is how you perform this sort of **decision-making**. It allows for conditional execution of a statement or group of statements based on the value of an expression.

### Introduction to the if Statement

We’ll start by looking at the most basic type of if statement. In its simplest form, it looks like this:

```py
if <expr>:
    <statement>
```

In the form shown above:

- `<expr>` is an expression evaluated in Boolean context.
- `<statement>` is a valid Python statement, which must be indented.

If `<expr>` is true (evaluates to a value that is “truthy”), then `<statement>` is executed. If `<expr>` is false, then `<statement>` is skipped over and not executed.

Note that the colon `(:)` following `<expr>` is required. Some programming languages require `<expr>` to be enclosed in parentheses, but Python does not.
"""

x = 0
y = 5

if x < y:                            # Truthy
    print('yes')

if y < x:                            # Falsy
    print('yes')

if x:                                # Falsy
    print('yes')

if y:                                # Truthy
    print('yes')

if 'aul' in 'grault':                # Truthy
    print('yes')

if 'quux' in ['foo', 'bar', 'baz']:  # Falsy
    print('yes')

"""### Grouping Statements: Indentation and Blocks

So far, so good.

But let’s say you want to evaluate a condition and then do more than one thing if it is true:

If the weather is nice, then I will:

- Mow the lawn
- Weed the garden
- Take the dog for a walk

(If the weather isn’t nice, then I won’t do any of these things.)

In all the examples shown above, each if `<expr>`: has been followed by only a single `<statement>`. There needs to be some way to say “If `<expr>` is true, do all of the following things.”

The usual approach taken by most programming languages is to define a syntactic device that groups multiple statements into one compound statement or block. A block is regarded syntactically as a single entity. When it is the target of an if statement, and `<expr>` is true, then all the statements in the block are executed. If `<expr>` is false, then none of them are.

Virtually all programming languages provide the capability to define blocks, but they don’t all provide it in the same way. Let’s see how Python does it.

**Python: It’s All About the Indentation**

Python follows a convention known as the off-side rule, a term coined by British computer scientist Peter J. Landin. (The term is taken from the offside law in association football.) Languages that adhere to the off-side rule define blocks by indentation. Python is one of a relatively small set of off-side rule languages.

Recall from the previous tutorial on Python program structure that indentation has special significance in a Python program. Now you know why: indentation is used to define compound statements or blocks. In a Python program, contiguous statements that are indented to the same level are considered to be part of the same block.

Thus, a compound if statement in Python looks like this:

```py
if <expr>:
    <statement>
    <statement>
    ...
    <statement>
<following_statement>
```

Here, all the statements at the matching indentation level (lines 2 to 5) are considered part of the same block. The entire block is executed if `<expr>` is true, or skipped over if `<expr>` is false. Either way, execution proceeds with `<following_statement>` (line 6) afterward.
    
<img src='https://files.realpython.com/media/t.78f3bacaa261.png' />
    
Notice that there is no token that denotes the end of the block. Rather, the end of the block is indicated by a line that is indented less than the lines of the block itself.
"""

if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
    
print('After conditional')

"""The four print() statements on lines 2 to 5 are indented to the same level as one another. They constitute the block that would be executed if the condition were true. But it is false, so all the statements in the block are skipped. After the end of the compound if statement has been reached (whether the statements in the block on lines 2 to 5 are executed or not), execution proceeds to the first statement having a lesser indentation level: the print() statement on line 6.

Blocks can be nested to arbitrary depth. Each indent defines a new block, and each outdent ends the preceding block. The resulting structure is straightforward, consistent, and intuitive.

Here is a more complicated script:
"""

# Does line execute?                        Yes    No
#                                           ---    --
if 'foo' in ['foo', 'bar', 'baz']:        #  x
    print('Outer condition is true')      #  x

    if 10 > 20:                           #  x
        print('Inner condition 1')        #        x

    print('Between inner conditions')     #  x

    if 10 < 20:                           #  x
        print('Inner condition 2')        #  x

    print('End of outer condition')       #  x
print('After outer condition')            #  x

"""### The else and elif Clauses

Now you know how to use an if statement to conditionally execute a single statement or a block of several statements. It’s time to find out what else you can do.

Sometimes, you want to evaluate a condition and take one path if it is true but specify an alternative path if it is not. This is accomplished with an else clause:

```py
if <expr>:
    <statement(s)>
else:
    <statement(s)>
```

If `<expr>` is true, the first suite is executed, and the second is skipped. If <expr> is false, the first suite is skipped and the second is executed. Either way, execution then resumes after the second suite. Both suites are defined by indentation, as described above.

In this example, x is less than 50, so the first suite (lines 4 to 5) are executed, and the second suite (lines 7 to 8) are skipped:
"""

x = 20

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

"""Here, on the other hand, x is greater than 50, so the first suite is passed over, and the second suite executed:"""

x = 120

if x < 50:
    print('(first suite)')
    print('x is small')
else:
    print('(second suite)')
    print('x is large')

hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
else:
    print("uang tidak cukup")

"""There is also syntax for branching execution based on several alternatives. For this, use one or more elif (short for else if) clauses. Python evaluates each `<expr>` in turn and executes the suite corresponding to the first that is true. If none of the expressions are true, and an else clause is specified, then its suite is executed:
    
```py
if <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
elif <expr>:
    <statement(s)>
    ...
else:
    <statement(s)>
```

An arbitrary number of elif clauses can be specified. The else clause is optional. If it is present, there can be only one, and it must be specified last:
"""

hargaBuku = 20000
hargaMajalah = 5000
uang = 2000

if uang > hargaBuku:
    print("beli buku")
elif uang > hargaMajalah:
    print("beli majalah")
else:
    print("uang tidak cukup")

name = 'Hacktiv8'
if name == 'Fred':
    print('Hello Fred')
elif name == 'Xander':
    print('Hello Xander')
elif name == 'Hacktiv8':
    print('Hello Hacktiv8')
elif name == 'Arnold':
    print('Hello Arnold')
else:
    print("I don't know who you are!")

"""At most, one of the code blocks specified will be executed. If an else clause isn’t included, and all the conditions are false, then none of the blocks will be executed.

An if statement with elif clauses uses short-circuit evaluation, analogous to what you saw with the and and or operators. Once one of the expressions is found to be true and its block is executed, none of the remaining expressions are tested. This is demonstrated below:
"""

if 'a' in 'bar':
    print('foo')
elif 1/0:
    print("This won't happen")
elif var:
    print("This won't either")

"""### One-Line if Statements

It is customary to write if `<expr>` on one line and `<statement>` indented on the following line like this:

```py
if <expr>:
    <statement>
```

But it is permissible to write an entire if statement on one line. The following is functionally equivalent to the example above:

`if <expr>: <statement>`

There can even be more than one `<statement>` on the same line, separated by semicolons:

`if <expr>: <statement_1>; <statement_2>; ...; <statement_n>`

But what does this mean? There are two possible interpretations:

If `<expr>` is true, execute `<statement_1>`.

Then, execute `<statement_2>` ... `<statement_n>` unconditionally, irrespective of whether `<expr>` is true or not.

If `<expr>` is true, execute all of `<statement_1>` ... `<statement_n>`. Otherwise, don’t execute any of them.

Python takes the latter interpretation. The semicolon separating the `<statements>` has higher precedence than the colon following `<expr>`—in computer lingo, the semicolon is said to bind more tightly than the colon. Thus, the `<statements>` are treated as a suite, and either all of them are executed, or none of them are:
"""

if 'f' in 'foo': print('1'); print('2'); print('3')

if 'z' in 'foo': print('1'); print('2'); print('3')

"""Multiple statements may be specified on the same line as an elif or else clause as well:"""

x = 2

if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')

x = 3
if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')

"""While all of this works, and the interpreter allows it, it is generally discouraged on the grounds that it leads to poor readability, particularly for complex if statements. PEP 8 specifically recommends against it.

As usual, it is somewhat a matter of taste. Most people would find the following more visually appealing and easier to understand at first glance than the example above:
"""

x = 3
if x == 1:
    print('foo')
    print('bar')
    print('baz')
elif x == 2:
    print('qux')
    print('quux')
else:
    print('corge')
    print('grault')

"""### Conditional Expressions (Python’s Ternary Operator)

Python supports one additional decision-making entity called a conditional expression. (It is also referred to as a conditional operator or ternary operator in various places in the Python documentation.) Conditional expressions were proposed for addition to the language in PEP 308 and green-lighted by Guido in 2005.

In its simplest form, the syntax of the conditional expression is as follows:

`<expr1> if <conditional_expr> else <expr2>`

This is different from the if statement forms listed above because it is not a control structure that directs the flow of program execution. It acts more like an operator that defines an expression. In the above example, `<conditional_expr>` is evaluated first. If it is true, the expression evaluates to `<expr1>`. If it is false, the expression evaluates to `<expr2>`.

Notice the non-obvious order: the middle expression is evaluated first, and based on that result, one of the expressions on the ends is returned. Here are some examples that will hopefully help clarify:
"""

raining = False
print("Let's go to the", 'beach' if not raining else 'library')

raining = True
print("Let's go to the", 'beach' if not raining else 'library')

age = 12
s = 'teen' if age < 21 else 'adult'
s

'yes' if ('qux' in ['foo', 'bar', 'baz']) else 'no'

"""You could use a standard if statement with an else clause:

```py
if a > b:
    m = a
else:
    m = b
```

But a conditional expression is shorter and arguably more readable as well:

`m = a if a > b else b`

Remember that the conditional expression behaves like an expression syntactically. It can be used as part of a longer expression. The conditional expression has lower precedence than virtually all the other operators, so parentheses are needed to group it by itself.

In the expression `<expr1>` if `<conditional_expr>` else `<expr2>`:

`If <conditional_expr> is true, <expr1> is returned and <expr2> is not evaluated.`

`If <conditional_expr> is false, <expr2> is returned and <expr1> is not evaluated.`

### The Python pass Statement

Occasionally, you may find that you want to write what is called a code stub: a placeholder for where you will eventually put a block of code that you haven’t implemented yet.

Consider this script foo.py:

```py
if True:

print('foo')
```

If you try to run foo.py, you’ll get this:

```py
  File "foo.py", line 3
    print('foo')
        ^
IndentationError: expected an indented block
```

The Python pass statement solves this problem. It doesn’t change program behavior at all. It is used as a placeholder to keep the interpreter happy in any situation where a statement is syntactically required, but you don’t really want to do anything:

```py
if True:
    pass

print('foo')
```

Now file runs without error.

______
"""

if True:
    pass
print('foo')