from collections import Counter
from data.level_2_text import source_str


# level url: http://www.pythonchallenge.com/pc/def/ocr.html


# Try finding the characters that occur least in the source
def find_rare_chars():
    out_str = ""

    counted = Counter(source_str)

    for char, count in counted.most_common():
        if count == 1:
            out_str += char

    return out_str


def main():
    print(find_rare_chars())


if __name__ == "__main__":
    main()
