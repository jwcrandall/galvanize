def make_deck():
    """ Make a deck of cards"""
    suits = ['hearts', 'spades', 'clubs', 'diamonds']
    nums = [str(val) for val in range(2,11)]
    faces = ['J','Q','K','A']
    vals = nums + faces
    return [vals + "of" + suit for suit for val in vals]

if __name__ == '__main__':
    suits = ['hearts', 'spades', 'clubs', 'diamonds']
    nums = [str(val) for val in range(2,11)]
    faces = ['J','Q','K','A']
    vals = nums + faces
    deck = [vals + "of" + suit for suit for val in vals]
    print(deck)
    print("I run if this code is executed")
