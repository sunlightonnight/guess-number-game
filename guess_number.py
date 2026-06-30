import random

number = random.randint(1, 10)
attempts = 0
max_attempts = 3
while attempts < max_attempts:
    try:
        guess = int(input("Введите число от 1 до 10:"))
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