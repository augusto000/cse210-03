import random

class Card:
    """Simple number card 
    This class holds number of a card.

    Attributes:
        number (int):       Value of the card instance.
        get_card_number():  Assign random number to the card instance. 
    """
    def __init__(self):
        self.number = 0
        self.get_card_num()
    
    def get_card_num(self):
        #Individual cards are represented as a number from 1 to 13.(Augusto)
        # this function each time that is called return a 
        # random number(1 to 13)#
        self.number = random.randint(1, 13)