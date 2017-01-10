import re
from getpass import getpass
from blacklist import bad_pass

ONE_POINT = 1
ZERO_POINTS = 0
MIN_LEN_PASS = 6
MAX_POINT = 10


def check_upper_case(password):
    return ONE_POINT if not password == password.lower() else ZERO_POINTS


def check_digits(password):
    return ONE_POINT if re.findall('\d+', password) else ZERO_POINTS


def check_special_characters(password):
    return ONE_POINT if re.search('[!@#$%^&*()]', password) else ZERO_POINTS


def check_blacklist(password):
    return ONE_POINT if password not in bad_pass else ZERO_POINTS


def check_len(password):
    return ONE_POINT if len(password) > MIN_LEN_PASS else ZERO_POINTS


def check_repeating_symbols(password):
    return ONE_POINT if max([password.count(symbol) for symbol in password]) < 3 else ZERO_POINTS


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
