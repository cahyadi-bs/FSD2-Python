##==================================================================================
##      Advance Python
##==================================================================================

# Iterators
# merupakan object yang dapat di iterasi . list, tuple, dict dan set merupakan object iterable
# untuk membuat object sebagai iterator harus mengimplementasikan method __iter__() dan __next__() ke object.

# Lazy iterable =  iterable yang tidak akan ditampilkan bila tidak diinginkan

##==================================================================================
# Generator
# function yang sama seperti function biasa tetapi menggunakan 'yield' bukan 'return'.
# Generator Function merupakan function yang mengembalikan lazy iterator. object yang dikembalikan sama seperti list, akan tetapi lazy iterator tidak menyimpan datanya di memory

def my_generator():
    print("Inside my generator")
    yield 'a'
    yield 'b'
    yield 'c'

my_generator()

# hasil dari generator diatas dapat digunakan pada for loop sama seperti iterator yang lain

for char in my_generator():
    print(char)

# Contoh Lain
def counter_generator(low, high):
    while low <= high:
        yield low
        low += 1

for i in counter_generator(5,10):
    print(i, end=' ')

# perbedaan yield dengan return adalah yield mengeluarkan nilai dan pause eksekusinya, dimana return mengembalikan nilai dan memberhentikan eksekusi dari function
##==================================================================================
# Generator expression
# merupakan metode penulisan singkat dari generator function. genrator expression merupakan anonymous genrator function
# Example
square_list = [n** 2 for n in range(5)]
# bagian pertama merupakan nilai yield dan bagian kedua merupakan for loop
for data in square_list:
    print(data)
    
# Generation Expression diatas mewakili Generator Function dibawah
'''
def squares(length):
    for n in range(length):
        yield n ** 2
for square in squares(5):
    print(square)
'''

##==================================================================================

## Decorators
# decorator meruapkan semua python object yang bisa dipanggil yang digunakan  untuk memodifikasi sebuah funtion atau class.
# decorator biasanya dipanggil sebelum definisi function yang ingin di 'decorate'
# Example
#   @Decorators
#   def someFunction():
#       pass

## First Class Object
# pada Python, function merupakan first-class object. yang berarti function dapat di lempar dan digunakan menjadi argumen.
# Example
def say_hello(name):
    return f"Hello {name}"

def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def greet_bob(greeter_func):  # greeter_func expect function sebagai argumennya
    return greeter_func("Bob")

print(greet_bob(be_awesome))

## Inner Functions
# sangat mungkin untuk mendefine function di dalam function lain. metode tersebut dimaksud dengan inner function
# Example
def parent():
    print("Printing from the parent() function")

    def first_child():
        print("Printing from the first_child() function")

    def second_child():
        print("Printing from the second_child() function")

    second_child()
    first_child()

parent()

# Returning function from function
# python mengijinkan function sebagai nilai yang dikembalikan dari return statement
# Example
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child

print(parent(1)())
#atau
second = parent(2)
print(second())


# Simple Decorator
# Example
'''
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
say_whee()
'''

# wrapper() memiliki referensi pada function say_whee() dan memanggil nya sebagai func()
# secara singkat, decorators 'wrap' sebuah function dan memodifikasi tingkah lakunya
# Example memakai decorator

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

say_whee()

# jadi @my_decorator merupakan cara mudah untuk menyampaikan 'say_whee = my_decorator(say_whee)'



# More Example
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator

# formula diatas dapat digunakan sebagai boilerplate template untuk membangun decorator yang lebih kompleks


import functools
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])