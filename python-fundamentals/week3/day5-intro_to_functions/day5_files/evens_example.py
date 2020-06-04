import pdb # import python debugger

def _even(num):
    '''Private function returns True if the integer is even'''
    return num % 2 == 0


def get_evens_in_range(low=0, high=10):
    '''Returns a list of the evens in the range from low to high, including low
       and high.

    Parameters: low: int
                     The lower limit value to be evaluated

                high: int
                      The upper limit value to be evaulated.

    Returns evens_lst: list of even integers from low to high'''

    if not (isinstance(low, int) and isinstance(high, int)):
        raise ValueError('The arguments must be integers.')

    evens_lst = []
    # pdb.set_trace() #usually placed in main or in function just before problem
    for number in range(low, high):
        if _even(number):
            evens_lst.append(number)
    return evens_lst


if __name__ == '__main__':
    # pdb.set_trace() #usually placed in main or in function just before problem
    # All commands after this script will not be excicuted else called up on.

    limit_low = 1
    limit_high = 4
    my_evens_1 = get_evens_in_range(low=limit_low, high=limit_high) # OK - uses keyword arguments
    my_evens_2 = get_evens_in_range(high=limit_high, low=limit_low) # OK - uses keyword arguments

    my_evens_3 = get_evens_in_range(1, 4)  #OK - uses positional arguments (low_limit defined first)

    my_evens_4 = get_evens_in_range(1, high=4)  #OK - positional and keyword, keyword is last

    # my_evens_5 = get_evens_in_range(low=1, 4)  #ERROR - positional must always come first

    print("My_evens_1 list: {0}".format(my_evens_1))
