# Write a script that prompts the user to input numbers separated by dashes ( - ).
# user_str = input("Please enter numbers separated by dashes: ")
user_str = 1-2-3-4-5-6-7-8
user_num = user_str.split('-')
user_num = [int(element.strip()) for element in user_num]
#Your script will take those numbers, and print a dictionary where the keys are
#the inputted numbers, and the values are the squares of those numbers.

sq_num = [user_num[i]**2 for i in user_num]
zip(user_num, sq_num)
