from warship import WarShip

def main():

    warship = WarShip("Duke", 20, 2000, 4, 16, 32, 2)
    warship2 = WarShip("Queen", 20, 2100, 2, 32, 100, 4)

    warship.get_stats()
    warship2.get_stats()

    warship.battle(2,warship2)
    warship.battle(1,warship2)
    warship.battle(0,warship2)

main()