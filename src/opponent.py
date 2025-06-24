import csv




class Hero:
    def __init__(self, name):
        self.name = name





class Warrior(Hero):
    def __init__(self, name, playstyle):
        super().__init__(name)
        self.playstyle = playstyle

    def change_deck(self):
        print(f"Do you want to change your decklist against {self.name}?\n")

        choice = input("Yes or No?")
        

        if choice.lower() == "yes":
            new_deck = [
                ["Blade Flurry (red)", 3],
                ["Draw Swords (red)", 3],
                ["Fate Foreseen (red)", 3],
                ["Hit and Run (red)", 3],
                ["Outland Skirmish (red)", 3],
                ["Slice and Dice (red)", 3],
                ["Spoils of War (red)", 3],
                ["Unsheathed (red)", 3],
                ["Blood on Her Hands (yellow)", 3],
                ["Draw Swords (yellow)", 3],
                ["Hit and Run (yellow)", 3],
                ["Outland Skirmish (yellow)", 3],
                ["Raise an Army (yellow)", 3],
                ["Stacking Gold (yellow)", 3],
                ["Seduce Secrets (yellow)", 2],
                ["Sharpened Senses (yellow)", 3],
                ["Blade Runner (blue)", 3],
                ["Glint the Quicksilver (blue)", 3],
                ["Hit and Run (blue)", 3],
                ["Provoke (blue)", 3],
                ["Trot Along (blue)", 3],
                ["Gorganian Tome", 1],
                ["Gold Gem", 1]
            ]
            with open("Deck_Againts_Warrior.csv", mode='w', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerows(new_deck)
            

            def read_new_deck():
                with open("Deck_Againts_Warrior.csv", newline='') as f:
                    csv_reader = csv.reader(f)
                    for row in csv_reader:
                        name, qty = row
                        print(f"{name} x{qty}")
            
            read_new_deck()

            print(f"\nDecklist Updated to play against {self.name}\n\n")

        else:
            print("\nNo changes were made\n")

        print("--"*50)

if __name__ == "__main__":
    warrior = Warrior("Warrior", "Aggresive")
    warrior.change_deck()