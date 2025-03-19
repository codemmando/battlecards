
class WarShip():
    
    def __init__(self, class_name, max_speed, range, main_guns = None, ssm = None, sam = None, ciws = None):
        self.class_name = class_name
        self.max_speed = max_speed
        self.range = range
        self.main_guns = main_guns
        self.ssm = ssm
        self.sam = sam
        self.ciws = ciws

    def get_stats(self):
        print(f"Class: {self.class_name}")
        print(f"---------stats----------")
        print(f"Max speed: {self.max_speed} knots")
        print(f"Range: {self.range} nm")
        print(f"Main guns: {self.main_guns}")
        print(f"SSM: {self.ssm}")
        print(f"SAM: {self.sam}")
        print(f"CIWS: {self.ciws}")