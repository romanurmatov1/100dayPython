#print('Hello world')
print('CALCULATOR')
def glob():
   global num1
   num1 = int(input('What\'s the first number: '))
   def calc():
      global num1
      print('+\n-\n*\n/')
      oper = input('Pick an operator: ')
      num2 = int(input('What\'s the next number: '))
      if oper == '+':
         result = num1 + num2
      elif oper == '-':
         result = num1 - num2
      elif oper == '*':
         result = num1 * num2
      elif oper == '/':
         result = num1 / num2
      
      print(str(num1) , ' ',oper ,' ', str(num2),' = ',str(result))
      next = input(f'Type \'y\' to calculating with {result}, or type \'n\' to start new calculator: ')
      if next == 'y':
         num1 = result
         calc()
      else:
         glob()
   calc()
glob()
      
   