# Write a script that prompts the user for a state name.
search_state = input("Please enter a state name: ")
search_state = search_state.lower()
#It will then check that state name against the dictionary below to give back the capital of that state.
# However, you'll notice that the dictionary doesn't know the capitals for all the states.
# If the user inputs the name of a state that isn't in the dictionary, your script should
# print that the capital is unknown.

state_dictionary = {'Colorado': 'Denver', 'Alaska': 'Juneau', 'California': 'Sacramento',
                       'Georgia': 'Atlanta', 'Kansas': 'Topeka', 'Nebraska': 'Lincoln',
                       'Oregon': 'Salem', 'Texas': 'Austin', 'New York': 'Albany'}

if search_state in state_dictionary:
    print(state_dictionary[search_state])
else:
    print('{} capital unknown.'.format(search_state))
