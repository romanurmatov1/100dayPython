#print('Hello world')
height = input('Enter a your height: ')
mass = input('Enter a massa: ')

bmi = int(mass)/(float(height)**2)
if bmi < 18.5:
   print('You have less massa.')
elif bmi > 18.5 and bmi<25:
   print('You have normal massa.')
elif bmi > 25 and bmi<30:
   print('You have less overbalance massa.')
elif bmi > 30 and bmi<35:
   print('You have less overbalance massa.')
elif bmi > 35:
   print('You have less overbalance massa.')