# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def generate_password():
    # Start coding here
    password_size = random.randint(8,16)
    password_list = []
    lowercase_in_password = 0
    numbers_in_password = 0
    uppercase_in_password = 0
    total_chars = 0
    while password_size != total_chars: #len(password_list):
        lowercase_in_password = random.randint(1,password_size - 3)
        numbers_in_password = random.randint(1, password_size- lowercase_in_password - 2)
        uppercase_in_password = random.randint(1, password_size - lowercase_in_password - 1)
        symbols_in_password = random.randint(1, password_size - lowercase_in_password - uppercase_in_password)
        total_chars = lowercase_in_password + numbers_in_password + uppercase_in_password + symbols_in_password
    # This part generate the lowercases characters in the password.
    lowercase_chars = []
    i = 0
    while len(lowercase_chars) != lowercase_in_password:
        i = random.randint(0,len(string.ascii_lowercase) - 1)
        lowercase_chars.append(string.ascii_lowercase[i])

    # This part generate the numbers in the password.
    numbers_chars = []
    j = 0
    while len(numbers_chars) != numbers_in_password:
        j = random.randint(0, len(string.digits) - 1)
        numbers_chars.append(string.digits[j])
    
    # This part generate the uppercase chars in password.
    uppercase_chars = []
    k = 0
    while len(uppercase_chars) != uppercase_in_password:
        k = random.randint(0, len(string.ascii_uppercase) - 1)
        uppercase_chars.append(string.ascii_uppercase[k])
    
    # This part generate the symbols in password.
    symbols_chars = []
    l = 0
    while len(symbols_chars) != symbols_in_password:
        l = random.randint(0, len(SYMBOLS)- 1)
        symbols_chars.append(SYMBOLS[l])
    
    password_array = uppercase_chars + lowercase_chars + numbers_chars + symbols_chars
    random.shuffle(password_array)
    password_string = ''.join(password_array)
    return password_string

def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
