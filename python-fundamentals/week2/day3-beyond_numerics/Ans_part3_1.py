# Write a script that creates a list of only the even numbers between 0
# and a user inputted number.
user_number = ''
while not user_number.isdigit():
    user_number = raw_input('Please input a number to get the evens up to: ')
user_number = int(user_number)

evens = []
# For loop way to do this.
for num in range(1, user_number): 
    if not num % 2:
        evens.append(num)

# List comp. way to do this.
evens = [num for num in range(1, user_number) if not num % 2]

print(evens)
