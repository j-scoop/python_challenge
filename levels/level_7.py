from pathlib import Path
from PIL import Image

# level url: http://www.pythonchallenge.com/pc/def/oxygen.html

# Webpage title: smarty
# Page consists only of image of river with grey pixels in middle
# Let's try get the value of the grey pixels?

IMAGE_PATH = Path("data/level_7/oxygen.png")

def process_image(img_path):
    """
    Process an image and get value of grey pixels
    """   

    grey_pixels = []

    with Image.open(img_path) as im:
        # What metadata can we get from the image?

        width, height = im.size

        print(im.format, im.size, im.mode)

        metadata = im.info
        for key, value in metadata.items():
            print(f"{key=}, {value=}")

        # Loop over pixels and find grey ones
        # Only loop over the middle row
        y_middle = height / 2
        for x in range(width):
            # for y in range(height):
            r, g, b, a = im.getpixel((x, y_middle))
            if r == g == b:
                # print(r, g, b, a)          
                # if r not in grey_pixels:
                if (r, g, b, a) != im.getpixel((x+1, y_middle)):
                    grey_pixels.append(r)
               
        print(f"{grey_pixels=}")

        # convert to unicode chars
        for pixel in grey_pixels:
            print(chr(pixel), end="")


def main():
    process_image(IMAGE_PATH)


if __name__ == "__main__":
    main()
