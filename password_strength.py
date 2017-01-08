import re
import sys
from getpass import getpass
from blacklist import bad_pass

TWO_POINTS = 2
ZERO_POINTS = 0


def input_password():
    password = getpass('Введите пароль: ')
    if not password:
        sys.exit('Пароль не может быть пустым')
    return password


def check_upper_case(password):
    return TWO_POINTS if not password == password.lower() else ZERO_POINTS


def check_digits(password):
    return TWO_POINTS if re.findall('\d+', password) else ZERO_POINTS


def check_special_characters(password):
    for special_characters in "!@#$%^&*()":
        if special_characters in password:
            return TWO_POINTS
    return ZERO_POINTS


def check_blacklist(password):
    return ZERO_POINTS if password in bad_pass else TWO_POINTS


def check_len(password):
    return TWO_POINTS if len(password) > 6 else ZERO_POINTS


def get_password_strength(password):
    strength = 0
    strength += check_upper_case(password)
    strength += check_digits(password)
    strength += check_special_characters(password)
    strength += check_blacklist(password)
    strength += check_len(password)
    return strength


if __name__ == '__main__':
    passwd = input_password()
    print("Сложность пароля: %s" % get_password_strength(passwd))
