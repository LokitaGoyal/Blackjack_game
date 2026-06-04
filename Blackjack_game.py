import random

suits=["spades","clubs","hearts","diamonds"]
cards={"A": 11,
       "2": 2,
       "3": 3,
       "4": 4,
       "5": 5,
       "6": 6,
       "7": 7,
       "8": 8,
       "9": 9,
       "10": 10,
       "J": 10,
       "Q": 10,
       "K": 10}
deck=[]
for suit in suits:
    for rank,value in cards.items():
        deck.append([rank,suit,value])
random.shuffle(deck)

def total(hand):
    total = 0
    for card in hand:
        total += card[2]
    return total

def play_game():
    print("Welcome to Blackjack.")
    print("Let's play a best of 3 games.")
    total_games = 0
    dealer_score = 0
    player_score = 0
    while total_games < 3:
        player_cards=[]
        dealer_cards=[]

        #Dealer Cards
        while len(dealer_cards) != 2:
            dealer_cards.append(deck.pop())
            if len(dealer_cards) == 2:
                print("Dealer has X &", dealer_cards[1])

         # Player Cards
        while len(player_cards) != 2:
            player_cards.append(deck.pop())
            if len(player_cards) == 2:
                print("You have ", player_cards)
         
        # Sum of the Dealer cards
        if total(dealer_cards) == 21:
            # 2) Add 1 for dealer
            dealer_score += 1
            print("Dealer has 21 and wins!")
        elif total(dealer_cards) > 21:
            # 2) Add 1 for player
            player_score += 1
            print("Dealer has busted!")

        # Sum of the Player cards
        while total(player_cards) < 21:
            action_taken = str(input("Do you want to stay or hit?  "))
            if action_taken == "hit":
                player_cards.append(deck.pop())
                print("You now have a total of " + str(total(player_cards)) + " from these cards ", player_cards)
            else:
                print("The dealer has a total of " + str(total(dealer_cards)) + " with ", dealer_cards)
                print("You have a total of " + str(total(player_cards)) + " with ", player_cards)
                if total(dealer_cards) > total(player_cards):
                    # 2) Add 1 for dealer
                    dealer_score += 1
                    print("Dealer wins!")
                else:
                    # 2) Add 1 for player
                    player_score += 1
                    print("You win!")
                    break

        if total(player_cards) > 21:
            # 2) Add 1 for dealer
            dealer_score += 1
            print("You BUSTED! Dealer wins.")
        elif total(player_cards) == 21:
            # 2) Add 1 for player
            player_score += 1
            print("You have BLACKJACK! You Win!! 21")

        # Text to inform the player of the status of the game and iterate over the total_games
        print("Current Best of 3: Dealer - " , str(dealer_score) ,  " times wins & You " + str(player_score) + " times wins")
        total_games += 1

play_game()
