#Write a script that removes all of the vowels
#in a user inputted string.
vowels = ['e','a','i','o','u','y','A', 'I', 'E', 'O', 'U', 'Y']
x1 = input("Enter your string: ")
# Method 1:
for i in vowels:
    x1 = x1.replace(i, '')
# Method 2: Probably the most efficient way to do this.
# x1 = ''.join(letter for letter in x1 if letter not in vowels)
print(x1)


# for v in vowels:
#     if v in x1:
#         newstr = x1.remove(v)
# print(newstr)
# for i in range(0,len(x1)):
#     # print(i, x1[i])
#     if x1[i] in vowels:
#         print(i,x1[i])
#         newstr = x1.remove(i)
# print(newstr)

# for i in x1:
#     if i in vowels:
#         newstr = x1.remove(i)
# print(newstr)
