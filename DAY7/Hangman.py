import random
import sys
fruits = ['quramboy', 'sharapat', 'mamarayim', 'eshimmat', 'hikmat', 'raxmatjon', 'murod', 'muhiddin']
rfruit = random.choice(fruits)
keyw = (len(rfruit)*'_ ')[:-1]
frlist = list(rfruit);
keywlist = keyw.split();
life = 0
step = 0
   
def game():
   global life, step
   keyw = ' '.join(keywlist)
   keyww = ''.join(keywlist)
   if keyww == rfruit:
      print('\nMolodes brat topdingiz\n')
      sys.exit()
   else:
      if life < 5:      
         if life == 0:
            if step == 0:
               print(f'\n{fruits}\n')
               print('_________________\n|         \n|         \n|         \n|       \ O /                 Nagap Brat szda 5 shans bo\n|         |\n|      _/___\_\n|      |     |')
            else:
               print('_________________\n|         \n|         \n|         \n|       \ O /                 Brat szda 5 shans bo\n|         |\n|      _/___\_\n|      |     |')
         elif life == 1:
            print('_________________\n|         |\n|         \n|         \n|       \ O /    Brat qarang 4 shans qoldi\n|         |\n|      _/___\_\n|      |     |')
         elif life == 2:
            print('_________________\n|         |\n|         |\n|         \n|       \ O /    Brat shatdingiz 3 shans qoldi\n|         |\n|      _/___\_\n|      |     |')
         elif life == 3:
            print('_________________\n|         |\n|         |\n|         |\n|       \ O /    Brat galdi bi 2 shans qoldi\n|         |\n|      _/___\_\n|      |     |')
         elif life == 4:
            print('_________________\n|         |\n|         |\n|         |\n|       \ O /    Brat o\'laman hozir bi 1 shans qoldi\n|         |\n|      _/___\_\n|           ')
         letter = input(f'\nKaroche yuqordayi odlodon birini harfini girit topmosong man o\'laman, qara lekin: {keyw}')
         if len(letter) == 1:
            if letter in frlist:
               if letter not in keyw:
                  for x in range(len(frlist)):
                     if frlist[x] == letter:
                        keywlist[x] = letter
                        step += 1
               else:
                  print('\nBrat aldin giritpadingiz bni :\\n')
                  life += 1
            else:
               print('\nTopavarmadngqu :|\n')
               life += 1
         else:
            print('Kallami bizma harf giritish garak')
         game()
      elif keyww == rfruit:
         print('Malades brat')
         exit1 = input()
      else:      
         print('_________________\n|         |\n|         |\n|         |\n|         O \n|       / | \           Indi fedosi yo\'q o\'ldimqu shansam qolmodi\n|       /   \ \n|           ')
         exit2 = input()
               
         
game()
   
