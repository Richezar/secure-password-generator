import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
pwd_quantity = int(input('Сколько паролей вам нужно сгенерировать? '))
pwd_len = int(input('Какой длины должен быть пароль? '))
pwd_digits = input('Включать ли в пароль цифры от 0 до 9?; д = да, н = нет ')
pwd_uppercase = input('Включать ли в пароль прописные буквы?; д = да, н = нет ')
pwd_lowercase = input('Включать ли в пароль строчные буквы?; д = да, н = нет ')
pwd_punctuation = input('Включать ли в пароль символы "!#$%&*+-=?@^_"?; д = да, н = нет ')
pwd_exceptions = input('Исключать ли неоднозначные символы "il1Lo0O"?; д = да, н = нет ')

if pwd_exceptions == 'д':
    chars = chars + digits
if pwd_uppercase == 'д':
    chars = chars + uppercase_letters
if pwd_lowercase == 'д':
    chars = chars + lowercase_letters
if pwd_punctuation == 'д':
    chars = chars + punctuation
if pwd_exceptions == 'д':
    for i in "il1Lo0O":
        chars = chars.replace(i, '')

def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return print(password)

for _ in range(pwd_quantity):
    generate_password(pwd_len, chars)