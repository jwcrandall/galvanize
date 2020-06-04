#Given the list [0, 3, 6, 9, 10, 2, 5] and [2, 6, 4, 7, 8, 1, 15],
# write a script that finds the common elements between them.
# Store them in a list, and print that list, sorted, as the final output
#(if you'd like you can go ahead and hard code those lists in your
#script).

lst1 = [0, 3, 6, 9, 10, 2, 5]
lst2 = [2, 6, 4, 7, 8, 1, 15]

# Way to do this with a for loop.
common_elements = []
for element in lst1:
    if element in lst2:
        common_elements.append(element)

# Using a list comp for this.
common_elements = [element for element in lst1 if element in lst2]
common_elements.sort()
print(common_elements)
