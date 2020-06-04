"""
Write a class to make an n-sided die
Python3

Attributes
    - total_sides
    - last_roll
Methods
    - return
    - Compare the value of two(2) die values
"""
import sys, random

class BaseDie():
    """
    A base class die
    """

    def __init__(self,n_sides):
        """
        A Base Class for a die
        """

        self.n_sides = n_sides
        self.last_roll = None

    def get_sides(self):
        return(self.n_sides)

    def __str__(self):
        return("Num sides: %s"%self.n_sides)

    def __add__(self,other,other2=None):
        return(self.n_sides + other.n_sides)

    def roll(self):
        return (random.randint(1, self.n_sides))

    def compare_dice(self, other, other2 = None):





if __name__ == "__main__":

    d1 = BaseDie(4)
    d2 = BaseDie(2)

    ## demonstrate magic functions
    print("combined", d1+d2)

    ## inherited class
    apple1 = Apple(4,colors=['g','g','r','r'])
