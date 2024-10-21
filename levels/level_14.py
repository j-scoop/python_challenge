from pathlib import Path
from PIL import Image


# Level url: http://www.pythonchallenge.com/pc/return/italy.html
# Level title: "walk around"
# The level image is a spiraling pastry
# Comment in html: "<!-- remember: 100*100 = (100+99+99+98) + (...  -->"
# wire.png has been formatted to 100x100px, but the actual file
# Is very long and thin: PNG (10000, 1) RGB
# We have to figure out the sequence and apply it to the png?

# When creating a 100x100 image from the wire.png, output img says "bit"
# bit.html says "you took the wrong curve."

# Let's try spiraling the pixels from the centre, or towards the centre

WIRE_IMG_PATH = Path("data/level_14/input/wire.png")
OUTPUT_IMG_PATH = Path("data/level_14/output/output_wire.png")


def process_image(img_path):
    """
    This function doesn't solve the level, but it does output an image with a hint
    """

    with Image.open(img_path) as im:

        # What metadata can we get from the image?
        width, height = im.size

        print(f"{width=}, {height=}")
        print(im.format, im.size, im.mode)

        metadata = im.info
        for key, value in metadata.items():
            print(f"{key=}, {value=}")

        pixels = im.load()

        # First lets try and split the wire image into a standard 100x100 png

        output_image = Image.new(im.mode, (100, 100))
        # Load the new image's pixel data
        output_pixels = output_image.load()

        counter = 0
        out_y = 0
        for x in range(width):
            pixel = pixels[x, 0]
            out_x = x % 99

            if counter < 99:
                output_pixels[out_x, out_y] = pixel
                counter += 1
            else:
                out_y += 1
                counter = 0

        output_image.save(OUTPUT_IMG_PATH)


def uzumaki(img_path):
    """
    This function sovles the level. Praise the spiral.
    """

    with Image.open(img_path) as im:
        # What metadata can we get from the image?
        width, height = im.size

        print(im.format, im.size, im.mode)

        pixels = im.load()

        output_image = Image.new(im.mode, (100, 100))
        output_pixels = output_image.load()

        out_x = 0
        out_y = 0

        direction = "right"

        # As we spiral round, we'll need to limit the length of the line being written
        limits = {
            "upper": 1,
            "lower": 99,
            "left": 0,
            "right": 99
        }

        # When we change direction, we aren't starting from 0 on the new axis

        for x in range(width):
            pixel = pixels[x, 0]
            # Write each line by spiralling round the output image clockwise

            if direction == "right":
                print(f"{limits['right']=}")
                if out_x < limits["right"]:
                    output_pixels[out_x, out_y] = pixel
                    out_x += 1
                else:
                    print(f"{out_x=}")
                    # We've reached the end, write the pixel,
                    # decrease the right limit & change direction
                    output_pixels[out_x, out_y] = pixel
                    limits["right"] -= 1
                    print(f"{limits['right']=}")
                    direction = "down"
                    # We are finished with the row, so increment y
                    out_y += 1

            elif direction == "down":
                if out_y < limits["lower"]:
                    output_pixels[out_x, out_y] = pixel
                    out_y += 1
                else:
                    # We've reached the end, write the pixel,
                    # decrease the right limit & change direction
                    output_pixels[out_x, out_y] = pixel
                    limits["lower"] -= 1
                    direction = "left"
                    # Finished with this row, de-increment x
                    out_x -= 1

            elif direction == "left":
                if out_x > limits["left"]:
                    output_pixels[out_x, out_y] = pixel
                    out_x -= 1
                else:
                    # When we've reached the end, write the pixel and change direction
                    output_pixels[out_x, out_y] = pixel
                    limits["left"] += 1
                    direction = "up"
                    # Finished with this row, deincrement y
                    out_y -= 1

            else:
                if out_y > limits["upper"]:
                    output_pixels[out_x, out_y] = pixel
                    out_y -= 1
                else:
                    # When we've reached the end, write the pixel and change direction
                    output_pixels[out_x, out_y] = pixel
                    limits["upper"] += 1
                    direction = "right"
                    # Finished with this row, increment x
                    out_x += 1

        output_image.save(OUTPUT_IMG_PATH)


def main():
    # process_image(WIRE_IMG_PATH)

    uzumaki(WIRE_IMG_PATH)


if __name__ == "__main__":
    main()
