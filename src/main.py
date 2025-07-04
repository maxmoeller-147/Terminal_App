import random
import utilities
import opponent
import pyjokes


#   Make sure your are in /src in your terminal
#   This is the the main function fro the app.
#   Please to start the app run _python3 main.py_ script
#   Before run the script make sure you are in a virtual enviroment and have pyjokes installed 
#   To install a Virtual Enviroment type:   "python3 -m venv .venv"
#   To activate: "source .venv/bin/activate"
#   To deactivate type ""deactivate"
#   To see if you have pyjokes installed type "pip list"
#   If not installed type "pip install -r requirements.txt"

#   YOU ARE READY TO RUN THE APP. HAVE FUN!   #



def main():

    while True:

        
        print(
            "\n\n1. Try Drawing a Random Hand\n2. Change Deck\n3. Get away from the Battle\n""4. Initial Decklist\n5. Life Calculator\n6. Quit\n\n"
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
                utilities.calculator_of_hero_life()
            case "6":
                print("Goodbye!")
                break
            case _: 
                print("invalid choice.")
                
if __name__ == "__main__":
             


    main()  