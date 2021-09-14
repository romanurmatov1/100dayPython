#print('Hello world')
print('Welcome to Treasure Island. Your mission is to find the treasure')
step1 = input('left or right? ')


if step1 == 'left':
   step2 = input('swim or wait? ')
   if step2 == 'wait':
      step3 = input('Which door(Red Blue Yellow)? ')
      if step3 == 'yellow':
         print('You win!')
      else:
         print('Game Over!')
   else:
      print('Game Over!')
else:
   print('Game Over!')