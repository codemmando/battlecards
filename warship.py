from colorama import Fore, Style
import time

class WarShip():
    
    def __init__(self, class_name, max_speed, range, main_gun = [], ssm = None, sam = None, ciws = None):
        self.class_name = class_name
        self.stats = [max_speed, range, main_gun, ssm, sam, ciws]

    def get_stats(self):
        self.print_cyan(f"\nClass: {self.class_name}\n---------stats----------\nMax speed: {self.stats[0]} knots\nRange: {self.stats[1]} nm\nMain gun: {self.stats[2][0]}\nMain gun caliber: {self.stats[2][1]}\nSSM: {self.stats[3]}\nSAM: {self.stats[4]}\nCIWS: {self.stats[5]}\n")
    
    def battle(self, stat, other):
        print(f"{self.class_name} is about to battle {other.class_name}\n")
        time.sleep(1)
        if self.stats[stat] > other.stats[stat]:
            self.print_green(f"{self.class_name} Wins\n")
        elif self.stats[stat] == other.stats[stat]:
            self.print_blue(f"Draw between {self.class_name} and {other.class_name}\n")
        else:
            self.print_red(f"Defeat {self.class_name} Lost\n")
            
    def print_red(self, string):
        print(Fore.RED + string + Style.RESET_ALL)
    
    def print_green(self, string):
        print(Fore.GREEN + string + Style.RESET_ALL)
    
    def print_blue(self, string):
        print(Fore.BLUE + string + Style.RESET_ALL)
    
    def print_cyan(self, string):
        print(Fore.CYAN + string + Style.RESET_ALL)