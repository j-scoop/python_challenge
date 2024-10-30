from pathlib import Path
from PIL import Image

from utils.helpers import get_image_metadata


# level url: http://www.pythonchallenge.com/pc/def/oxygen.html

# Webpage title: smarty
# Page consists only of image of river with grey pixels in middle
# Let's try get the value of the grey pixels?

IMAGE_PATH = Path("data/level_7/oxygen.png")


def process_image(img_path):
    """
    Process an image and get value of grey pixels
    """

    all_grey_pixels = []
    grey_pixels = []

    with Image.open(img_path) as im:
        width, height = im.size

        # Loop over pixels and find grey ones
        # Only loop over the middle row
        y_middle = height / 2
        for x in range(width):
            r, g, b, a = im.getpixel((x, y_middle))
            if r == g == b:
                all_grey_pixels.append(r)
                # if r not in grey_pixels:
                if (r, g, b, a) != im.getpixel((x + 1, y_middle)):
                    grey_pixels.append(r)

        ouptut_list = [105, 110, 116, 101, 103, 114, 105, 116, 121]

        for num in ouptut_list:
            print(chr(num), end="")


def main():
    get_image_metadata(IMAGE_PATH)

    process_image(IMAGE_PATH)


if __name__ == "__main__":
    main()
