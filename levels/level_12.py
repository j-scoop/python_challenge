from pathlib import Path
from PIL import Image
import requests


# level url: http://www.pythonchallenge.com/pc/return/evil.html
# Page title: "dealing evil"
# image url: "evil1.jpg" - is there an evil2.jpg? Yes
# evil2.jpg has text "not jpg - _.gfx", let's see if we can download evil2.gfx

# Can we parse the metadata of the evil2.jpg to get a hint?

# Downloading evil4.jpg and looking inside at the binary data, it reads "Bert is evil! go back!"
# http://www.pythonchallenge.com/pc/return/bert.html has picture of Bert from Bert and Ernie

# Evil1-3 are all same size jpgs. Maybe create new image(s) with a pixel from each?

IMAGE_PATH_1 = Path("data/level_12/evil1.jpg")
IMAGE_PATH_2 = Path("data/level_12/evil2.jpg")
IMAGE_PATH_3 = Path("data/level_12/evil3.jpg")
IMAGE_PATH_4 = Path("data/level_12/bert.gif")
GFX_PATH = Path("data/level_12/evil2.gfx")

OUTPUT_PATH_1 = Path("data/output_1.jpg")
OUTPUT_PATH_2 = Path("data/output_2.jpg")
OUTPUT_PATH_3 = Path("data/output_3.jpg")

EVIL_4_IMAGE_URL = "http://www.pythonchallenge.com/pc/return/evil4.jpg"


def download_image(url, save_path):
    username = "huge"
    password = "file"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"Image downloaded and saved as {save_path}")

    else:
        print(f"Failed to download image. Status code: {response.status_code}")


def parse_gfx(gfx_path):
    with open(gfx_path, "rb") as f:
        # Level image is someone dealing 5 sets of cards - lets try 'dealing' the bytes into 5 'piles'
        data = f.read()
        print(f"{len(data)=}")
        # for line in f:
        #     print(line)

        print(f"{data=}")
        print(f"{data[0]}")

        of1 = open(Path("data/level_12/output_1.jpg"), "wb")
        of2 = open(Path("data/level_12/output_2.jpg"), "wb")
        of3 = open(Path("data/level_12/output_3.jpg"), "wb")
        of4 = open(Path("data/level_12/output_4.jpg"), "wb")
        of5 = open(Path("data/level_12/output_5.jpg"), "wb")

        counter = 0
        for i in range(len(data)):
            if counter == 0:
                of1.write(bytes([data[i]]))
            elif counter == 1:
                of2.write(bytes([data[i]]))
            elif counter == 2:
                of3.write(bytes([data[i]]))
            elif counter == 3:
                of4.write(bytes([data[i]]))
            else:
                of5.write(bytes([data[i]]))

            counter += 1
            if counter == 5:
                counter = 0

        # for key, value in cards.items():
        #     output_file = Path(f"data/level_12/output_{key}.jpg")
        #     with open(output_file, "wb") as of:
        #         of.write(value)

        of1.close()
        of2.close()
        of3.close()
        of4.close()
        of5.close()


def process_image(img_path1, img_path2, img_path3):

    with Image.open(img_path1) as im1:

        with Image.open(img_path2) as im2:

            with Image.open(img_path3) as im3:

                pixels_1 = im1.load()
                pixels_2 = im2.load()
                pixels_3 = im3.load()

                # What metadata can we get from the image?
                width, height = im1.size
                print(im1.format, im1.size, im1.mode)

                output_image_1 = Image.new(im1.mode, (width, height))
                output_pixels_1 = output_image_1.load()

                output_image_2 = Image.new(im1.mode, (width, height))
                output_pixels_2 = output_image_2.load()

                output_image_3 = Image.new(im1.mode, (width, height))
                output_pixels_3 = output_image_3.load()

                metadata = im1.info
                for key, value in metadata.items():
                    print(f"{key=}, {value=}")

                exif_data = im1.getexif()
                # print(f"{exif_data=}")

                if exif_data:
                    print("There is exif data")
                    for key, item in exif_data.items():
                        print(f"{key}: {item}")
                else:
                    print("There is no exif data")

                # Loop over pixels and write to output
                counter = 0
                for y in range(height):
                    for x in range(width):
                        pixel_1 = pixels_1[x, y]
                        pixel_2 = pixels_2[x, y]
                        pixel_3 = pixels_3[x, y]
                        # Get every 3rd pixel
                        if counter == 0:
                            output_pixels_1[x, y] = pixel_1
                            output_pixels_2[x, y] = pixel_2
                            output_pixels_3[x, y] = pixel_3
                        elif counter == 1:
                            output_pixels_1[x, y] = pixel_2
                            output_pixels_2[x, y] = pixel_3
                            output_pixels_3[x, y] = pixel_1
                        else:
                            output_pixels_1[x, y] = pixel_3
                            output_pixels_2[x, y] = pixel_1
                            output_pixels_3[x, y] = pixel_2
                        counter += 1
                        if counter == 3:
                            counter = 0

                output_image_1.save(OUTPUT_PATH_1)
                output_image_2.save(OUTPUT_PATH_2)
                output_image_3.save(OUTPUT_PATH_3)


def main():

    # download_image(EVIL_4_IMAGE_URL, Path("data/level_12/evil4.jpg"))

    # process_image(IMAGE_PATH_1, IMAGE_PATH_2, IMAGE_PATH_3)

    parse_gfx(GFX_PATH)


if __name__ == "__main__":
    main()
