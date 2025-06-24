import opponent



#   Flow Control Estructure with classes that inherents from the class Hero.

def select_hero_opponent():

    P1 = opponent.Warrior("Dorinthea","Agressive")
    P2 = opponent.Guardian("Victor","Very Defensive")
    P3 = opponent.Wizard("Oscilio","Very Aggresive")
   
    print ("Please, select the class of your Opponent Hero:\n1.Warrior\n2.Guardian\n3.Wizard\n")

    choice = input("\nEnter the number of your Choice:")

    if choice == "1":
        print("\nYou Selected Warrior\n")
        print(f"{P1.name} plays {P1.playstyle} attacking with her signiature sword multiple times during the turn while surprising the opponent with attack reaction cards")
        P1.change_deck()
    elif choice == "2":
        print("You Selected Guardian")
        print(f"{P2.name} plays {P2.playstyle} blocking most of the time with very good defensive cards while setting up a huge and devastating phisical attack")
        P2.change_deck()
    elif choice == "3":
        print("You Selected Wizard")
        print(f"{P3.name} plays {P3.playstyle} attacking with multiple electric attacks and finish the turn with a huge magical attack")
        P3.change_deck()
    else:
        print("Invalid Selection. Please Try Again")
        select_hero_opponent()

if __name__ == "__main__":
    select_hero_opponent()





def show_complete_decklist():
     with open('decklist.json','r') as f:
        cards = json.load(f)
     for card, quantity in cards.items():
        print(f"{quantity}x {card}")

if __name__ == "__main__":

    show_complete_decklist()






def draw_hand_from_decklist(num_cards=4):
    with open("decklist.json", "r") as f:
        decklist = json.load(f)
        random_hand = random.sample(list(decklist.keys()), num_cards)
    for card in random_hand:
        print(card)

if __name__ == "__main__":

    draw_hand_from_decklist()