import re
from getpass import getpass
from blacklist import bad_pass

MIN_LEN_PASS = 6
MAX_POINT = 10


def check_upper_case(password):
    return bool(password != password.lower())


def check_digits(password):
    return bool(re.findall('\d+', password))


def check_special_characters(password):
    return bool(re.search('[!@#$%^&*()]', password))


def check_blacklist(password):
    return bool(password not in bad_pass)


def check_len(password):
    return bool(len(password) > MIN_LEN_PASS)


def check_repeating_symbols(password):
    return bool(max([password.count(symbol) for symbol in password]) < 3)


def get_password_strength(password):
    checks = {check_upper_case,
              check_digits,
              check_special_characters,
              check_blacklist,
              check_len,
              check_repeating_symbols}
    check_cost = MAX_POINT / len(checks)
    return int(check_cost * sum([1 if check(password) else 0 for check in checks]))


if __name__ == '__main__':
    user_password = getpass('Введите пароль: ')
    print("Сложность пароля: {}".format(get_password_strength(user_password)))
