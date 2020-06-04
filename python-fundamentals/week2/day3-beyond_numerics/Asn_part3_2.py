# Write a script that creates a list of only numbers divisible by a user
#inputted number that are between 0 and a user inputted number
user_num1 = ''
user_num2 = ''

while not user_num1.isdigit() and not user_num2.isdigit():
    user_num1 = raw_input('Please enter a digit to divide other digits by: ')
    user_num2 = raw_input('Please enter a digit to go up to for our search: ')

user_num1 = int(user_num1)
user_num2 = int(user_num2)

# For loop way to do this.
divisible_nums = []
for num in range(1, user_num2):
    if not num % user_num1:
        divisible_nums.append(num)

# List comp. way to do this.
# divisble_nums = [num for num in range(1, user_num2) if not num % user_num1]
print divisible_nums
