from PIL import Image, ExifTags


def get_image_metadata(image_path):
    metadata = {}

    with Image.open(image_path) as img:
        # Basic metadata
        metadata["format"] = img.format
        metadata["mode"] = img.mode
        metadata["size"] = img.size  # (width, height)

        # Extract EXIF data (JPEG and some TIFFs)
        if img.format == "JPEG" or img.format == "TIFF":
            exif_data = img._getexif()
            if exif_data:
                exif = {}
                for tag, value in exif_data.items():
                    decoded_tag = ExifTags.TAGS.get(tag, tag)
                    exif[decoded_tag] = value
                metadata["exif"] = exif

        # Extract PNG text and color info
        if img.format == "PNG":
            png_info = img.info
            metadata["gamma"] = png_info.get("gamma")
            metadata["icc_profile"] = png_info.get("icc_profile")
            metadata["text"] = png_info.get("text")  # Embedded text fields

        # Extract GIF frame data
        if img.format == "GIF":
            metadata["n_frames"] = img.n_frames
            gif_info = img.info
            metadata["background"] = gif_info.get("background")
            metadata["loop"] = gif_info.get("loop")  # Loop count
            metadata["duration"] = gif_info.get("duration")  # Frame duration (ms)

    for key, value in metadata.items():
        print(f"{key}: {value}")

    return metadata
