#112 Day 11: blackjack-final

from random import choice

from replit import clear

from time import sleep

from art import logo

player = {

"player": "user",

"cards": [],

"points": 0,

"blackjack": False}

dealer = {"player": "dealer",

"cards": [],

"points": 0,

"blackjack": False}

game = [ player, dealer ]

dealer_card = []

user_card = []

def choice_card():

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

card = choice(cards)

return card

def sum_cards(card_of_player):

""" Calcute the total points of the player """

if sum(card_of_player) > 21 and 11 in card_of_player:

# replace card ace = 11 if total points > 21

index = card_of_player.index(11)

card_of_player[index] = 1
# replace card ace = 11 if total points > 21

index = card_of_player.index(11)

card_of_player[index] = 1
return sum(card_of_player)

def print_score(): print(f"{player['player'].title()}")

print(f"Score:({player['points']:2}) Cards: {player['cards']} ")

print()

print(f"{dealer['player'].title()}")

print(f"Score:({dealer['points']:2}) Cards: {dealer['cards']} ")

def update_score():

player["points"] = sum_cards( player["cards"])

dealer["points"] = sum_cards( dealer["cards"])

print_score()

def is_blackjack(user):

if user["points"] == 21 and len(user["cards"]) == 2:

user["blackjack"] = True

print(f"\n{user['player'].title()} get BackJack!!")
user["blackjack"] = True

print(f"\n{user['player'].title()} get BackJack!!")
def start_game_conditions():

""" Create begin condition of game """

player["cards"] = []

player["points"] = 0

player["blackjack"] = False

dealer["cards"] = []

dealer["points"] = 0

dealer["blackjack"] = False

clear()

print(logo)

player["cards"] = [choice_card(), choice_card()]

dealer["cards"] = [choice_card()]

update_score()

is_blackjack(player)

def play_game():

end_of_game = False

while not end_of_game:

start_game_conditions()
    if  player["points"] > 21:

      stop = True

      has_winner = True

  else:

    stop = True


# Dealer

if not has_winner:

  stop = False

  while not stop and dealer["points"] <= 16: 

    print("\n---------dealer --------------------\n") 

    sleep(2)  

    dealer["cards"].append(choice_card())

    update_score() 

    is_blackjack(dealer)

    if dealer["blackjack"]:

      stop = True

    sleep(2)


print()

# Polling

winner = "User"

if dealer["points"] <= 21:

  if player["points"] > 21:

    winner = "Dealer"

  elif dealer["points"] == player["points"]:

    winner = ""

  elif player["points"] <= 21:

    if dealer["blackjack"] and not player["blackjack"]:

      winner = "Dealer"

    elif not dealer["blackjack"] and player["blackjack"]:

      winner = "User"
      
    else:

      if dealer["points"] > player["points"]:

        winner = "Dealer"


if winner != "":

  print(f"---->>>> {winner} win!! <<<----" )

else:

  print("The game is drawn!!")

sleep(4)

if input("\nDo you want play again? y or n ").lower() == "n":

  end_of_game = True
start_game_conditions()

has_winner = False

stop = False

# User

stop = False

while not stop and player["points"] < 21 and not player["blackjack"]:

  print()

  if input("More cards?: [y n] ").lower() == "y":

    print("\n------------user-----------------\n") 

    sleep(2) 

    player["cards"].append(choice_card())

    update_score()


    if  player["points"] > 21:

      stop = True

      has_winner = True

  else:

    stop = True


# Dealer

if not has_winner:

  stop = False

  while not stop and dealer["points"] <= 16: 

    print("\n---------dealer --------------------\n") 

    sleep(2)  

    dealer["cards"].append(choice_card())

    update_score() 

    is_blackjack(dealer)

    if dealer["blackjack"]:

      stop = True

    sleep(2)


print()

# Polling

winner = "User"

if dealer["points"] <= 21:

  if player["points"] > 21:

    winner = "Dealer"

  elif dealer["points"] == player["points"]:

    winner = ""

  elif player["points"] <= 21:

    if dealer["blackjack"] and not player["blackjack"]:

      winner = "Dealer"

    elif not dealer["blackjack"] and player["blackjack"]:

      winner = "User"
      
    else:

      if dealer["points"] > player["points"]:

        winner = "Dealer"


if winner != "":

  print(f"---->>>> {winner} win!! <<<----" )

else:

  print("The game is drawn!!")

sleep(4)

if input("\nDo you want play again? y or n ").lower() == "n":

  end_of_game = True
play_game()