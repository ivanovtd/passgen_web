import string
import random

LOWERCASE_LETTERS = string.ascii_lowercase
UPPERCASE_LETTERS = string.ascii_uppercase
NUMBERS = string.digits
PUNCTUATION = string.punctuation


#MultiDict([('csrf_token', 'IjVhN2E5NzkzNjlmODBlMjM3MDU2MTQ2MThkMmI4MzNkMjRkN2M1Y2Ui.YCCbpA.QeMPXdu_qmk1JXJTci-D-Msfo5Q'), 
# ('length', '12'), ('is_use_numbers', 'y'), ('is_use_letters', 'y'), ('is_use_capitals', 'y'), ('is_use_specials', 'y')])

def generate_password(form):
    printable = []
    if 'is_use_letters' in form:
        printable.append(f'{LOWERCASE_LETTERS}')
    if 'is_use_capitals' in form:
        printable.append(f'{UPPERCASE_LETTERS}')
    if 'is_use_numbers' in form:
        printable.append(f'{NUMBERS}')
    if 'is_use_specials' in form:
        printable.append(f'{PUNCTUATION}')
    printable = list(''.join(printable))
    random.shuffle(printable)

    random_pass = random.choices(printable, k=int(form['length']))
    return ''.join(random_pass)

