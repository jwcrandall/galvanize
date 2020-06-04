#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 13:05:33 2017

@author: rdelapp
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# a divisor D of an integer N is an integer that can be multiplied by some other integer to produce N (Wikipedia)

# examples of divisors:
# 2 is a divisor of 8 because 2 x 4 = 8
# 3 is a divisor of 9 because 3 x 3 = 9
# 5 is a divisor of 10 because 5 x 2 = 10

# NOT: 2 is not a divisor of 3
# NOT: 8 is not a divisor of 4


# Write a function, get_divisors, that takes a list of numbers, and returns,
# in a list, those of them divide another element in the input list.
# You may assume that the input list does not contain any duplicates.


                
# return to enumerate method i,j
def get_divisors(num_list):
    x = [] # empty vector
    for i in range(0, len(num_list)):
        for j in range(0, len(num_list)):
            #print("i: ", i, "j: ", j)
            #print("i: ", i, "num_list[i]: ", num_list[i])
            #print("j: ", j, "num_list[j]: ", num_list[j])
           # print("num_list[i]: ", num_list[i], "num_list[j]: ", num_list[j], "Product: ", num_list[i]*num_list[j])

            if num_list[i]*num_list[j] in num_list:
                print("num_list[i]: ", num_list[i], "num_list[j]: ", num_list[j], "Product: ", num_list[i]*num_list[j])
                x.append(num_list[i])
                i += 1; # By adding one to i it makes sure we don't get multiples of the same.
    return(x)               
                

print(get_divisors([2, 5, 6, 4, 10, 8]))
# -> [2, 5, 4]
print(get_divisors([3, 9]))
# -> [3]
# Scratcg Code:
