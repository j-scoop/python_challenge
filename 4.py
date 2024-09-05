import re

from info import four_text

in_str = four_text.source

length = len(in_str)

out_str = ''
# print(in_str)

# for i in range(length):
#     if in_str[i].isupper():
#         if in_str[i+1].isupper():
#             if in_str[i+2].isupper():
#                 if in_str[i+3].islower():
#                     if in_str[4] == in_str[i+2]:
#                         if in_str[5] == in_str[i+1]:
#                             if in_str[6] == in_str[i+0]:
#                                 out_str += in_str[i+3]

# for i in range(length):
#     if in_str[i].isupper():
#         if in_str[i+1] == in_str[i]:
#             if in_str[i+2] == in_str[i]:
#                 if in_str[i+3] == in_str[i]:
#                     if in_str[4] == in_str[i]:
#                         if in_str[5] == in_str[i]:
#                             if in_str[6] == in_str[i]:
#                                 out_str += in_str[i+3]

# checking upper x 3, lower x 1, upper x 3 = too many results
# for i in range(length):
#     if in_str[i].isupper():
#         if in_str[i+1].isupper():
#             if in_str[i+2].isupper():
#                 if in_str[i+3].islower():
#                     if in_str[i+4].isupper():
#                         if in_str[i+5].isupper():
#                             if in_str[i+6].isupper():
#                                 print(in_str[i:i+7])
#                                 out_str += in_str[i+3]

# Check identical uppers = no results
# for i in range(length):
#     if in_str[i].isupper():
#         if in_str[i+1] == in_str[i]:
#             if in_str[i+2] == in_str[i]:
#                 if in_str[i+3].islower():
#                     if in_str[i+4] == in_str[i]:
#                         if in_str[i+5] == in_str[i]:
#                             if in_str[i+6] == in_str[i]:
#                                 print(in_str[i:i+7])
#                                 out_str += in_str[i+3]

# Check symmetry uppers = gets to end of list
# for i in range(length):
#     if in_str[i].isupper() and in_str[i] == in_str[i+6]:
#         if in_str[i+1] == in_str[i+5]:
#             if in_str[i+2] == in_str[i+4]:
#                 if in_str[i+3].islower():
#                     print(in_str[i:i+7])
#                     out_str += in_str[i+3]

# 

# pattern = r'(?<=[A-Z])\1{2}([a-z])(?<=\1{3})'
# matches = re.findall(pattern, in_str)

# print(matches)

# Convert input string into list separated at newlines
in_list = in_str.splitlines()
num_lists = len(in_list)
# Assume lists are same length
list_length = len(in_list[1])

print(f"{list_length=}")

pos = 0
# Loop over list and search for pattern
# for string_num, current_string in enumerate(in_list):
#     # We should skip the first few rows as no rows above, also blank line at beginning
#     # print(f"{string_num}: {list}")
#     # print(f"{string_num=}")
#     if string_num < 4:
#         continue
#     for i in range(list_length):
#         # Stop when we get to the end of the string
#         if i + 7 >= list_length:
#             continue
#         if current_string[i].isupper():
#             if current_string[i+1].isupper():
#                 if current_string[i+2].isupper():
#                     if current_string[i+3].islower():
#                         if current_string[i+4].isupper():
#                             if current_string[i+5].isupper():
#                                 if current_string[i+6].isupper():
#                                     # Check for vertical bodyguards
#                                     if in_list[string_num-1][i+3].isupper():
#                                         if in_list[string_num-2][i+3].isupper():
#                                             if in_list[string_num-3][i+3].isupper():
#                                                 if in_list[string_num+1][i+3].isupper():
#                                                     if in_list[string_num+2][i+3].isupper():
#                                                         if in_list[string_num+3][i+3].isupper():
#                                                             print(f"Coordinates: {string_num=}, char: {i+3} = {current_string[i+3]}")
#                                                             print(f"{current_string[i+3]}")
#                                                             out_str += current_string[i+3]

for string_num, current_string in enumerate(in_list):
    # We should skip the first few rows as no rows above, also blank line at beginning
    print(f"{string_num}: {list}")
    print(f"{string_num=}")
    if string_num < 4:
        continue
    for i in range(list_length):
        # Stop when we get to the end of the string
        if i + 7 >= list_length:
            continue
        if current_string[i].isupper():
            if current_string[i+1].isupper():
                if current_string[i+2].isupper():

                    if current_string[i+3].islower():

                        if current_string[i+4].isupper():
                            if current_string[i+5].isupper():
                                if current_string[i+6].isupper():

                                    if current_string[i+-1].islower():
                                        if current_string[i+7].islower():
                                            print(f"{current_string[i+3]}")
                                            out_str += current_string[i+3]

# Maybe it should ONLY have 3 characters on each side?

# Check rows above and below for pattern in vertical format

print(out_str)
