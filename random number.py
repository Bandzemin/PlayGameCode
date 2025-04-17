import random
print('Кто выйграет?')
def main():
    print('Введите имена игроков:  ')
    print('')
    print('Имя первого игрока!')
    player1 = input('>>>  ')
    print('Привет!', player1)
    print('')
    print('Введите имя второго игрока:  ')
    player2 = input('>>>  ')
    print('Привет!', player2)
    print('')
    rand = random.randint(0, 10)
    print('Число игрока 1: ', rand)
    rand2 = random.randint(0, 10)
    print('Число игрока 2: ', rand2)
    player1 = rand
    player2 = rand2
    if player1 > player2:
        print('Выйграл игрок 1')
    elif player1 < player2:
        print('Выйграл игрок 2')
    else:
        print('Ничья')
        main()

main()
