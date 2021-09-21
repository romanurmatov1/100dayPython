#print('Hello world')
import math
pr = 0

def checkp(number):
   global pr
   for i in range(2, number):
      if (number % i) == 0:
         pr = pr + 1;
         
n = int(input('enter a number: '))
checkp(n)

if pr > 0:
   print('not prime')
else:
   print('prime')