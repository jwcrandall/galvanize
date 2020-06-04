def common_mult_func(x1, x2)
    user_inputted_num1 = int(x1)
    user_inputted_num2 = int(x2)
    commmon_mult_list  = []

idx = user_inputted_num1
if idx > user_inputted_num2:
    idx = user_inputted_num2

while True:
    if  idx % user_inputted_num1 == 0 and idx % user_inputted_num2 == 0:
        found = True
        print idx
        break
idx += 1

if __name__ == '__main__':
    user_number = input('Enter a number: ')
    number = int(user_number)
    divs = devisors_func(number)
    print("The divisor are {0}".format(divs))
