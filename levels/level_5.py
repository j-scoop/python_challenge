import pickle
from pathlib import Path


# level url: http://www.pythonchallenge.com/pc/def/peak.html

# Hints
# <!-- peak hell sounds familiar ? -->
# Peak hell == pickle?

# Try pickle/unpicke level image
image_path = Path("data/level_5/banner.p")


def pickle_image(img_path):

    with open(img_path, "rb") as f:

        unpickled = pickle.load(f, fix_imports=True)
        # print(f"{unpickled=}")

        for list in unpickled:
            for char, num in list:
                print(char * num, end="")
            print()


def main():
    pickle_image(image_path)


if __name__ == "__main__":
    main()
