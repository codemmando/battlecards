import colors
import time
import random

class Deck():

    def __init__(self):
        self.warships = []
        self.life = 0

    def set_deck(self, warships):
        self.warships = warships
        self.life = len(warships)

    def __repr__(self):
        warships_names = "Deck contains\n"
        for warship in self.warships:
            warships_names += f"{warship.class_name}\n"
        return warships_names
    
    def discard(self): 
        if len(self.warships) == 0:
            raise Exception("deck is empty")
        self.warships.pop(0)

    def shuffle(self):
        random.shuffle(self.warships)

    def draw_hand(self, warshiplist):
        random.shuffle(warshiplist)
        random.shuffle(warshiplist)
        self.set_deck(warshiplist[:4])

    def show_card(self):
        return self.warships[0].get_stats()

  
    
def battle(deck, other, stat):
        if len(deck.warships) == 0 or len(other.warships) == 0:
            print("No more cards in deck")
            return
        else:
            friendly = deck.warships[0]
            enemy = other.warships[0]
            print(f"{friendly.class_name} is about to battle {enemy.class_name}\n")
            time.sleep(1)
            if friendly.stats[stat] > enemy.stats[stat]:
                colors.print_green(f"{friendly.class_name} Wins\n")
                other.discard()
                other.life -= 1
            elif friendly.stats[stat] == enemy.stats[stat]:
                colors.print_blue(f"Draw between {friendly.class_name} and {enemy.class_name}\n")
                deck.shuffle()
            else:
                colors.print_red(f"Defeat {friendly.class_name} Lost\n")
                deck.discard()
                deck.life -= 1
        

    
            