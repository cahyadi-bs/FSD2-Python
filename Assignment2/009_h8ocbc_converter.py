
# Soal No 1
# Function untuk konversi dari Celcius ke Kelvin dan sebaliknya
def kelvinCelciusConverter(value,temperatureType):
    ''' 
    function ini melakukan konversi dari celcius ke kelvin dan sebaliknnya 
    :param value: Input value | int or float
    :param temperatureType: Input temperature type | string

    :return: value: hasil dari kalkulasi konversi | int or float
    '''
    if temperatureType.lower() == 'k':
        return value-273.15
    elif temperatureType.lower() == 'c':
        return value+273.15
    else:
        return

# Soal No 2
# Function untuk konversi dari Celcius/Kelvin ke Fahrenheit
def convertToFahrenheit(value,temperatureType):
    ''' 
    function ini melakukan konversi ke fahrenheit dari celcius/kelvin

    :param value: Input value | int or float
    :param temperatureType: Input temperature type | string

    :return: value: hasil dari kalkulasi konversi | int or float 
    '''
    if temperatureType.lower() == 'k':
        return (kelvinCelciusConverter(value,'K')*(9/5)) + 32 
    elif temperatureType.lower() == 'c':
        return (value*(9/5)) + 32 
    else:
        return

# Soal No 3
# Function untuk konversu daru Fahrenheit ke Celcius/Kelvin
def convertFromFahrenheit(value,temperatureType):
    ''' 
    function ini melakukan konversi dari fahrenheit ke celcius/kelvin 

    :param value: Input value | int or float
    :param temperatureType: Input temperature type | string

    :return: value: hasil dari kalkulasi konversi | int or float
    '''
    if temperatureType.lower() == 'k':
        return kelvinCelciusConverter((value-32) * (5/9),'C')
    elif temperatureType.lower() == 'c':
        return (value-32) * (5/9)
    else:
        return

listProgram = ['1','2','3','4','5','6']
state = True
while state:
    print('')
    print("=====================================")
    print("======= PROGRAM KONVERSI SUHU =======")
    print("=====================================")
    print("   1. Konversi Celcius ke Kelvin     ")
    print("   2. Konversi Kelvin ke Celcius     ")
    print("   3. Konversi Celcius ke Fahrenheit ")
    print("   4. Konversi Kelvin ke Fahrenheit  ")
    print("   5. Konversi Fahrenheit ke Celcius ")
    print("   6. Konversi Fahrenheit ke Kelvin  ")
    print("=====================================")
    
    try:
        x = input('   Masukkan kode program: ')
        assert (x in listProgram) , "Pilihan tidak ada. Mohon coba lagi!!"
        value = int(input("   Masukkan nilai: "))
    except ValueError:
        print("Input harus berupa angka. Mohon Coba Lagi!!")
    except AssertionError as error:
        print(error)
    else:
        if x=='1':
            print('   Hasil Konversi = ' + str(round(kelvinCelciusConverter(value,'C'),2)) + ' \u00b0K')
        elif x=='2':
            print('   Hasil Konversi = ' + str(round(kelvinCelciusConverter(value,'K'),2)) + ' \u00b0C')
        elif x=='3':
            print('   Hasil Konversi = ' + str(round(convertToFahrenheit(value,'C'),2)) + ' \u00b0F')
        elif x=='4':
            print('   Hasil Konversi = ' + str(round(convertToFahrenheit(value,'K'),2)) + ' \u00b0F')
        elif x=='5':
            print('   Hasil Konversi = ' + str(round(convertFromFahrenheit(value,'C'),2)) + ' \u00b0C')
        elif x=='6':
            print('   Hasil Konversi = ' + str(round(convertFromFahrenheit(value,'C'),2)) + ' \u00b0C')
    state = True if (input("\nApakah anda mau mengulang (y/n)? ")).lower() == 'y' else False