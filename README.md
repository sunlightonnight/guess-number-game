# Угадай число

Консольная игра на Python, где нужно угадать число от 1 до 10 за 3 попытки.

A simple console game in Python. Guess the number from 1 to 10 in 3 attempts.

---

## Как запустить / How to run

1. Установи Python 3.x / Install Python 3.x
2. Скачай файл `guess_number.py` / Download `guess_number.py`
3. Запусти в терминале: `python guess_number.py` / Run in terminal: `python guess_number.py`

---

## Как играть / How to play

1. Введи число от 1 до 10 / Enter a number from 1 to 10
2. Программа подскажет: больше или меньше загаданное число / The game will tell you if the number is higher or lower
3. У тебя 3 попытки / You have 3 attempts
4. Если угадал — победа. Если нет — игра покажет загаданное число / If you guess correctly, you win. If not, the game shows the secret number

---

## Пример / Example

Введите число от 1 до 10: 3
Загаданное число больше.
Осталось 2 попыток.

Введите число от 1 до 10: 7
Загаданное число меньше.
Осталось 1 попыток.

Введите число от 1 до 10: 5
Вы угадали число!

---

## Код / Code

```python
import random

number = random.randint(1, 10)
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    try:
        guess = int(input("Введите число от 1 до 10: "))
    except ValueError:
        print("Ошибка! Нужно ввести число, а не буквы. Попробуй снова.")
        continue

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
