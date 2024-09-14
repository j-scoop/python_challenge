from pathlib import Path
import re
import sys


# level url: www.pythonchallenge.com/pc/def/channel.zip
# Hints
# From data/channel/readme.txt: 
# hint1: start from 90052
# hint2: answer is inside the zip

file_key = 90052


def traverse_files(file_key):

    # Search for digits at end of string
    pattern = r"\d+$"

    filepath = Path(f"data/level_6/channel/{file_key}.txt")

    with open(filepath, "r") as f:
        for line in f:
            m = re.search(pattern, line)
            if m:
                print(line)
                file_key = m.group(0)
                filepath = Path(f"data/level_6/channel/{file_key}.txt")
            else:
                print(f"Failed to find the next key. Page text: {line}")


def main():
    traverse_files(file_key)


if __name__ == "__main__":
    main()
