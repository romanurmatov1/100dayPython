# print('Hello world')
leapyear = False;
def is_leap(year):
      global leapyear
      if year % 4 == 0:
         if year % 100 == 0:
            if year % 400 == 0:
               leapyear = True;
            else:
               leapyear = False;
         else:
            leapyear = True;
      else:
         leapyear = False;

def days_in_month(year, month):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  is_leap(year)
  if leapyear:
     if month == 1:
        return 29
     else:
        return month_days[month]
  else:
     return month_days[month]
  
  
# 🚨 Do NOT change any of the code below 
year1 = int(input("Enter a year: "))
month1 = int(input("Enter a month: "))
days = days_in_month(year1, month1-1)
print(days)
