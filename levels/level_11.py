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
OUTPUT_PATH_2 = Path("data/level_11/output_2.jpg")


def is_even(num: int):
    if num % 2:
        return False
    else:
        return True


def process_image(img_path):

    with Image.open(img_path) as im:

        # What metadata can we get from the image?
        width, height = im.size

        print(im.format, im.size, im.mode)

        metadata = im.info
        for key, value in metadata.items():
            print(f"{key=}, {value=}")

        pixels = im.load()

        # Create a new blank image with the same size and mode as the input image
        output_image = Image.new(im.mode, (int(width / 2), int(height / 2)))
        # Load the new image's pixel data
        output_pixels = output_image.load()

        # Create a new blank image with the same size and mode as the input image
        output_image_2 = Image.new(im.mode, (int(width / 2), int(height / 2)))
        # Load the new image's pixel data
        output_pixels_2 = output_image_2.load()

        # Loop over pixels and store odd/even separately
        for x in range(width):
            for y in range(height):
                pixel = pixels[x, y]

                if not is_even(x) and not is_even(y):
                    output_pixels[int(x / 2), int(y / 2)] = pixel
                elif is_even(x) and is_even(y):
                    output_pixels[int(x / 2), int(y / 2)] = pixel
                else:
                    output_pixels_2[int(x / 2), int(y / 2)] = pixel

        output_image.save(OUTPUT_PATH)
        output_image_2.save(OUTPUT_PATH_2)


def main():
    process_image(IMAGE_PATH)


if __name__ == "__main__":
    main()
