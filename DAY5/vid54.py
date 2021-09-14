#print('Hello world')
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)
# print(letters[:3])
# print(numbers[:3])
# print(symbols[:3])
ln = int(input('How many letters would you like in your password? '))
sn = int(input('How many symbols would you like? '))
nn = int(input('How many numbers would you like? '))
shl = letters[:ln]
shn = numbers[:nn]
shs = symbols[:sn]
full = shl+shn+shs
random.shuffle(full)
full1 = ''.join(full)
print(full1)