import random

number = random.randint(1, 1000)
print(number)
i = 0
while True:
    guess = input('Выбирете число от одного 1 до 1000 :')
    if guess.isdigit():
        guess_as_number = int(guess)
        if guess_as_number == number:
            print("Вы угадали")
            break
        elif guess_as_number < number:
            print('Введенное число больше')
        elif guess_as_number > number:
            print('Введенное число меньше')
    else:
        print('Выбирете число от 1 до 1000')
    i = i + 1
print('Количество попыток', i)
