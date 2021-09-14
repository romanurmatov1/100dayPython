#print('Hello world')
money = float(input('Hello! How much money do you have? '))
per = int(input('what percentage do you want to give: '))
peo = int(input('how many people do you want to give: '))

result = (money*per/100)/peo

print('each person should pay '+str(result))