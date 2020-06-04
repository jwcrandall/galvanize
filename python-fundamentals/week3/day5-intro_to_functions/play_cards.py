import random

class Cards():
    def __init__(self, deck = None):
        if deck = None:
            self.deck = [1,2,3,4]
        self.peak = self.deck[-1]

    def shuff(self):
        random.shuffle(self.deck)
        self.peak = self.deck[-1]

    def add_card(self, new_card):
        self.deck.append(new_card)

    def draw_card(self):
        return self.deck.pop()

if __name__ == '__main__':
    my_deck = [1,1,1,3,4,5,3,5,7]
    cards = Cards(my_deck)
