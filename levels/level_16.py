from pathlib import Path
from PIL import Image

from utils.helpers import get_image_metadata


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
# It looks like there is only one line of pink pixels per row
# Do we have to adjust each row horizontally so they display in a vertical line?

IMAGE_PATH = Path("data/level_16/mozart.gif")
OUTPUT_PATH = Path("data/level_16/output/output.gif")


def get_adjusted_coordinate(x_coord, offset, limit):
    return (x_coord - offset) % limit


def straighten_pixels(img_path):

    with Image.open(img_path) as im:

        # Issue with image when in P mode
        if im.mode == "P":
            im = im.convert("RGB")

        width, height = im.size

        pixels = im.load()

        # Create a new blank image with the same size and mode as the input
        output_image = Image.new(im.mode, (width, height))
        output_pixels = output_image.load()

        offset_values = {}

        # For each row of pixels, get the offset of the pink pixels from 0 position
        for y in range(height):
            for x in range(width):
                pixel = pixels[x, y]

                if pixels[x, y] == (255, 0, 255):
                    current_offset = -x
                    offset_values[y] = current_offset

                output_pixels[x, y] = pixel

            if offset_values.get(y) is None:
                offset_values[y] = 0

        # For each row of pixels, write according to the offset
        for y in range(height):
            for x in range(width):

                current_offset = get_adjusted_coordinate(x, offset_values[y], width)
                output_pixels[x, y] = im.getpixel((current_offset, y))

        output_image.save(OUTPUT_PATH)


def main():
    get_image_metadata(IMAGE_PATH)

    straighten_pixels(IMAGE_PATH)


if __name__ == "__main__":
    main()
