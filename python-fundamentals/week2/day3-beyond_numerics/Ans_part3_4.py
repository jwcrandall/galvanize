# For a user inputted number, write a script that outputs a
# list of multiples of that number from 0 up to another user inputted
# number. For example, given the numbers 4 and 20,
#your script should print the numbers 4, 8, 12, and 16.
user_num1 = ''
user_num2 = ''

while not user_num1.isdigit() and not user_num2.isdigit():
    user_num1 = input('Please enter a digit to to get multiples of: ')
    user_num2 = input('Please enter a digit to go up to for our search: ')

user_num1 = int(user_num1)
user_num2 = int(user_num2)
step = int(user_num2 / user_num1)

# Using a for loop.
# multiples = []
# for num in range(1, step):
#     multiples.append(num * user_num1)
print(multiples)

# Using a list comp.
multiples = [num * user_num1 for num in range(1, step)]
print(multiples)
