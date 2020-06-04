#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 14:49:50 2017

@author: rdelapp
"""
# Import Statements
from re import match, I
from itertools import combinations


class QuestionFive:

    def __init__(self):
        pass

    @staticmethod
    def matching_pairs(data_list):

        # Preallocate Output
        data_output = list()

        # To simplify reading if statement, check if string has two vowels or two consonants
        letter_checker = '(([aieou]*[aieou]{2,})|(([bcdfghjklmnpqrstvwxyz]*[bcdfghjklmnpqrstvwxyz]){2,}))'

        for subset in combinations(enumerate(data_list), 2):

            # Pointer Clarification for Tuple Arrangement
            ((first_index, (first_letter, first_number)),
             (second_index, (second_letter, second_number))) = subset
            
            # Verify both letters are consonants/vowels AND the sum of numbers is a multiple of 3
            if match(letter_checker, (first_letter + second_letter), flags=I) is not None and \
                    (first_number + second_number) % 3 is 0:
                data_output.append((first_index, second_index))

        return data_output

if __name__ == '__main__':

    # From Question 5 Example
    data = [('a', 4), ('b', 5), ('c', 1), ('d', 3), ('e', 2), ('f', 6)]

    # Execute Program
    app = QuestionFive()
    output = app.matching_pairs(data)

    # Print Output
    print(output)