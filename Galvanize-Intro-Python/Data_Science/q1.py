import re
from collections import defaultdict
"""
Write a Python program that analyzes input from a file and compiles statistics on it.

The program should output:

1. The total word count

2. The count of unique words

3. The number of sentences

"""
user_str = input('Please input a string: ').lower()

# Counts Number of Words
tmp = defaultdict(int)
for n_word in user_str.split():
    tmp[n_word] += 1
       
#Counts number of unique words
distinct_word = tmp.items()

# number of sentences in string
n_sentences = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].*)',user_str)

#Output
print ('1. Total Word Count:', len(user_str.split()))  
print ('2. Numeber of Distinct Words:', len(distinct_word))
print ('3. Number of Sentences:', len(n_sentences))

"""
Brownie points will be awarded for the following extras:

1. The ability to calculate the average sentence length in words

2. The ability to find often used phrases (a phrase of 3 or more words used over 3 times)

3. A list of words used, in order of descending frequency

4. The ability to accept input from STDIN, or from a file specified on the command line.
"""

print ('E1. Average Sentence Length (in words)', float(len(user_str.split())/len(n_sentences)), '\n')

s =sorted(tmp.items(),key=lambda item: item[1])
print ('\n',"E2. List of Words in Descending Frequency:",'\n')
for i, (words, count) in enumerate(s):
    print (words, count)
    