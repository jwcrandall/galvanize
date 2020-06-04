#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 16:42:32 2017

@author: rdelapp
"""
def letter_counter(path_to_file, letters_to_count):
 ''' Returns the number of times specified letters appear in a file

 Parameters
 -----------
 path_to_file: str
 Relative or absolute path to file of interest
 letters_to_count: str
 String containing the letters to count in the text

 Returns
 --------
 letter_dict: dict
 - key: letter
 - value: the count of that letter in the file
 The counting is case insensitive

 Example
 --------
 ```file.txt
 This is the file of interest. Count my vowels!
 ```
 >>> letter_counter('file.txt', 'aeiou')
 {'i': 4, 'e':4, 'o':2, 'u':1}
 '''
     with open(path_to_file, 'r') as f:
         text = f.read()
    letter_to_count = frozenset(letter_to_count)
    count = 0
    for char in text:
        count += 1
    return count
 pass
