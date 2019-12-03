import random

number = random.randint(1, 1000)
print(number)

counter = 0
while True:
    guess = input('Выбирете число от одного 1 до 1000 :')
    if int(guess) > 1000:
        print("Меньше сука 1000")
        continue
    if int(guess) < 0:
        print("Больше сука 0")
        continue
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

    counter = counter + 1
print('Количество попыток', counter)
