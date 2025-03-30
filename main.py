from warship import WarShip
from deck import Deck, battle

def main():

    duke = WarShip("Duke", 20, 2000, [4,80], 16, 32, 2)
    queen = WarShip("Queen", 20, 2100, [2,80], 32, 100, 4)
    king = WarShip("King", 22, 2300, [4,180], 64, 200, 8)
    prince = WarShip("Prince", 32, 1800, [8,60], 8, 16, 1)
    jack = WarShip("Jack", 24, 2200, [1,80], 0, 0, 0)
    hunter = WarShip("Hunter", 42, 200, [4,30], 8, 16, 2)
    head = WarShip("Head", 10, 20100, [0,0], 0, 0, 16)
    warshiplist = [
            duke,
            queen,
            king,
            prince,
            jack,
            hunter,
            head
            ]

    deck1 = Deck()
    deck2 = Deck()

    deck1.draw_hand(warshiplist)
    deck2.draw_hand(warshiplist)

    print(deck1.show_card())
    x = input("pick a stat for the battle: ")
    
    battle(deck1, deck2, int(x))
    #battle(deck1, deck2, 4)
    #battle(deck1, deck2, 1)
    #battle(deck1, deck2, 0)
    #battle(deck1, deck2, 5)
    #battle(deck1, deck2, 2)
    #battle(deck1, deck2, 3)
    #battle(deck1, deck2, 1)
    #battle(deck1, deck2, 2)
    print(deck1)
    print(deck2)
    deck1.shuffle()
    print(deck1)
   

main()