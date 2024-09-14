import pickle
from pathlib import Path


# level url: http://www.pythonchallenge.com/pc/def/peak.html

# Hints
# <!-- peak hell sounds familiar ? -->
# Peak hell == pickle?

# Try pickle/unpicke level image
image_path = Path("data/banner.p")


def pickle_image(img_path):

    # unpickled = pickle.load(image_path)
    # unprint(f"{pickled=}")

    answer = 0

    with open(img_path, 'rb') as f:

        unpickled = pickle.load(f, fix_imports=True)
        print(f"{unpickled=}")

        char_num = 0

        for list in unpickled:
            # print(list)
            
            total = 0
            for char, num in list:
                print(char * num, end='')
            print()
                # total += num
                # if char == "#":
                #     char_num += num
            # answer += char_num
            # print(f"{chr(char_num)=}")
            
            # All rows add up to 95
            # if total != 95:
            #     print(f"{list=}")

        # print(f"{answer=}")
        # The answer is not 661
        # The answer is not 5942
        # The answer is not 20278


def main():
    pickle_image(image_path)


if __name__ == "__main__":
    main()
