import sys
import urllib
from pathlib import Path
import requests
from urllib import request
import re

from utils.helpers import get_image_metadata, check_cookies, decode_bz2
from levels.level_13 import xmlrpc_phone_method


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

# Collecting the cookies of the busynothings to a bytes string and decoding results in:
# "is it the 26th already? call his father and inform him that "the flowers are on their way". he\'ll understand.'"

# How do we call his father? Perhaps using level 13 phone thingy?
# Call father ("Leopold") = success, outputs "555-VIOLIN"
# Via violin.html we get redirected to http://www.pythonchallenge.com/pc/stuff/violin.php
# Contains image of Mozart's father & title: "it's me. what do you want?"

MOZART_FATHER = "Leopold"
XML_URL = "http://www.pythonchallenge.com/pc/phonebook.php"
LEOPOLD_URL = "http://www.pythonchallenge.com/pc/stuff/violin.php"

LEVEL_IMAGE = Path("data/level_17/input/cookies.jpg")
LEVEL_URL = "http://www.pythonchallenge.com/pc/return/romance.html"
USERNAME = "huge"
PASSWORD = "file"


def traverse_url(url_key: str, num_items: int):
    cookies_bytes = b""
    visited_urls = []
    for i in range(num_items):
        url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={url_key}"
        print(f"{url=}")

        # Search for digits at end of string
        re_pattern = r"\d+$"

        info_cookie = check_cookies(url)
        cookies_bytes += info_cookie.encode()
        print(f"{cookies_bytes=}")

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
                return cookies_bytes


def main():
    get_image_metadata(LEVEL_IMAGE)

    # Traverser the urls and get the text from each page's cookies
    cookie_bytes = traverse_url("12345", 400)
    print(f"{cookie_bytes=}")

    # Decode the text from the cookies
    decoded_string = urllib.parse.unquote_to_bytes(cookie_bytes)
    print(f"{decoded_string=}")

    output = decode_bz2(decoded_string)
    print(f"{output=}")

    # Get Mozart's father's 'phone number'
    xmlrpc_phone_method(XML_URL, MOZART_FATHER)

    # Use the 'phone number' (url) to give Mozart's father the message
    cookies = {"info": "the flowers are on their way"}
    response = requests.get(LEOPOLD_URL, cookies=cookies)
    print(response.text)


if __name__ == "__main__":
    main()
