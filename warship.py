import colors

class WarShip():
    
    def __init__(self, class_name, max_speed, range, main_gun = [], ssm = None, sam = None, ciws = None):
        self.class_name = class_name
        self.stats = [max_speed, range, main_gun, ssm, sam, ciws]

    def get_stats(self):
        colors.print_cyan(f"\nClass: {self.class_name}\n---------stats----------\nMax speed: {self.stats[0]} knots\nRange: {self.stats[1]} nm\nMain gun: {self.stats[2][0]}\nMain gun caliber: {self.stats[2][1]}\nSSM: {self.stats[3]}\nSAM: {self.stats[4]}\nCIWS: {self.stats[5]}\n")
           
  