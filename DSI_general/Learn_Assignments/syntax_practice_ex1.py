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

def even_odd1(L):
    '''
    Use list comprehension to return a list of the same length with the strings
    "even" or "odd" depending on whether the element in L is even or odd.

    Parameters
    ----------
    L : {list} of {int}

    Returns
    -------
    list : {list} of {str}

    Example
    -------
    >>> even_odd1([6, 4, 1, 3, 8, 5])
    ['even', 'even', 'odd', 'odd', 'even', 'odd']
    '''
    num_list = []
    return list(['odd' if i%2 != 0 else 'even' for i in L])

def even_odd2(L):
    '''
    Use map to return a list of the same length with the strings
    "even" or "odd" depending on whether the element in L is even or odd.

    Parameters
    ----------
    L : {list} of {int}

    Returns
    -------
    list : {list} of {str}

    Example
    -------
    >>> even_odd2([6, 4, 1, 3, 8, 5])
    ['even', 'even', 'odd', 'odd', 'even', 'odd']
    '''
    return list(map(lambda x: 'odd' if x%2 != 0 else 'even', L ))

def filter_words(word_list, letter):
    '''
    Use filter to return the words from word_list which start with letter.

    Parameters
    ----------
    word_list : {list} of words ({str})
    letter : {str}

    Returns
    -------
    list : {list} of words {str}

    Example
    -------
    >>> filter_words(["salumeria", "dandelion", "yamo", "doc loi", "rosamunde",
                      "beretta", "ike's", "delfina"], "d")
    ['dandelion', 'doc loi', 'delfina']
    '''
    # return [x for x in word_list if x[0]==letter]
    return list( filter(lambda x: x[0] == letter, word_list) )

def factors(num):
    '''
    Use filter to return all of the factors of num.

    Parameters
    ----------
    num : {int}

    Returns
    -------
    list : {list} of {int}

    Example
    -------
    >>> factors(15)
    [1, 3, 5, 15]
    '''
    # return  list([x for x in range(1,num) if num % x == 0])
    return list ( filter(lambda x: num % x == 0, range(1, num+1)))

def only_sorted(L):
    '''
    Use filter to return only the lists from L that are in sorted order.
    Hint: the all function may come in handy.

    Parameters
    ----------
    L : {list} of {list} of {int}

    Returns
    -------
    list : {list} of {list} of {int}

    Example
    -------
    >>> only_sorted([[3, 4, 5], [4, 3, 5], [5, 6, 3], [5, 6, 7]])
    [[3, 4, 5], [5, 6, 7]]
    '''
    #list(map(lambda x: sorted(x), L))
    # return list( filter(lambda x: all(x in L for x in L), L))
    # return list( filter( [all( L[x] == sorted(L[x])) for x in L] ))
    return list( filter(lambda x: x == sorted(x), L))

def digits_to_num(digits): # Does not work
    '''
    Use reduce to take a list of digits and return the number that they
    correspond to. Do not convert the integers to strings.

    Parameters
    ----------
    digits : {list} of {int}

    Returns
    -------
    int : {int}

    Example
    -------
    >>> digits_to_num([5, 0, 3, 8])
    5038
    '''
    import functools
    return functools.reduce(lambda x,y: str(x) + str(y) , digits)

def intersection_of_sets(list_of_sets):
    '''
    Use reduce to take the intersection of a list of sets.
    Hint: the & operator takes the intersection of two sets.

    Parameters
    ----------
    list_of_sets : {list} of {set}

    Returns
    -------
    set : intersection of all sets in list_of_sets

    Example
    -------
    >>> intersection_of_sets([{1, 2, 3}, {2, 3, 4}, {2, 5}])
    set([2])
    '''
    return reduce(lambda x,y: x&y, list_of_sets)

def shift_on_character(string, char):
    '''
    Find the first occurence of the character char and return the string with
    everything before char moved to the end of the string. If char doesn't
    appear, return the same string.

    Parameters
    ----------
    string : {str}
    char : {str}

    Returns
    -------
    str

    Example
    -------
    >>> shift_on_character("galvanize", "n")
    'nizegalva'
    '''
    if char not in string:
        return string;
    else:
        start_num = string.index(char)
        return string[start_num:]+string[:start_num];
    pass

def is_palindrome(string):
    '''
    Return whether the given string is the same forwards and backwards.

    Parameters
    ----------
    string : {str

    Returns
    -------
    bool

    Example
    -------
    >>> is_palindrome("rats live on no evil star")
    True

    >>> is_palindrome("the moon waxes poetic in sunlight")
    False
    '''
    return string == string[::-1]

def alternate(L):
    '''
    Use list slicing to return a list containing all the odd indexed elements
    followed by all the even indexed elements.

    Parameters
    ----------
    L : {list}

    Returns
    -------
    list : {list}

    Example
    -------
    >>> alternate(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
    ['b', 'd', 'f', 'a', 'c', 'e', 'g']
    '''
    return L[1::2] + L[0::2]

def shuffle(L):
    '''
    Return the result of a "perfect" shuffle. You may assume that L has even
    length. You should return the result of splitting L in half and alternating
    taking an element from each.

    Parameters
    ----------
    L : {list}

    Returns
    -------
    list : {list}

    Example
    -------
    >>> shuffle([1, 2, 3, 4, 5, 6])
    [1, 4, 2, 5, 3, 6]
    '''
    shuffled = []
    for i in range(len(L) // 2):
        shuffled.append(L[i])
        shuffled.append(L[i+len(L) // 2])
    return shuffled
    # return [x]
def count_match_index(L):
    '''
    Use enumerate and other skills to return the count of the number
    of items in the list whose value equals its index.

    Parameters
    ----------
    L : {list} of {int}

    Returns
    -------
    int : {int}

    Example
    -------
    >>> count_match_index([0, 2, 2, 3, 6, 5])
    4
    '''
    return len([x for x in enumerate(L) if x[0]==x[1]])

def invert_list(L):
    '''
    Use enumerate and other skills to return a dictionary which has
    the values of the list as keys and the index as the value. You may assume
    that a value will only appear once in the given list.

    Parameters
    ----------
    L : {list}

    Returns
    -------
    dict : keys are entries in L, vallues are the index

    Example
    -------
    >>> invert_list(['a', 'b', 'c', 'd'])
    {'a': 0, 'c': 2, 'b': 1, 'd': 3}
    '''
    return {value:key for key, value in enumerate(L)}

def concatenate(L1, L2, connector=""):
    '''
    L1 and L2 have the same length. Use zip and other skills from above to
    return a list of the same length where each value is the two strings from
    L1 and L2 concatenated together with connector between them.

    Parameters
    ----------
    L1 : {list} of {str}
    L2 : {list} of {str}
    connector : {str} (optional)

    Returns
    -------
    list : {list} of {str}

    Example
    -------
    >>> concatenate(["A", "B"], ["b", "b"])
    ['Ab', 'Bb']
    >>> concatenate(["San Francisco", "New York", "Las Vegas", "Los Angeles"], \
                    ["California", "New York", "Nevada", "California"], ", ")
    ['San Francisco, California', 'New York, New York', 'Las Vegas, Nevada', 'Los Angeles, California']
    '''
    return str([ (x[0], x[1]) for x in zip(L1,L2)])
    return str([ (x[0] + x[1]) for x in zip(L1,L2)])
    # return [(a,b) for a,b zip(L1,L2)]

def transpose(mat):
    '''
    Return the transpose of the matrix. You may assume that the matrix is not
    empty. You can do this using a double for loop in a list comprehension.
    There is also a solution using zip.

    Parameters
    ----------
    mat : {list} of {list} of {int}

    Returns
    -------
    list : {list} of {list} of {int}

    Example
    -------
    >>> M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> transpose(M)
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    '''
    # return [zip(*mat) for row in mat]
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]

def acronym(phrase):
    '''
    Given a phrase, return the associated acronym by breaking on spaces and
    concatenating the first letters of each word together capitalized.

    Parameters
    ----------
    phrase : {str}

    Returns
    -------
    str : {str}

    Example
    -------
    >>> acronym("data science immersive")
    'DSI'
    '''
    return ''.join([x[0].upper() for x in phrase.split()])
    # return ''.join( [row[0] for row in phrase.split()] ).upper()

def sort_by_ratio(L):
    '''
    Sort the list L by the ratio of the elements in the 2-tuples.
    For example, (1, 3) < (2, 4) since 1/3 < 2/4.
    Use the key parameter in the sort method.

    Parameters
    ----------
    L : {list} of 2-tuples ({tuple}) of {int}

    Returns
    -------
    None

    Example
    -------
    >>> L = [(2, 4), (8, 5), (1, 3), (9, 4), (3, 5)]
    >>> sort_by_ratio(L)
    >>> L
    [(1, 3), (2, 4), (3, 5), (8, 5), (9, 4)]
    '''
    return sorted(L, key = lambda ratio: ratio[0]/ratio[1])

def string_combinations(alphabet, n):
    '''
    Use itertools.combinations to return all the combinations of letters in
    alphabet with length at most n.

    Parameters
    ----------
    alphabet : {str}
    n : {int}

    Returns
    -------
    list : {list} of {str}

    Example
    -------
    >>> string_combinations('abc', 2)
    ['a', 'b', 'c', 'ab', 'ac', 'bc']
    '''
    import itertools
    # return ["".join(x) for x in itertools.combinations( list(alphabet) , n) ]
    return list(map("".join, (comb for i in range(1, n+1) for comb in itertools.combinations(alphabet, i))) )

def permutations_in_dict(string, words):
    '''
    Use itertools.permutations to return all the permutations of the string
    and return only the ones which are members of set words.

    Parameters
    ----------
    string : {str}
    words : {set}

    Returns
    -------
    list : {list} of {str}

    Example
    -------
    >>> permutations_in_dict('act', {'cat', 'rat', 'dog', 'act'})
    ['act', 'cat']
    '''
    import itertools
    # return [ filter(words in itertools.permutations(string))  ]
    return ["".join(perm) for perm in itertools.permutations(string) if "".join(perm) in
if __name__ == "__main__":
    # mat = [[4, 5, 2, 8], [3, 9, 6, 7]]
    # average_rows1(mat)
    # average_rows2(mat)
    # M = [[4, 5, 2, 8], [3, 9, 6, 7]]
    # sort_rows(M)
    # word_lengths1("Welcome to the Data Science Immersive Program!")
    # print(word_lengths2("Welcome to the Data Science Immersive Program!!"))
    # even_odd1([6, 4, 1, 3, 8, 5])
    # print(filter_words(["salumeria", "dandelion", "yamo", "doc loi", "rosamunde",
    #                   "beretta", "ike's", "delfina"], "d"))
    # print( factors(15) )
    # print( only_sorted([[3, 4, 5], [4, 3, 5], [5, 6, 3], [5, 6, 7]]))
    # print( digits_to_num([5, 0, 3, 8]) )
    # print(alternate(['a', 'b', 'c', 'd', 'e', 'f', 'g']))
    # print( shuffle([1, 2, 3, 4, 5, 6]))
    # print( count_match_index([0, 2, 2, 3, 6, 5]))
    # print( invert_list(['a', 'b', 'c', 'd']))
    print( concatenate(["San Francisco", "New York", "Las Vegas", "Los Angeles"], \
                    ["California", "New York", "Nevada", "California"], ", "))
    print( concatenate(["A", "B"], ["b", "b"]) )
    M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(transpose(M))
    print( acronym("data science immersive"))
    L = [(2, 4), (8, 5), (1, 3), (9, 4), (3, 5)]
    print( sort_by_ratio(L) )
    print( string_combinations('abc', 2))
    print( permutations_in_dict('act', {'cat', 'rat', 'dog', 'act'}) )
