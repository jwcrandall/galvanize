def get_mean(lst):
    """
    INPUT: list of ints/floats
    RETURNS: the mean value of the input list as a float

    """
    return float(sum(lst))/float(len(lst))


def get_median(lst):
    """
    INPUT: list of ints/floats
    RETURNS: the median value of the input list as a float

    """
    tmp = sorted(lst)
    if len(tmp) % 2 == 0:
        return (float(tmp[(len(tmp) // 2)]) + float(tmp[(len(tmp) // 2) + 1]) ) / 2
    else:
        return  (float(tmp[(len(tmp) // 2)])


def get_mode(lst):
    """
    INPUT: list of ints/floats
    RETURNS: the modal value of the input list as a float

    """

    # most = max(list(map(lst.count, lst)))
    return max(set(lst), key=lst.count)
    # return list(set(filter(lambda x: lst.count(x) == most, lst)))

    """ +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"""

import numpy as np

def get_range(lst):
    """
    INPUT: list of ints/floats
    RETURNS: the range of the input list - the distance from the minimum value to the maximum value

    """
    return min(lst), max(lst)


def get_IQR(lst):
    """
    INPUT: list of ints/floats
    RETURNS: the interquartile range of the input list - the distance from Q1 (25th percentile) to Q3 (75th percentile)

    hint: use [np.percentile](https://docs.scipy.org/doc/numpy-dev/reference/generated/numpy.percentile.html)

    """
    return np.percentile(lst, 75) - np.percentile(lst, 25)


def remove_outliers(lst):
    """
    INPUT: list of ints/floats
    RETURNS: two lists
              - a list of all data points that fall either 3 times the IQR above Q3 or 3 times the IQR below Q1
              - a list of all remaining points

    """
    return [x for x in lst if x <= 3 *IQR + np.percentile(lst, 75) or x <= 3 *IQR +  np.percentile(lst, 25)],
    [x for x in lst if x > 3 *IQR + np.percentile(lst, 75) or x >  np.percentile(lst, 25) - 3 *IQR ]

    

if __name__ == '__main__':
print(get_mean([ 1, 2, 3, 4, 5))
print(get_median([ 1, 2, 3, 4, 5, 6,7]))
print(get_median([ 1, 2, 3, 4, 5, 6]))
