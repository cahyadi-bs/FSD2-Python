#Python Data Type
#Integer
print(10)
print(type(10))

#Float
print(4.2)
print(type(4.2))
print(4.)
print(.2)
print(.4e7)
print(4.2e-4)

#String
print("Hacktiv8")
print(type("Hacktiv8"))
print("This string contains a single quote (') character.")
print('This string contains a double quote (") character.')

#Boolean
print(type(True))
print(type(False))

print(100 > 200) #False
print(100 == 200) #False
print(100 < 200) #True
#======================================================================
#Variable Assignment
n = 300
a = b = c = 300

#Variable Name Format
# Camel Case, Example: numberOfCollegeGraduates
# Pascal Case, Example: NumberOfCollegeGraduates
# Snake Case,Example: number_of_college_graduates
#======================================================================
#Operator
#Arithmetic Operators
a = 4
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)

#Comparison Operators
a = 10
b = 20
print(a == b)
print(a != b)
print(a <= b)
print(a >= b)
#======================================================================
#String Manipulation
s = 'foo'
t = 'bar'
# + and * Operators
print(s + t )
print(s * 4)
#Case Conversion
print(s.capitalize())
print(s.lower())
print(s.upper())
print(s.swapcase())

#======================================================================
# Python Lists
# List is mutable (Dapat Berubah)
# List dibuat dengan "[]"
a = ['foo', 'bar', 'baz', 'qux']
print(a)

#Modifying List Value
a[2] = 10
a[-1] = 20
print(a)

#Modifying several elements at one time using slice assignment, example syntax:
a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[1:4])
a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5] 
#[Start:End] , End Tidak termasuk dalam assignment
#Start inclusive, End exculsive, ex. [2:5] akan mengambil index 2 sampai 4
print(a)

#Built-in function
# .append(value) ==> add element to the last index 
# .remove(value)
# .count()
# .sort()
# .sorted() ==> return sorted value in a new variable
# .insert(index, value) ==> add to lists depending on the index
# .pop() ==> remove the last element in the lists

#======================================================================
# Python Tuples
# Tuple is immutable (Tidak Dapat Berubah)
# Tuple dibuat dengan "()"
t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print(t)
print(t[0])
print(t[-1])

#======================================================================
# Python Dictionary
# Dictionary memiliki karakteristik yang sama dengan lists,
# yang membedakan, elemen dictionary diakses menggunakan 'keys'
# Dictionary dibuat dengan "{}"

MLB_team = {
    'Colorado': 'Rockies',
    'Boston': 'Red Sox',
    'Minnesota': 'Twins',
    'Seattle': 'Mariners',
}

print(MLB_team['Minnesota'])

#Adding an entry to an existing dictionary
MLB_team['Kansas City'] = 'Royals'
#Change an entry with list
MLB_team['Seattle'] =  ['White Fox', 'Red Fox']

print(MLB_team)