# Conditional

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

##==================================================================================
## Di Python tidak ada {} yang digunakan adalah indentation
# If Statement

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

##==================================================================================
#If..Else..
x = 20

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

##==================================================================================
##Else...IF...
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

##==================================================================================
## One Line If
# Untuk lebih dari 2 statement maka dipisah dengan ";"
# Walaupun ini bisa digunakan, akan tetapi format seperti ini tidak dianjurkan

if 'f' in 'foo': print('1'); print('2'); print('3')

if x == 1: print('foo'); print('bar'); print('baz')
elif x == 2: print('qux'); print('quux')
else: print('corge'); print('grault')

##==================================================================================
#Ternary Operator
# Format: <expr1> if <conditional_expr> else <expr2>
# If <conditional_expr> is true, <expr1> is returned and <expr2> is not evaluated.
# If <conditional_expr> is false, <expr2> is returned and <expr1> is not evaluated.

raining = False
print("Let's go to the", 'beach' if not raining else 'library')

age = 12
s = 'teen' if age < 21 else 'adult'
print(s)

##==================================================================================
#Python Pass statement
# pass digunakan sebagai placeholder untuk kode yang belum diimplementasikan
#ex.
# if True:
            
# print('foo')

if True:
    pass

print('foo')

##==================================================================================
# Looping
# terdapat 2 tipe iterasi : indefinite dan definite

# While Loops
# Format
# while <expr>:    
#     <statement(s)>
#Ex.
n = 5
while n > 0:
    n -= 1
    print(n)

#Break and Continue statement
# Break statement memberhentikan iterasi loop secara keseluruhan
# Continue statement memberhentikan iterasi pada saat itu.

n = 5
while n > 0:
    n -= 1
    if n == 2:
        break # Break Statement
    print(n)
print('Loop ended.')

n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue # Continue Statement
    print(n)
print('Loop ended.')

# Else clause
# merupakan clause opsional yang akan dijalankan ketika loop berakhir
# akan tetapi bila loop diberhentikan secara prematur (break statement), clause tidak akan dijalankan
# Format:
# while <expr>:
#     <statement(s)>
# else:
#     <additional_statement(s)>

n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')

#Nested While Loop
a = ['foo', 'bar']

while len(a):
    print(a.pop(0))
    
    b = ['baz', 'qux']
    
    while len(b):
        print('>', b.pop(0))

# Break or continue within nested while loop applies to the nearest enclosing
# while <expr1>:
#     statement
#     statement

#     while <expr2>:
#         statement
#         statement
#         break  # Applies to while <expr2>: loop

#     break  # Applies to while <expr1>: loop


# One-Line while loops
n = 5
while n > 0: n -= 1; print(n)

#==================================================================================
# for Loop
#Format:
# for <var> in <iterable>:
#     <statement(s)>

#For Loop untuk List
a = ['foo', 'bar', 'baz']
for i in a:
    print(i)

#For Loop untuk Dictionary
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)
#Loop diatas akan mengiterasikan keynya

for k in d:
    print(d[k])
#Loop diatas akan mengiterasikan valuenya

for k in d.values():
    print(k)
#Loop diatas akan mengiterasikan valuenya

for k, v in d.items(): 
    print(k, ":", v) 
#Loop diatas akan mengiterasikan key dan valuenya


#==================================================================================
# Range Function
# termasuk numeric range loop
# range() akan mengembalikan objek class range, bukan list/tuple tapi masih berpa iterable


for n in (0, 1, 2, 3, 4):
    print(n)

x = range(5)
for n in x:
    print(n)

# break dan continue in For Loop
# Break
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i)

# Continue
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        continue
    print(i)

# Else clause in For Loop
for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('Done.')  # Will execute

## sama seperti pada kasus While loop, Else clause tidak akan dijalankan bila loop diberhentikan secara prematur (break)