'''
                Generating a random text: working with functions

Fill in each of the 3 functions below. Complete the 'if __name__' block.

Run "python -m doctest assignment_2a.py" at the command line to test your work.
'''

import random
import string
from sys import argv
from sys import exit


def word_counts(f):
    '''
    INPUT: file
    OUTPUT: dictionary
    Return a dictionary whose keys are all the words in the file (broken by
    whitespace). The value for each word is a dictionary containing each word
    that can follow the key and a count for the number of times it follows it.
    You should lowercase everything.
    Use strip and string.punctuation to strip the punctuation from the words.
    Example:
    >>> #example.txt is a file containing: "The cat chased the dog."
    >>> with open('../data/example.txt') as f:
    ...     word_counts(f)
    {'the': {'dog': 1, 'cat': 1}, 'chased': {'the': 1}, 'cat': {'chased': 1}}
    '''

    words = _get_words_from_file(f) # get list of all words in text file
    all_words = {} # outer dictionary storing all words in text file
    #print(words)

    # add words to dictionary
    for index, word in enumerate(words):
        if (index != len(words) - 1):
        # If not VERY LAST WORD in file...
            subsequent_word = words[index + 1]
            if word not in all_words: # adding a new word
                all_words[word] = {subsequent_word: 1}
            else: # word already in all_words, just need to update inner dict
                if subsequent_word not in all_words[word]:
                    all_words[word][subsequent_word] =  1
                else:
                    all_words[word][subsequent_word] +=  1

    #print(all_words)

    return all_words

    """
    line = f.readline().lower()
    all_words = {} # outer dictionary storing all words in text file
    words = []  # list to store all words in file
    while line:
        # create list of words in line and remove external punctuation
        words_in_line = line.split()
        #print(words_in_line)
        words_in_line = map(_eliminate_external_punc, words_in_line)
        words += words_in_line
        print(words)

        # add words to dictionary
        for index, word in enumerate(words_in_line):
            if (index != len(words_in_line) - 1 and f.readline != ""):
            # If not VERY LAST WORD in file...
                subsequent_word = words_in_line[index + 1]
                if word not in all_words: # adding a new word
                    all_words[word] = {subsequent_word: 1}
                else: # word already in all_words, just need to update inner dict
                    if subsequent_word not in all_words[word]:
                        all_words[word][subsequent_word] =  1
                    else:
                        all_words[word][subsequent_word] +=  1

        print(all_words)
        #output: {"the": {"dog": 1}, "dog":{}}
        line = f.readline().lower()
        """

def _get_words_from_file(f): # Helper function
    line = f.readline().lower()
    words = []  # list to store all words in file
    while line:
        # create list of words in line and remove external punctuation
        words_in_line = line.split()
        #print(words_in_line)
        words_in_line = map(_eliminate_external_punc, words_in_line)
        words.extend(words_in_line)
        line = f.readline().lower()
    return words

def _eliminate_external_punc(word): # Helper function
    return word.strip(string.punctuation)




def unigrams(f):
    '''
    INPUT: file
    OUTPUT: dictionary

    Return a dictionary where the key is an empty tuple and the only value is
    the list of all words in the file, words should appear as many times as
    they occur in the document.

    You should lowercase everything.
    Use strip and string.punctuation to strip the punctuation from the words.

    Example:
    >>> with open('../data/example.txt') as f:
    ...     d = unigrams(f)
    >>> d[()]
    ['the', 'cat', 'chased', 'the', 'dog']
    '''
    word_list = _get_words_from_file(f) # get list of all words in text file
    unigrams_result = {}
    unigrams_result[()] = word_list
    #print(result)
    #print(result[()])

    return unigrams_result



def bigrams(f):
    '''
    INPUT: file
    OUTPUT: dictionary

    Return a dictionary where the keys are tuples of a single word in
    the file and the value for each key is a list of words that were found
    directly following the key.

    You should lowercase everything.
    Use strip and string.punctuation to strip the punctuation from the words.

    Words should be included in the list the number of times they appear.

    Suggestions on how to handle first words: create an entry in the dictionary
    with a first key None.

    Example:
    >>> with open('../data/alice.txt') as f:
    ...     d = bigrams(f)
    >>> d[('among', )]
    ['the', 'those', 'them', 'the', 'the', 'the', 'the', 'the', 'the', 'mad', 'the', 'them']
    '''
    word_counts_dict = word_counts(f)

    bigrams_result = {}

    for word in word_counts_dict:
        subsequent_words_dict = word_counts_dict[word]

        subsequent_words_list = []
        for k, v in subsequent_words_dict.iteritems():
            words_to_add = [k]*v
            subsequent_words_list += words_to_add
        #print("subsequent_words_list",subsequent_words_list)

        bigrams_result[(word,)] = subsequent_words_list

    #print("bigrams_result",bigrams_result)

    return bigrams_result

def trigrams(f):
    '''
    INPUT: file
    OUTPUT: dictionary

    Return a dictionary where the keys are tuples of two consecutive words in
    the file and the value for each key is a list of words that were found
    directly following the key.

    You should lowercase everything.
    Use strip and string.punctuation to strip the punctuation from the words.

    Words should be included in the list the number of times they appear.

    Suggestions on how to handle first words: create an entry in the dictionary
    with a first key (None, None), a second key (None, word1)

    Example:
    >>> with open('../data/alice.txt') as f:
    ...     d = trigrams(f)
    >>> d[('among', 'the')]
    ['people', 'party', 'trees', 'distant', 'leaves', 'trees', 'branches', 'bright']
    '''

    words = _get_words_from_file(f) # get list of all words in text file

    word_counts_result = word_counts(f)

    trigrams_result = {} #outer dict storing all tuples of two consecutive words

    # add words to dictionary
    for i, word in enumerate(words):
        if (i < len(words) - 2):
        # If not VERY LAST TUPLE in file...
            new_tuple = (words[i], words[i + 1])
            subsequent_word = words[i + 2]
            if new_tuple not in trigrams_result: # adding a new tuple
                trigrams_result[new_tuple] = {subsequent_word: 1}
            else: # tuple already in trigrams_result, just update inner dict
                if subsequent_word not in trigrams_result[new_tuple]:
                    trigrams_result[new_tuple][subsequent_word] =  1
                else:
                    trigrams_result[new_tuple][subsequent_word] +=  1

    #print("trigrams_result", trigrams_result)

    return trigrams_result

"""
    for i in range(len(words)):
        if(i != len(words) - 1):
            new_tuple = (words[i], words[i + 1])
        trigrams_result[new_tuple] =

        the boy went to the store.

        [(the, boy), (boy, went), (went, to),(to, the),(the, store)]


"""



def make_random_story(f, n_gram=2, num_words=200):
    '''
    INPUT: file, integer, interger
    OUTPUT: string

    Call n_grams (unigrams, bigrams or trigrams for n_gram set at 1, 2 or 3) on
    file f and use the resulting dictionary to randomly generate text with
    num_words total words.

    Choose the next word by using random.choice to pick a word from the list
    of possibilities given the (n_gram - 1) previous words.

    Use join method to turn a list of words into a string.

    Example:
    >>> # Seed the random number generator for consistent results
    >>> random.seed('Is the looking-glass is half full or half-empty?')
    >>> # Generate a random story
    >>> with open('../data/alice.txt') as f:
    ...     story = make_random_story(f, 2, 10)
    ...     story
    stick, and tumbled head over heels in its sleep 'twinkle,
    >>> len(story.split())  # Verify story length is 10 words
    10
    '''
    if n_gram == 1:
        n_grams = unigrams(f)
    elif n_gram == 2:
        n_grams = bigrams(f)
    else:
        n_grams = trigrams(f)
    story = random.choice(n_grams.keys()) # This gets the start of the story
    print ("first word", story)
    print("n_grams", n_grams)


    #next_word = (random.choice(n_grams[(story[0],)]),)
    #print("next_word", next_word)


    # TODO: fill in the rest of this to make the story

    pass
    if (n_gram == 2):
        for i in range(num_words-1):
            #choose next word(s) of story by choosing randomly from list of
            #possible subsequent words store in the values of the n_grams dict
            possible_subsequent_words = (story[i],)
            if (n_grams.get(possible_subsequent_words) != None):
                next_word = (random.choice(n_grams[possible_subsequent_words],)
            #else:
                #if no possible options for a subsequent chunk,
                # choose a new random tuple






if __name__ == '__main__':
    # open the 'alice.txt' file, in the data directory
    # call the 'make_random_story' to print a 100 word long story based on bigrams
    random.seed('Is the looking-glass is half full or half-empty?')
    with open('../data/alice.txt') as f:
        story = make_random_story(f, 2, 10)
