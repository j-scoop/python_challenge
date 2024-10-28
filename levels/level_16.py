from pathlib import Path
from PIL import Image


# level url: http://www.pythonchallenge.com/pcc/return/mozart.html
# Level title: "let me get this straight"
# Hint: Doesn't seem to be a hint.

# Image is a TV static looking picture with some pink marks on
# It is a gif

# What do we have to straighten out?

# What does Mozart have to do with it? Do we have to 'compose' something?

# Ideas:
# We have to compose functions to call each other
# We have to create a moving gif from the static gif

IMAGE_PATH = Path("data/level_16/mozart.gif")


def get_image_metadata(img_path):

    with Image.open(img_path) as im:

        # What metadata can we get from the image?
        width, height = im.size

        print(f'{width=}, {height=}')

        print(f"{im.format=}, {im.size=}, {im.mode=}")

        metadata = im.info
        for key, value in metadata.items():
            print(f"{key=}, {value=}")


def main():
    get_image_metadata(IMAGE_PATH)


if __name__ == "__main__":
    main()
