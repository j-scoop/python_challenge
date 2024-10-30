from PIL import Image


def get_image_metadata(img_path):

    with Image.open(img_path) as im:

        # What metadata can we get from the image?
        width, height = im.size

        print(f"{width=}, {height=}")

        print(f"{im.format=}, {im.size=}, {im.mode=}")

        print(f"{im.n_frames=}")

        metadata = im.info
        for key, value in metadata.items():
            print(f"{key=}, {value=}")
