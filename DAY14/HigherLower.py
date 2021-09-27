import random
import os
clear = lambda: os.system('cls')
vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
values = [
   {
      "name": "Dybala",
      "value": 50
   },
   {
      "name": "Chiesa",
      "value": 70
   },
   {
      "name": "Neymar",
      "value":100,
   },
   {
      "name": "Ronaldo",
      "value": 45
   },
   {
      "name": "Morata",
      "value":55
   },
   {
      "name": "Haaland",
      "value":110
   },
   {
      "name": "Higuain",
      "value":15
   },
   {
      "name": "Bonucci",
      "value":20
   }
]
test = []
gameS = 0
gamet = 0
valueslen = []
for i in values:
   valueslen.append(values.index(i))
a = random.choice(valueslen)
b = random.choice(valueslen)


def game(A, B):
   global gameS, gamet, clear
   
   AA = A
   BB = B
   Aname = values[A]["name"]
   Avalue = values[A]["value"]
   if gamet > 0:
      print(f"Your current score {gameS}")
   print(f"Compore A: {Aname}")
   print(vs)
   Bname = values[B]["name"]
   Bvalue = values[B]["value"]
   print(f"Compore B: {Bname}")
   AB = input("He is have a high value :")
   if (AB == "A" and Avalue > Bvalue) or (AB == "B" and Bvalue > Avalue) or ((AB == "A" or AB == "B") and Avalue == Bvalue):
      test.append(valueslen[B])
      valueslen.pop(B)
      b = random.choice(valueslen)
      for i in test:
         valueslen.append(i)
      test.clear()
      clear()
      gamet += 1
      gameS += 1
      
      game(B,b)

   else:
      clear()
      print(f'You are lost{gameS}')
game(a, b)
   
