
class Deck():

    def __init__(self):
        self.warships = []

    def set_deck(self, warships):
        self.warships = warships

    def __repr__(self):
        warships_names = "Deck contains\n"
        for warship in self.warships:
            warships_names += f"{warship.class_name}\n"
        return warships_names
    
    def discard(self): 
        if len(self.warships) == 0:
            raise Exception("deck is empty")
        self.warships.pop(0)
        