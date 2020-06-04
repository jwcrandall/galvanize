# Write a script that makes every other letter of a user inputted
# string capitalized.
x1 = input("Enter your string: ")
# for i in x1[1::2]:
#     print(x1)
#     x2 = x1.append(x1.upper())
# print(x2)

# One way to do this.
empty_lst = []
for idx, char in enumerate(x1):
    if idx % 2 != 0:
        empty_lst.append(char.upper())
    else:
        empty_lst.append(char.lower())

output_str = ''.join(empty_lst)
print(output_str)


# # One way to do this.
# empty_lst = []
# for idx, char in enumerate(x1):
#     if idx % 2 != 0:
#         empty_lst.append(char.upper())
#     else:
#         empty_lst.append(char.lower())
#
# output_str = ''.join(empty_lst)
#
# # A comprehension way to do this.
# output_str = ''.join(char.upper() if idx % 2 != 0 else char.lower()
# for idx, char in enumerate(x1))
