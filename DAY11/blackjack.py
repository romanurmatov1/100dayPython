# print('Hello world')
cardspoint = [2, 3, 4, 5, 6, 7, 8, 9,10,11]
player = []
dealer = []
import random

print('Blackjack')
for i in random.sample(cardspoint, k = 2):
   player.append(i)
for i in random.sample(cardspoint, k = 2):
   dealer.append(i)

def game():
   if sum(player) == 21:
      print('Player Win')
   elif sum(dealer) == 21:
      print('Dealer Win')
   elif sum(dealer) > 21:
      print('Player Win')
   elif sum(player) > 21:
      print('Dealer Win')
   else:
      print('Player cards is ', player, ' points: ', sum(player))
      print('Dealer cards is ', dealer, ' points: ', sum(dealer))
      next = input('Choise another card: "y" "n"');
      if next == 'y':
         i = random.choice(cardspoint)
         player.append(i)
         game()
game()
         
   