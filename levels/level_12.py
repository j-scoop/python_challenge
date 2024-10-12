from pathlib import Path
from PIL import Image


# level url: http://www.pythonchallenge.com/pc/return/evil.html
# Page title: "dealing evil"
# image url: "evil1.jpg" - is there an evil2.jpg? Yes
# evil2.jpg has text "not jpg - _.gfx", let's see if we can download evil2.gfx

# Can we parse the metadata of the evil2.jpg to get a hint?

INPUT_FILE = Path("data/level_12/evil2.jpg")


def process_image(img_path):

    with Image.open(img_path) as im:

        # What metadata can we get from the image?
        width, height = im.size

        print(im.format, im.size, im.mode)

        metadata = im.info
        for key, value in metadata.items():
            print(f"{key=}, {value=}")


def main():
    process_image(INPUT_FILE)


if __name__ == "__main__":
    main()
