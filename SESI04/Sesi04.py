##==================================================================================
##      FILES
##==================================================================================

# opening files
##==================================================================================
    # flag / mode pada open() :
        # r => Opens a file for reading. (default)
        # w => Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists
        # x => Opens a file for exclusive creation. If the file already exists, the operation fails
        # a => Opens a file for appending at the end of the file withouttruncating it. Creates a new file if it does not exist.
        # t => Opens in text mode. (default)
        # b => Opens in binary mode.
        # + => Opens a file for updating (reading and writing)
##==================================================================================
# opening files
file = open('Hack8_Sample_Text.txt')
##==================================================================================
# You should always make sure that an open file is properly closed.
# closing files
file.close()

#untuk lebih aman menggunakan try...finally block
try:
    f = open("Hack8_Sample_Text.txt", encoding = 'utf-8')
    # perform file operations
finally:
    f.close()

##==================================================================================
# writing files
with open("test.txt",'w',encoding = 'utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")

##==================================================================================
f = open("test.txt",'r',encoding = 'utf-8')
f.read(4) # read the first 4 data
f.read(4) # read the next 4 data
f.read()  # read in the rest till end of file
f.read()  # further reading returns empty sting
f.tell()    # get the current file position
f.seek(0)   # bring file cursor to initial position
print(f.read())  # read the entire file

# read a file line by line using for loop
f.seek(0)   # bring file cursor to initial position
for line in f:
    print(line, end = '')

# alternatif lain, kita dapat menggunakan readline() untuk membaca setiap garis
f.seek(0)
f.readline()

#berikut merupakan contoh untuk membuka dan membaca semua konten dari file menggunakan .read()
with open('sample.txt', 'r') as reader:
    # Read & print the entire file
    print(reader.read())

# untuk dapat menambahkan line atau konten ke dalam file adalah dengan mengubah  mode pada saat open() dengan 'a' kemudian melakukan .write() method.
# berikut contoh menambahkan suatu line 

with open("test.txt", 'a', encoding = 'utf-8') as f:
    f.write("add new line\n")  




##==================================================================================
##      EXCEPTION
##==================================================================================

# Exceptions vs Syntax Error
    # Contoh Syntax Error
    ''' 
    print( 0 / 0 ))  
        File "<stdin>", line 1    
        print( 0 / 0 ))     
                    ^
    SyntaxError: invalid syntax
    '''
    # Contoh exceptions
    '''
    print( 0 / 0 )
    Traceback (most recent call last):
        File "<stdin>", line 1, in <module>
    ZeroDivisionError: integer division or modulo by zero
    '''

# jika ingin 'throw' sebuah error ketika suatu kondisi terpenuhi dapat menggunakan 'raise' dengan custom exceptions
# Contoh
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))

##==================================================================================
# Try and except block : Handling Exceptions
try:    
    with open('file.log') as file:        
        read_data = file.read()
except:    
    print('Could not open file.log')

def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('windows' in sys.platform), "This code runs on Windows only."
    print('Doing something.')

try:
    os_interaction()
except:
    print('Windows function was not executed')

##==================================================================================
# Else clause
# else pada try...except merupakan suatu statement dimana block dalam else statement akan dijalankan bila tidak terdapat exceptions

try:    
    with open('file.log') as file:        
        read_data = file.read()
except FileNotFoundError as error:    
    print(error)
else:    
    print('Executing the else clause.')

##==================================================================================
#finally 
# merupakan blok code pada try statement dimana semua expression dalam block tersebut selalu dijalankan 