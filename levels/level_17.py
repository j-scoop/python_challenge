import sys
from pathlib import Path
import requests
from urllib import request
import re
from utils.helpers import get_image_metadata


# Level url: http://www.pythonchallenge.com/pc/return/romance.html
# Level title: "eat?"

# Image is a photo of some choc chip cookies with a small photo of
# some wooden men with a saw, cutting a log in the left corner
# The saw men image is from level 4! 
# Level 4 cookies state using 'busynothing' - let's try level 4
# solution with 'busynothing' in place of 'nothing'

# Ideas:
# Check/make use of website cookies
# Cookie cutter

LEVEL_IMAGE = Path("data/level_17/input/cookies.jpg")
LEVEL_URL = "http://www.pythonchallenge.com/pc/return/romance.html"
USERNAME = "huge"
PASSWORD = "file"


def check_cookies(url):
    response = requests.get(url, auth=(USERNAME, PASSWORD))

    cookies = response.cookies
    print(f"{cookies=}")
    for cookie in cookies:
        print(cookie.name, cookie.value)


def traverse_url(url_key: str, num_items: int):
    visited_urls = []
    for i in range(num_items):
        url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={url_key}"
        print(f"{url=}")

        # Search for digits at end of string
        re_pattern = r"\d+$"

        with request.urlopen(url) as page:
            visited_urls.append(url_key)

            page_text = page.read(300).decode("utf-8")

            m = re.search(re_pattern, page_text)
            if m:
                url_key = m.group(0)
                if url_key in visited_urls:
                    print(f"We've already visited this key. Page body: {page_text}")
                    sys.exit()
            else:
                print(f"Failed to find the next key. Page body: {page_text}")
                sys.exit()


def main():
    get_image_metadata(LEVEL_IMAGE)

    # Seem to be no cookies for this level
    check_cookies("http://www.pythonchallenge.com/pc/def/linkedlist.php")

    # traverse_url("12345", 400)

    # url='http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=83051'
    # Failed to find the next key. Page body: that's it.

    # Cookie of 83051: 

    # The 'busynothings' seem to have cookies.
    # Cookie title: 90
    # Cookie title: h

    # Maybe I have to read the cookies rather than the html body to get the next nothing?!

    # Try inputting these into the busynothing

    # traverse_url("90", 400)

    traverse_url("h", 400)


if __name__ == "__main__":
    main()
