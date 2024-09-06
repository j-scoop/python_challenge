import re
from data.three_text import source as in_str


length = len(in_str)
out_str = ''

# Initial attempt using for loops
# Convert input string into list separated at newlines
in_list = in_str.splitlines()

# Assume lists are same length
list_length = len(in_list[1])
print(f"{list_length=}")

for string_num, current_string in enumerate(in_list):
    # Skip blank line
    if string_num == 0:
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

                                    # Does it have to have lowercase either side?
                                    if current_string[i+-1].islower():
                                        if current_string[i+7].islower():
                                            out_str += current_string[i+3]

print(f'{out_str=}')

# Attempt using regex
pattern = r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]'
middle_letters = re.findall(pattern, in_str)

out_str_regex = ''.join(middle_letters)

print(f'{out_str_regex=}')
