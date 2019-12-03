numbers = []
import random
number = random.randint(1,1000)
print(number)
while True :
   a = input('Выбирете число от одного 1 до 1000 :')
   if a.isdigit():
       numbers.append(int(a))
   if int(a) == number :
       print("Вы угадали")
       break
   elif int(a) < number:
       print('Введенное число больше')
   elif int(a) > number :
       print ('Введенное число меньше')
print("Количество попыток ", len(numbers))
