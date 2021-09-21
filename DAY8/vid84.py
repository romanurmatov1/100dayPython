#print('Hello world')
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
a = []
# text = text1.split()
# for ii in text:
#    for i in ii:
#       i = alphabet[alphabet.index(i)+shift]
      


for i in list(text):
   if i in alphabet:
      a.append(alphabet[alphabet.index(i)-shift])
   else:
      a.append(i)
result = ''.join(a)
print(result)