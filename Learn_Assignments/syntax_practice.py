def average_rows1(mat):
    '''
    Use list comprehension to take the average of each row in the matrix and
    return it as a list.

    Parameters
    ----------
    mat : {list} of {list} of numbers ({int or float})

    Returns
    -------
    list : {list} of {float}

    Example
    -------
    >>> average_rows1([[4, 5, 2, 8], [3, 9, 6, 7]])
    [4.75, 6.25]
    '''
    print( list([sum(row)/len(row) for row in mat]) )

def average_rows2(mat):
    '''
    Use map to take the average of each row in the matrix and
    return it as a list.

    Parameters
    ----------
    mat : {list} of {list} of numbers ({int or float})

    Returns
    -------
    list : {list} of {float}

    Example
    -------
    >>> average_rows1([[4, 5, 2, 8], [3, 9, 6, 7]])
    [4.75, 6.25]
    '''
    print( list(map(lambda row: sum(row)/len(row), mat)))

def sort_rows(mat):
    '''
    Use list comprehension to modify each row of the matrix to be sorted.
    Notice that the matrix is modified in place

    Parameters
    ----------
    mat : {list} of {list} of {int}

    Returns
    -------
    None

    Example
    -------
    >>> M = [[4, 5, 2, 8], [3, 9, 6, 7]]
    >>> sort_rows(M)
    >>> M
    [[2, 4, 5, 8], [3, 6, 7, 9]]
    '''
    print( list( [sorted(row) for row in mat] ))

def word_lengths1(phrase):
    '''
    Use list comprehension to find the length of each word in the phrase
    (broken by spaces) and return the values in a list.

    Parameters
    ----------
    phrase : {str}

    Returns
    -------
    list : {list} of {int}

    Example
    -------
    >>> word_lengths1("Welcome to the Data Science Immersive Program!")
    [7, 2, 3, 4, 7, 9, 8]
    '''
    # return [len(x) for x in phrase.split()]
    print( list([len(row) for row in phrase.split()]) )

def word_lengths2(phrase):
    '''
    Use map to find the length of each word in the phrase
    (broken by spaces) and return the values in a list.

    Parameters
    ----------
    phrase : {str}

    Returns
    -------
    list : {list} of {int}

    Example
    -------
    >>> word_lengths2("Welcome to the Data Science Immersive Program!!")
    [7, 2, 3, 4, 7, 9, 8]
    '''
    return list(map(len, phrase.split()) )

if __name__ == "__main__":
    mat = [[4, 5, 2, 8], [3, 9, 6, 7]]
    average_rows1(mat)
    average_rows2(mat)
    M = [[4, 5, 2, 8], [3, 9, 6, 7]]
    sort_rows(M)
    word_lengths1("Welcome to the Data Science Immersive Program!")
    print(word_lengths2("Welcome to the Data Science Immersive Program!!"))
