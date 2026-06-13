Guess the Number

A simple console game in Python. Guess the number from 1 to 10 in 3 attempts.

How to run

1. Install Python 3.x
2. Download guess_number.py
3. Run in terminal: python guess_number.py

How to play

1. Enter a number from 1 to 10
2. The game will tell you if the number is higher or lower
3. You have 3 attempts
4. If you guess correctly, you win. If not, the game shows the secret number

Example

Enter a number from 1 to 10: 3
The number is higher.
Attempts left: 2

Enter a number from 1 to 10: 7
The number is lower.
Attempts left: 1

Enter a number from 1 to 10: 5
You guessed it!

Code

import random

number = random.randint(1, 10)
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    guess = int(input("Введите число от 1 до 10:"))
    attempts += 1
    if guess == number:
        print("Вы угадали число!")
        break
    elif guess < number:
        print("Загаданное число больше.")
    elif guess > number:
        print("Загаданное число меньше.")
    print(f"Осталось {max_attempts - attempts} попыток.")
if attempts == max_attempts and guess != number:
    print(f"У вас закончились попытки, было загадано число {number}")

Author

sunlightonnight

License

MIT

---

Угадай число

Консольная игра на Python. Нужно угадать число от 1 до 10 за 3 попытки.

Как запустить

1. Установи Python 3.x
2. Скачай файл guess_number.py
3. Запусти в терминале: python guess_number.py

Как играть

1. Введи число от 1 до 10
2. Программа подскажет: больше или меньше загаданное число
3. У тебя 3 попытки
4. Если угадал — победа. Если нет — игра покажет загаданное число

Пример

Введите число от 1 до 10: 3
Загаданное число больше.
Осталось 2 попыток.

Введите число от 1 до 10: 7
Загаданное число меньше.
Осталось 1 попыток.

Введите число от 1 до 10: 5
Вы угадали число!

Код

import random

number = random.randint(1, 10)
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    guess = int(input("Введите число от 1 до 10:"))
    attempts += 1
    if guess == number:
        print("Вы угадали число!")
        break
    elif guess < number:
        print("Загаданное число больше.")
    elif guess > number:
        print("Загаданное число меньше.")
    print(f"Осталось {max_attempts - attempts} попыток.")
if attempts == max_attempts and guess != number:
    print(f"У вас закончились попытки, было загадано число {number}")

Автор

sunlightonnight
Лицензия

MIT
