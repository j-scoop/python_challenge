from pathlib import Path
import re
import sys
import os
import zipfile


# level url: www.pythonchallenge.com/pc/def/channel.html
# Dowload zip file at www.pythonchallenge.com/pc/def/channel.zip
# Hints
# From data/channel/readme.txt:
# hint1: start from 90052
# hint2: answer is inside the zip

# Loop stops at 46145.txt text below:
# Collect the comments.

INITIAL_FILE_KEY = 90052


def search_files(directory):
    """
    Search text files in a directory and print if does not match the pattern
    """
    pattern = r"\d+$"
    for file in os.listdir(directory):
        with open(os.path.join(directory, file), "r") as f:
            for line in f:
                m = re.search(pattern, line)
                if not m:
                    print(f"{line}")


def get_zip_comment(zip_file_path):
    """
    Loop over all files in a .zip file and get their comments
    """

    file_comments = {}

    zip_file = zipfile.ZipFile(zip_file_path)
    infolist = zip_file.infolist()
    for info in infolist:
        file_key = info.filename[:-4]
        file_comments[file_key] = str(info.comment, "utf-8")

    return file_comments


def traverse_files(file_key, file_comments):
    """
    Traverse the files which match the pattern in a directory and return the
    comments associated with each as a single string
    """

    # Search for digits at end of string
    pattern = r"\d+$"

    filepath = Path(f"data/level_6/channel/{file_key}.txt")

    output = ""

    while True:
        with open(filepath, "r") as f:
            for line in f:
                m = re.search(pattern, line)
                if m:
                    # print(line)
                    file_key = m.group(0)
                    filepath = Path(f"data/level_6/channel/{file_key}.txt")

                    output += file_comments[file_key]

                else:
                    print(f"Failed to find the next key. Page text: {line}")
                    return output


def main():
    path = Path("data/level_6/channel.zip")

    file_comments = get_zip_comment(path)
    answer = traverse_files(INITIAL_FILE_KEY, file_comments)
    print(answer)


if __name__ == "__main__":
    main()
