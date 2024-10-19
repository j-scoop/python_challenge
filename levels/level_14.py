from pathlib import Path
from PIL import Image


# Level url: http://www.pythonchallenge.com/pc/return/italy.html
# Level title: "walk around"
# Comment in html: "<!-- remember: 100*100 = (100+99+99+98) + (...  -->"
# wire.png has been formatted to 100x100px, but the actual file
# Is very long and thin: PNG (10000, 1) RGB
# We have to figure out the sequence and apply it to the png?


WIRE_IMG_PATH = Path("data/level_14/wire.png")
OUTPUT_IMG_PATH = Path("data/level_14/output_wire.png")


def process_image(img_path):

    with Image.open(img_path) as im:

        # What metadata can we get from the image?
        width, height = im.size

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

            out_x = x % 100

            if counter < 100:
                output_pixels[out_x, out_y] = pixel
                counter += 1
            else:
                out_y += 1
                counter = 0

        output_image.save(OUTPUT_IMG_PATH)

def main():
    process_image(WIRE_IMG_PATH)


if __name__ == "__main__":
    main()
