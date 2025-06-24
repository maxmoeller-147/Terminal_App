import random
import utilities
import opponent









def main():

    while True:

        
        print(
            "\n\n1. Try Drawing a Random Hand\n2. Change Deck\n3. Get away from the Battle\n""4. Initial Decklist\n5. Quit\n\n"
            )
        print("--"*50)
        choice = input ("Choose an Option:")

        print("\n\n")
        
        match choice:
            case "1":
                utilities.draw_hand_from_decklist(num_cards=4)     
            case "2":
                utilities.select_hero_opponent()
            case "3":
                print ("Need to decompress from the fight? Here is a joke:")
            case "4":
                utilities.show_complete_decklist()
            case "5":
                print("Goodbye!")
                break
            case _: 
                print("invalid choice.")
                
if __name__ == "__main__":
             


    main()  