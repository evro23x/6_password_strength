# Password Strength Calculator

Cкрипт просит ввести пароль и выдаёт ему оценку от 1 до 10. 1 – очень слабый пароль, 10 – очень крутой.


# Quickstart

Пример запуска скрипта в среде Linux, под Python 3.5:

```#!bash
$ python password_strength.py <password>
```
# Example

```#!bash

$ python password_strength.py star
Сложность пароля: 0
$ python password_strength.py starr
Сложность пароля: 2
$ python password_strength.py starrrrr
Сложность пароля: 4
$ python password_strength.py starrrrr1
Сложность пароля: 6
$ python password_strength.py starrrrr1@
Сложность пароля: 8
$ python password_strength.py sTArrrrr1@
Сложность пароля: 10
```



# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
