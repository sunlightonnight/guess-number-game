import random

number = random.randint(1, 10)
attempts = 0
max_attempts = 3

print("Угадай число от 1 до 10. У тебя 3 попытки.")

while attempts < max_attempts:
    guess = int(input("Введите число: "))
    attempts += 1
    
    if guess == number:
        print(f"Поздравляю! Ты угадал за {attempts} попытки(у)!")
        break
    elif guess < number:
        print("Загаданное число БОЛЬШЕ")
    else:
        print("Загаданное число МЕНЬШЕ")
    
    print(f"Осталось попыток: {max_attempts - attempts}")

if attempts == max_attempts and guess != number:
    print(f"Ты проиграл! Было загадано число {number}")