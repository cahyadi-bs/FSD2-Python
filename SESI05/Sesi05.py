##==================================================================================
##      OOP - Object Oriented Programming
##==================================================================================

## Class vs Instances
## Class merupakan blueprint
## Instance merupakan sesuatu (object) yang dibuat menggunakan Class

## Define a class
# class Dog:
#     pass

# __init__() digunakan sama seperti constructor pada bahasa pemograman lain
# digunakan untuk memberikan status/properti inisial ketika class di inisiasi

class Dog:
    # Class attribute
    species = "Canis familiaris"
    def __init__(self, name, age):
        self.name = name
        self.age = age

# self mengacu pada class itu sendiri
##==================================================================================
## Instantiate an Object in Python
varName = Dog("buddy", 21)

## Untuk mengakses data properties/method yang telah inisiasi dapat menggunakana dot (.)
varName.name
varName.age
##==================================================================================
## Instance Method
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
##==================================================================================
# Inheritation
# merupakan proses yang mengambil properties atau method dari class yang lain
# dibedakan menjadi 2 yaitu parent dan child class, dimana child class mewariskan semua properties dan method dari parent class

# untuk membuat child class, dengan membuat class seperti biasa
# kemudian memasukkan nama dari parent class ke dalam ()

class JackRussellTerrier(Dog):
    pass

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

# Extend functionality of a parent class
# untuk dapat mengoveride method dari parent class maka dapat dilakukan dengan membuat method dengan nama yang sama dengan method yang ada di parent class
# 
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return f"{self.name} says {sound}"
