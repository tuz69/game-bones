import os
from random import randint

rool_1 = randint(1, 6)
rool_2 = randint(1, 6)

rool_3 = randint(1, 6)
rool_4 = randint(1, 6)

rool_5 = randint(1, 6)
rool_6 = randint(1, 6)

rool_7 = randint(1, 6)
rool_8 = randint(1, 6)
def game():
    player = input('\nВведите количество игроков: ')

    if player == '1':
       name1 = input('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\nИмя игрока: ')

       print('▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\nИгроку: ' + name1 + '\nВыпали кости номиналом: ' + str(rool_1) + ' и ' + str(rool_2) + '\n')
       summa_1 = rool_1 + rool_2
       print('Всего выпало: ' + str(summa_1) + '\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
       print('Выиграл: ' + str(name1))

    elif player == '2':
       name1 = input('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\nИмя первого игрока: ')
       name2 = input('Имя второго игрока: ')
   
   
   
       print('▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\nИгроку: ' + name1 + '\nВыпали кости номиналом: ' + str(rool_3) + ' и ' + str(rool_1))
       summa_2 = rool_1 + rool_3
       print('\nВсего выпало: ' + str(summa_2))

       print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\nИгроку: ' + name2 + '\nВыпали кости номиналом: ' + str(rool_4) + ' и ' + str(rool_2))
       summa_3 = rool_4 + rool_2
       print('\nВсего выпало: ' + str(summa_3) + '\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
       win_2 = max(summa_2, summa_3)
       if win_2 == int(summa_2):
           print('Выиграл: ' + str(name1))
       elif win_2 == int(summa_3):
   	       print('Выиграл: ' + str(name2))
       elif int(summa_2) == int(summa_3):
   	       print("Ничия)")

    elif player == '3':
       name1 = input('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\nИмя первого игрока: ')
       name2 = input('Имя второго игрока: ')
       name3 = input('Имя третьего игрока: ')
   
       print('▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\nИгроку: ' + name1 + '\nВыпали кости номиналом: ' + str(rool_3) + ' и ' + str(rool_2))
       summa_4 = rool_3 + rool_2
       print('\nВсего выпало: ' + str(summa_4) + '\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')

       print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\nИгроку: ' + name2 + '\nВыпали кости номиналом: ' + str(rool_1) + ' и ' + str(rool_4))
       summa_5 = rool_1 + rool_4
       print('\nВсего выпало: ' + str(summa_5) + '\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')

       print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\nИгроку: ' + name3 + '\nВыпали кости номиналом: ' + str(rool_5) + ' и ' + str(rool_6))
       summa_6 = rool_5 + rool_6
       print('\nВсего выпало: ' + str(summa_6) + '\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
   
       win_3 = max(summa_4, summa_5,summa_6)
       if win_3 == int(summa_4):
           print('Выиграл: ' + str(name1))
       elif win_3 == int(summa_5):
           print('Выиграл: ' + str(name2))
       elif win_3 == int(summa_6):
           print('Выиграл: ' + str(name3))   	    	

    elif player == '4':
       name1 = input('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\nИмя первого игрока: ')
       name2 = input('Имя второго игрока: ')
       name3 = input('Имя третьего игрока: ')
       name4 = input('Имя четвертого игрока: ')
   
       print('▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\nИгроку: ' + name1 + '\nВыпали кости номиналом: ' + str(rool_3) + ' и ' + str(rool_2))
       summa_7 = rool_3 + rool_2
       print('\nВсего выпало: ' + str(summa_7) + '\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')

       print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\nИгроку: ' + name2 + '\nВыпали кости номиналом: ' + str(rool_1) + ' и ' + str(rool_4))
       summa_8 = rool_1 + rool_4
       print('\nВсего выпало: ' + str(summa_8) + '\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')

       print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\nИгроку: ' + name3 + '\nВыпали кости номиналом: ' + str(rool_5) + ' и ' + str(rool_6))
       summa_9 = rool_5 + rool_6
       print('\nВсего выпало: ' + str(summa_9) + '\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')	 

       print('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\nИгроку: ' + name4 + '\nВыпали кости номиналом: ' + str(rool_7) + ' и ' + str(rool_8))
       summa_10 = rool_7 + rool_8
       print('\nВсего выпало: ' + str(summa_10) + '\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')

       win_4 = max(summa_7, summa_8,summa_9,summa_10)
       if win_4 == int(summa_7):
           print('Выиграл: ' + str(name1))
       elif win_4 == int(summa_8):
           print('Выиграл: ' + str(name2))
       elif win_4 == int(summa_9):
           print('Выиграл: ' + str(name3))
       elif win_4 == int(summa_10):
   	       print('Выиграл: ' + str(name4))   
    elif str(player) > '4':
           print('Не больше 4 игроков!!!')
       	   game()
game()           
while True:
   flag = input('▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒\nЕщё раз? [да/нет]: ')

   if flag == 'да' or 'Да':
       os.system('cls' if os.name == 'nt' else 'clear')
       game()
    elif flag == 'нет' or 'Нет':
        exit()
   else:
       break  

