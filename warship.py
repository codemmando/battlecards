
class WarShip():
    
    def __init__(self, class_name, max_speed, range, main_guns = None, ssm = None, sam = None, ciws = None):
        self.class_name = class_name
        self.stats = [max_speed, range, main_guns, ssm, sam, ciws]

    def get_stats(self):
        print(f"\nClass: {self.class_name}")
        print(f"---------stats----------")
        print(f"Max speed: {self.stats[0]} knots")
        print(f"Range: {self.stats[1]} nm")
        print(f"Main guns: {self.stats[2]}")
        print(f"SSM: {self.stats[3]}")
        print(f"SAM: {self.stats[4]}")
        print(f"CIWS: {self.stats[5]}\n")
    
    def battle(self, stat, other):
        print(f"{self.class_name} is about to battle {other.class_name}\n")
        if self.stats[stat] > other.stats[stat]:
            print(f"{self.class_name} Wins\n") 
        elif self.stats[stat] == other.stats[stat]:
            print(f"Draw between {self.class_name} and {other.class_name}\n")
        else:
            print(f"Defeat {self.class_name} Lost\n")