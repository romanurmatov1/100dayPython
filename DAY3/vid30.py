#print('Hello world')
def a():
   year = int(input("Which year do you want to check? "))

   if year % 4 == 0:
      if year % 100 == 0:
         if year % 400 == 0:
            print('This year leap')
            a()
         else:
            print('This year not leap')
            a()
      else:
         print('This year leap')
         a()
   else:
      print('This year not leap')
      a()
a()