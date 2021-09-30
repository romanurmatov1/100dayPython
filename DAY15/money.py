
from resources import moneys, summ
def entermoney():
    global moneys, summ
    quarter = int(input('How many quarters?: '))
    dime = int(input('How many dimes?: '))
    nickel = int(input('How many nickels?: '))
    penny = int(input('How many pennies?: '))
    summ = moneys['penny']*penny+moneys['nickel']*nickel + \
        moneys['dime']*dime+moneys['quarter']*quarter