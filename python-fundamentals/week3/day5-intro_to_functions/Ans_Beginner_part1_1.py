def devisors_func(x):
    devisors_list = [i for i in range(1,x+1) if x % i == 0]
    return devisors_list

if __name__ == '__main__':
    user_number = input('Enter a number: ')
    number = int(user_number)
    divs = devisors_func(number)
    print("The divisor are {0}".format(divs))
