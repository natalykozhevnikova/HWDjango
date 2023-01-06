import random
number = random.randint(1, 100)
#print(number)
user_number = int(input('введите число: '))

while True:
    if number == user_number:
        print('победа')
        break
    elif number < user_number:
        print('ваше число больше загаданного'
    else:
        print('ваше число меньше загаданного')

