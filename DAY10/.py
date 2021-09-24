bosh = int(input('Nechadan boshlangan: '))
end = int(input('Nechada tamom bulgan: '))+1
for a in range(bosh,end):
   filename = 'vid'+str(a) + '.py'
   with open(filename, 'w') as f:
    f.write("#print('Hello world')");