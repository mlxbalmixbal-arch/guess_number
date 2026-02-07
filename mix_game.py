import random
print('------------------------------------------------------')
print('---ИГРА УГАДАЙ ЧИСЛО---')
print('угадай число от 1 до 100 за 5 попыток')
print('------------------------------------------------------')
secret_number = random.randint(1, 100)
attempts_left = 5
while True:
    guess_num = int(input('введи число - '))
    attempts_left -= 1 
    if attempts_left == 0:
            print('================================')
            print(f'осталось {attempts_left} попытки')
            print('попытки закончились, ты проиграл')
            print(f'это было {secret_number}')
            print('================================')
            attempts_left = 5
            print('еще раз?')
            ans = input('да/нет - ')
            if ans == 'нет':
                print('пока')
                break
    elif guess_num == secret_number:
            print('================================')
            print(f'правильно, это было {secret_number}')
            print(f'оставалось {attempts_left} попытки')
            print('================================')
            attempts_left = 5
            print('еще раз?')
            ans = input('да/нет - ')
            if ans == 'нет':
                print('пока')
                break
    elif guess_num < secret_number:
            print('================================')
            print('загаданое число БОЛЬШЕ, попробуй еще')
            print(f'осталось {attempts_left} попытки')
            print('================================')
    elif guess_num > secret_number:
            print('================================')
            print('загаданое число МЕНЬШЕ, попробуй еще')
            print(f'осталось {attempts_left} попытки')
            print('================================')
    else:

        print('ошибка')
