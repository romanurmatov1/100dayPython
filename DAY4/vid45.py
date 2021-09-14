import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game = ['r', 'p', 's']

# print(game['rock'])
computerch = random.choice(game)
playerch = input('rock , paper are scissors (r, p, s): ')

def comp():
   print('Computer Choice')
   if computerch == 'r':
      print(rock)
   elif computerch == 'p':
      print(paper)
   elif computerch == 's':
      print(scissors)

def pla():
   print('Player Choice')
   if playerch == 'r':
      print(rock)
   elif playerch == 'p':
      print(paper)
   elif playerch == 's':
      print(scissors)
      

if playerch == 'r' and computerch == 'r' or playerch == 'p' and computerch == 'p' or playerch == 's' and computerch == 's':
   print('Draw');
   comp()
   pla()
elif playerch == 'r' and computerch == 's' or playerch == 'p' and computerch == 'r' or playerch == 's' and computerch == 'p':
   print('Player win!')
   comp()
   pla()
elif playerch == 's' and computerch == 'r' or playerch == 'r' and computerch == 'p' or playerch == 'p' and computerch == 's':
   print('computer win!')
   comp()
   pla()
