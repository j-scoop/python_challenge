from pathlib import Path
from PIL import Image


# level url: http://www.pythonchallenge.com/pc/return/5808.html
# Page title: "odd even"
# image url: "cave.jpg"

# Image is kind of blurry/possibly two images superimposed
# Loop over pixels & create two new images - one comprised of
# the pixels at odd indices and the other even

IMAGE_PATH = Path("data/level_11/cave.jpg")
OUTPUT_PATH = Path("data/level_11/output.jpg")


def process_image(img_path):

    print(f"{0 % 2=}")
    print(f"{1 % 2=}")
    print(f"{2 % 2=}")

    with Image.open(img_path) as im:

        # What metadata can we get from the image?
        width, height = im.size

        print(im.format, im.size, im.mode)

        metadata = im.info
        for key, value in metadata.items():
            print(f"{key=}, {value=}")

        pixels = im.load()

        # Create a new blank image with the same size and mode as the input image
        output_image = Image.new(im.mode, (int(width/2), int(height/2)))

        # Load the new image's pixel data
        output_pixels = output_image.load()

        # Loop over pixels and store odd/even separately
        for x in range(width):
            for y in range(height):
                pixel = pixels[x, y]

                # When x is odd and y is even
                if x % 2 and not y % 2:
                    output_pixels[int(x/2), int(y/2)] = pixel
                # OR, when x is even and y is odd
                elif not x % 2 and y % 2:
                    output_pixels[int(x/2), int(y/2)] = pixel
                    # output_pixels[x, y] = pixel
                else:
                    output_pixels[int(x/2), int(y/2)] = pixel


        output_image.save(OUTPUT_PATH)


def main():
    process_image(IMAGE_PATH)


if __name__ == "__main__":
    main()
