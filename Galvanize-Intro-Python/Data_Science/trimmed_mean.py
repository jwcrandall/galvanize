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

'''
for i,v in enumerate(my_list):
'''
'''
num_list = [2, 5, 6, 4, 10, 8]


                
# return to enumerate method i,j
def get_divisors(num_list):
    x = []
    for i in range(len(num_list)):
        if i == 
        print(len(i))
            if num_list[i] % num_list[i+1] == 0:
                x.append(num_list[i])
                print(num_list[i])
    return(x)               
                

print(get_divisors([2, 5, 6, 4, 10, 8]))

# -> [2, 5, 4]
print(get_divisors([3, 9]))
# -> [3]
# Scratcg Code:
inv_map = {v: k for k, v in cipher_alphabet.items()}
'''
#_____________________________________________________

#my_list.remove(item)

#Given a list of numbers, compute the mean of those numbers excluding the min and the max value.
def trimmed_mean(num_list):
    temp = [item for item in num_list if item != min(num_list) and item != max(num_list)]    
    return(sum(temp)/(len(temp)))
'''
    for i in range(num_list):
        if num_list[i] == min(num_list) or num_list[i] == max(num_list):
'''
'''
def trimmed_mean(num_list):
    temp_list = num_list
    min_num = min(num_list)
    max_num = max(num_list)
    for i in num_list:
        print('i', i)
        print("min", min_num)
        print("max", max_num)
        print(" temp-1", temp_list)
        if i == min_num or i==max_num:
            temp_list = temp_list.remove(i)
        print(" temp-2", temp_list)   
    print(temp_list.remove(min_num and max_num))
    return(sum(temp_list)/(len(temp_list)))
'''
print(trimmed_mean([1,1,3,4,5]))
#3.5
print(trimmed_mean([3,1,1,4,5,5]))
#3.5
print(trimmed_mean([3,1,1,4,5,5,2,2]))
#2.75
