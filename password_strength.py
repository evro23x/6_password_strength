import re
import sys
from blacklist import bad_pass

TWO_POINTS = 2
ZERO_POINTS = 0


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
    score = 0
    score += check_upper_case(password)
    score += check_digits(password)
    score += check_special_characters(password)
    score += check_blacklist(password)
    score += check_len(password)
    return score


if __name__ == '__main__':
    passwd = sys.argv[1]
    print("Сложность пароля: %s" % get_password_strength(passwd))
