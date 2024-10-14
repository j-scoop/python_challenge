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

# INPUT_FILE = Path("data/level_12/evil1.jpg")
INPUT_FILE = Path("data/level_12/bert.gif")
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


def process_image(img_path):

    with Image.open(img_path) as im:

        # What metadata can we get from the image?
        width, height = im.size

        print(im.format, im.size, im.mode)

        metadata = im.info
        for key, value in metadata.items():
            print(f"{key=}, {value=}")

        exif_data = im.getexif()
        print(f"{exif_data=}")

        if exif_data:
            print("There is exif data")
            for key, item in exif_data.items():
                print(f"{key}: {item}")
        else:
            print("There is no exif data")


def main():

    # download_image(EVIL_4_IMAGE_URL, Path("data/level_12/evil4.jpg"))

    process_image(INPUT_FILE)


if __name__ == "__main__":
    main()
