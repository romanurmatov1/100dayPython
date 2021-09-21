#print('Hello world')
import os
print('Welcome to the secret auction program.')
win = []

clear = lambda: os.system('cls')

def secret():
   dic = {}
   name = input('what is your name?: ')
   bid = input('What is your bid?: ')
   vo = input('Are there any other bidders? Type "yes" or "no": ' )
   dic["name"] =name;
   dic["bid"] =bid;
   if vo == 'yes':
      clear()
      
   