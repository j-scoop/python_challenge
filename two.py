from collections import Counter
from data.two_text import source_str


level_url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
out_str = ''

# Try finding the characters that occur least in the source
c = Counter(source_str)

for char, count in c.most_common():
    if count == 1:
        out_str += char

print(f'{out_str=}')
