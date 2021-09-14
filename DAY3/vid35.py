#print('Hello world')
name1 = input('Enter a name1')
name2 = input('Enter a name2')

a = 1
fullname1 = name1+name2
fullname = fullname1.lower()
trueT = fullname.count('t')
trueR = fullname.count('r')
trueU = fullname.count('u')
trueE = fullname.count('e')
trueResult = trueT + trueR + trueU + trueE

loveL = fullname.count('l')
loveO = fullname.count('o')
loveV = fullname.count('v')
loveE = fullname.count('e')
loveResult = loveL + loveO + loveV + loveE

result = str(trueResult) + str(loveResult)
resultint = int(result)
if resultint < 10 or resultint > 90:
   print(f'Your score is {result}, you go together like coke and mentos.')
elif resultint > 40 and resultint < 50:
   print(f'Your score is {result}, you goare alright together.')
else:
   print(f'Your score is {result}.')
   


