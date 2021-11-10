# class Dog:
#     species = "Canis familiaris"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # Instance method
#     def description(self):
#         return f"{self.name} is {self.age} years old"

#     # Another instance method
#     def speak(self, sound):
#         return f"{self.name} says {sound}"  


# class JackRussellTerrier(Dog):
#     def speak(self, sound="Arf"):
#         return f"{self.name} says {sound}"

# class Dachshund(Dog):
#     pass

# class Bulldog(Dog):
#     pass

# buddy = Dog("Buddy", 9)
# dog1 = JackRussellTerrier("Jack", 3)
# dog2 = Bulldog("Jin", 1)

# print(dog1.speak("Wan"))
# print(buddy.description())

# print(isinstance(dog1, Dog))

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