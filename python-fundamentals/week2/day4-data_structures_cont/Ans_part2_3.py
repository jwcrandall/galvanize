# Write a script that will continually prompt the user for a set of three things
# to be separated by commas. The first two things will be (x, y) coordinates of
#the word that follows (the word will be the third thing).
#So the user will input a string that is formatted like x, y, word.
#Your script will use the string to build a dictionary with the first two inputs
#(i.e. the (x, y)) from each string as keys to a dictionary, and the third input
# (the word) as the value for that key.
#The script will continually prompt the user to input strings in this format
#until the user inputs nothing (i.e. hits enter with no input).

word_dict = {}
while True:
    entry = input('Please enter a coordinate-word pair in the format (x, y, word): ')
    if not entry:
        break
    x, y, word = entry.split(', ') #removes the comma between the values
    word_dict[(x, y)] = word  # Builds a dictionary with (x,y) as keys and word as values

while True:
    lookup = input('Please enter a coordinate to look up: ')
    if lookup == 'q': # exit script if 'q' is entered
        break
    coord = tuple(lookup.split(', ')) # Removes comma and makes coord into a tuple
    if coord not in word_dict:
        print('Coordinate not found')
        continue
print(word_dict[coord])
