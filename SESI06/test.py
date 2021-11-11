def my_generator():
    print("Inside my generator")
    yield 'a'
    yield 'b'
    yield 'c'

myGen = my_generator()
print(next(myGen))
print(next(myGen))
print(next(myGen))
# for char in my_generator():
#     print(char)

def counter_generator(low, high):
    while low <= high:
        yield low
        low += 1

# for i in counter_generator(5,10):
#     print(i, end=' ')

# countGen = counter_generator(4, 10)
# print(next(countGen))
# print(next(countGen))
# print(next(countGen))
# print(next(countGen))
# print(next(countGen))
# print(next(countGen))
# print(next(countGen))

# square_list = [n** 2 for n in range(5)]

# for data in square_list:
#     print(data)


# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"

#     def second_child():
#         return "Call me Liam"

#     if num == 1:
#         return first_child
#     else:
#         return second_child


# print(parent(1)())
# second = parent(2)
# print(second())

# def say_hello(name):
#     return f"Hello {name}"

# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"

# def greet_bob(greeter_func):
#     return greeter_func("Bob")

# print(greet_bob(say_hello))

# def parent():
#     print("Printing from the parent() function")

#     def first_child():
#         print("Printing from the first_child() function")

#     def second_child():
#         print("Printing from the second_child() function")

#     second_child()
#     first_child()

# parent()

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

#say_whee = my_decorator(say_whee)
say_whee()


