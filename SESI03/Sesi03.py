##==================================================================================
# Python Function

# User Defined Function
# Format:
# def function_name( parameters ):
#    '''docstring'''
#    statement(s)

# string yang terdapat diantara ''' merupakan docstring (Documentation String) 

# Example of Function Creation
# Secara default, parameter pada python harus dimasukkan sesuai dengan urutannya
def my_function(p, l):
    '''Function to calculate area of a square'''
    print(p * l)


def printme( str_input ):
    '''This prints a passed string into this function'''
    print(str_input)

##==================================================================================
# Calling a function
printme("I'm first call to user defined function!")
printme("Again second call to the same function")

##==================================================================================
##==================================================================================
## Function Arguments
## terdapat 4 tipe argumen untuk pemanggilan function:
    ## - Required Arguments
    ## - Keyword arguments
    ## - Default arguments
    ## - Variable-length arguments

##==================================================================================
## Required Arguments
    # argumen ini merupakan argumen yang di passed ke function pada urutan yang benar sesuai dengan parameter yang ditentukan pada deklarasi function.
# Example
# Function definition is here
def printme( str_input, str_input2 ):
    '''This prints a passed string into this function'''
    print(str_input)
    print(str_input2)
# Now you can call printme function
printme("Hello","World!!")

# # This syntax will give you an error
# printme()         # This is ERROR, karena tidak ada argumen
# printme("Hello")  # This is also ERROR, karena parameter harus 2 tapi argumen hanya 1      
##==================================================================================
## Keyword Arguments
    #argumen ini menggunakan 'keyword' pada pemanggilan function. keyword berupa nama parameter yang dideklarasi function. dengan keyword arguments penempatan argumen tidak perlu sesuai dengan urutan.

# Function definition is here
def printme( str_input, str_input2 ):
    '''This prints a passed string into this function'''
    print(str_input)
    print(str_input2)

# Now you can call printme function
printme(str_input2="Hello", str_input = "Hacktiv8")

##==================================================================================
##Default Arguments
    #argumen yang dipakai bila argumen tidak dimasukkan pada pemanggilan function
# Function definition is here
def printinfo( name, age = 26 ):
    '''This prints a passed info into this function'''
    print("Name : ", name)
    print("Age  : ", age)
    print("")

# Now you can call printinfo function
printinfo( age=50, name="hacktiv8" )
printinfo( name="hacktiv" )

## DEFAULT PARAMETER HARUS DITULIS SETELAH REQUIRED PARAMATER
# EXAMPLE: def printinfo(name, age=26):
# NOT THIS: def printinfo(age=26, name):

##==================================================================================
# Variable-length Arguments
    # Argumen yang dimasukkan lebih dari yang dispesifikasikan
# Example:
# def functionName(args, *var_args_tuple ):
#     '''function_docstring'''
#     function_suite
#     return [expression]

# satu asterisk (*) sebelum variable akan menyimpan value sebagai tuple
# dua asterisk (**) sebelum variable akan menyimpan value sebagai dictionary

# Contoh 1 asterisk (tuple)
def invoice(customerName, *items):
    '''this prints a variable passed arguments'''
    print('Customer Name    :', customerName)
    print('Items            :', items )
    print('')

invoice('Cahyadi','eggs','wheat','flour')

# Contoh 2 asterisk (dictionary)
def person_car(total_data, **kwargs):
    '''Create a function to print who owns what car'''
    print('Total Data : ', total_data)
    for key, value in kwargs.items():
        print('Person : ', key)
        print('Car    : ', value)
        print('')

person_car(3, jimmy='chevrolet', frank='ford', tina='honda')
person_car(3)

##==================================================================================
##==================================================================================
# Anonymous Function
    # function ini disebut anonymous karena tidak dideklarasikan secara benar (tidak menggunakan def keyword)

# Format
# lambda [arg1 [,arg2,.....argn]]:expression

sum = lambda arg1, arg2: arg1 + arg2

# That lambda function will be equal to :
# def sum(arg1, arg2):
#     return arg1+arg2

# Now you can call sum as a function
print("Value of total : ", sum( 10, 20 ))
print("Value of total : ", sum( 20, 20 ))

##==================================================================================
##==================================================================================
# Return statement
    # statement ini akan mengeluarkan diri dari function, return statement secara opsional dapat mengembalikan expresi, tanpa ekspresi sama seperti (return None)
def sum(arg1, arg2):
    # Add both the parameters and return them."
    total = arg1 + arg2
    return total

# Now you can call sum function
total = sum(10, 20)
print("Result function : ", total)

##==================================================================================
##==================================================================================
# Scope of Variables
    # Terdapat 2 scope yaitu local dan global
# Declare a global variable
total = 0

# Create sum function
def sum( arg1, arg2 ):
    # Decclare a local variable
    total = arg1 + arg2; 
    print("Inside the function local total   : ", total)
    return total

# Call a function
print("Outside the function global total - before : ", total)
total = sum( 10, 20 )
print("Outside the function global total - after  : ", total)

##==================================================================================
##==================================================================================
# Docstring
# docstring dibentuk dengan menggunakan format 
# ''' docstring ''' atau """ docstring """

# Example of docstring in a function

def sum_number(num1, num2):
    '''
    This function is used to sum of 2 variables.
    :param num1: Input number 1 | int or float
    :param num2: Input number 2 | int or float
    
    :return: num3: Sum of number | int or float
    '''

    num3 = num1 + num2
    return num3




##==================================================================================
# MODULE and PACKAGES
##==================================================================================
# 4 Advantages modularizing code:
    # Simplicity
    # Maintainability
    # Reusability
    # Scoping

# Import statement
# import <module_name>
# cara ini tidak membuat semua konten dari module dapat diakses
# jadi konten dapat di akses dengan <moduleName>.<content>

# from <module_name> import <something>
# dengan cara ini konten tidak perlu dipanggil dengan prefix <module_name>

# bisa juga memasukkan semua tanpa spesifikasi import apa saja yang akan digunakan dengan menggunakan :

# from <module_name> import *

# akan tetapi hal ini tidak dianjurkan pada kode berskala besar,
# karena akan memasukkan nama baru ke local symbol table dan adapat terjadi konflik

##==================================================================================
# Aliases
# from <module_name> import <something> as <alt_name>
from person import name as p_name, devices as p_devices

#import <module_name> as <alt_name>
import person as my_person
##==================================================================================
# Module contents can be imported from within a function definition. In that case, the import does not occur until the function is called
# However, Python 3 does not allow the indiscriminate import * syntax from within a function:

##==================================================================================
# Reloading a module
# If you make a change to a module and need to reload it, you need to either restart the interpreter or use a function called reload() from module importlib

##==================================================================================
#Python Packgage
# untuk memudahkan organisir atau meng-grouping module
# Package mengijinkan struktur hierarki pada namespace module dengan notasi dot (.)
# hal ini digunakan untuk membantu mencegah terjadinya kolisi antara global variable names, dengan modules name

# contoh struktur 
#   pkg --> (Directory)
#     - mod1.py 
#     - mod2.py

# maka kedua file tersebut dapat diimport dengan format
#import <folder/package><.module_name_1>, <folder/package>.<module_name_2>
import pkg.mod1, pkg.mod2

#atau

# from <pakckage>.<module_name> import <something>
from pkg.mod1 import kitchen_sets

#Bila dengan alias
#from <package>.<module_name> import <something> as <alt_name>
from pkg.mod1 import kitchen_sets as ks