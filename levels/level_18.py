from pathlib import Path
from utils.helpers import get_image_metadata
from PIL import Image


# Level url: http://www.pythonchallenge.com/pc/return/balloons.html
# Level title: "can you tell the difference?"
# Comment: "<!-- it is more obvious that what you might think -->"
# Typo? that/than?

# Image is two of the same image (two swans) side by side, with the one on the
# right being darker than the left.

# Let's compare the pixels for each side and see how they differ.

LEVEL_IMAGE = Path("data/level_18/input/balloons.jpg")


def compare_split_image(img_path):
    # First, split the image on the x axis
    metadata = get_image_metadata(LEVEL_IMAGE)
    width, height = metadata["size"]

    img_2_index = width // 2

    with Image.open(img_path) as im:

        pixels = im.load()

        # Loop over the pixels for each half
        for x in range(img_2_index):
            for y in range(height):
                img_1_pixel = pixels[x, y]
                img_2_pixel = pixels[x + img_2_index, y]

                print(f"{img_1_pixel=}")
                print(f"{img_2_pixel=}")

                diff_r, diff_g, diff_b = img_2_pixel - img_1_pixel
                print(f"{diff_r=}")
                print(f"{diff_g=}")
                print(f"{diff_b=}")

    # Get the difference between each pixel


def main():
    compare_split_image(LEVEL_IMAGE)


if __name__ == "__main__":
    main()