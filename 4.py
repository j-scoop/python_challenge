import re

from info import four_text

in_str = four_text.source
length = len(in_str)

out_str = ''

for i in range(length):
    if in_str[i].isupper():
        if in_str[i+1].isupper():
            if in_str[i+2].isupper():
                if in_str[i+3].islower():
                    if in_str[4] == in_str[i+2]:
                        if in_str[5] == in_str[i+1]:
                            if in_str[6] == in_str[i+0]:
                                out_str += in_str[i+3]

print(out_str)
