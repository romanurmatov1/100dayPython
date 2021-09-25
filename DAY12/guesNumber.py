
def game():
   import random
   level = input('Are you "easy" or "hard": ')
   if level == 'easy':
      live = 10
   elif level == 'hard':
      live = 5
   random = random.choice(range(1,51))



   print(f'You level is ' + level + ' live: ' + str(live))
   while live > 0:
      num = int(input(f'Enter a number 1 to 50: your live{live} '))
      if num > random:
         print('your number is big')
         live -= 1
      elif num < random:
         print('your number is small')
         live -= 1
      else:
         print('you win')
         input()
         game()
   else:
      print('You are lose')
game()