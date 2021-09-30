from resources import MENU, profit, resources, moneys, summ, report
from money import entermoney
def coffe():
    global moneys, summ, profit
    text = input('What would you like? (espresso/latte/cappucino): ')
    if text == 'report':
        report()
        coffe()
    else:
        entermoney()
        if summ < MENU[text]['cost']:
            print('money not enough')
        else:
            for i in MENU[text]['ingredients']:
                if resources[i]<MENU[text]['ingredients'][i]:
                    print(f'{i} not enough')
                    coffe()
                resources[i] = resources[i] - MENU[text]['ingredients'][i]  
            summ = summ - MENU[text]['cost']
            profit = profit + MENU[text]['cost']
            print(f'Here is {summ} in change')
            print(f'Here is your {text} Enjoy');
        coffe()
coffe()
