
# def os_interaction():
#     assert ('linux' in sys.platform), "Function can only run on Linux systems."
#     assert ('windows' in sys.platform), "This code runs on Windows only."
#     print('Doing something.')

# try:
#     os_interaction()
# except:
#     print('Windows function was not executed')

# def check_coins(coins):
#     assert (coins > 10), "some coins fell down on the way"

# coins = 11
# try:
#     check_coins(coins)
# except AssertionError as error:
#     print(error)

def os_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    assert ('windows' in sys.platform), "This code runs on Windows only."
    print('Doing something.')

try:
    os_interaction()
except:
    print('Windows function was not executed')