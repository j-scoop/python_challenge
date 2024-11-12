import sys
import bz2
import urllib
from pathlib import Path
import requests
from urllib import request
import re

from utils.helpers import get_image_metadata
from levels.level_13 import parse_xml


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
LEOPOLD_URL  = "http://www.pythonchallenge.com/pc/stuff/violin.php"

LEVEL_IMAGE = Path("data/level_17/input/cookies.jpg")
LEVEL_URL = "http://www.pythonchallenge.com/pc/return/romance.html"
USERNAME = "huge"
PASSWORD = "file"

ENCODED_STRING = b'BZh91AY%26SY%94%3A%E2I%00%00%21%19%80P%81%11%00%AFg%9E%A0%20%00hE%3DM%B5%23%D0%D4%D1%E2%8D%06%A9%FA%26S%D4%D3%21%A1%EAi7h%9B%9A%2B%BF%60%22%C5WX%E1%ADL%80%E8V%3C%C6%A8%DBH%2632%18%A8x%01%08%21%8DS%0B%C8%AF%96KO%CA2%B0%F1%BD%1Du%A0%86%05%92s%B0%92%C4Bc%F1w%24S%85%09%09C%AE%24%90'


def check_cookies(url):
    response = requests.get(url, auth=(USERNAME, PASSWORD))

    cookies = response.cookies
    print(f"{cookies=}")
    for cookie in cookies:
        print(cookie.name, cookie.value)

    return cookies.get('info')


def traverse_url(url_key: str, num_items: int):
    cookies = b""
    visited_urls = []
    for i in range(num_items):
        url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={url_key}"
        print(f"{url=}")

        # Search for digits at end of string
        re_pattern = r"\d+$"

        info_cookie = check_cookies(url)
        cookies += info_cookie.encode()
        print(f"{cookies=}")

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


def decode_bz2(bytes_string):
    decompressed_str = bz2.decompress(bytes_string)

    return decompressed_str


def xmlrpc_get_methods(url):

    xml_request = """<?xml version="1.0"?>
    <methodCall>
        <methodName>system.methodSignature</methodName>
    <params>
        <param><value><string>phone</string></value></param>
    </params>
    </methodCall>
    """

    response = requests.post(
        url, data=xml_request, headers={"Content-Type": "text/xml"}
    )

    if response.status_code == 200:
        print(response.content)


def main():
    get_image_metadata(LEVEL_IMAGE)

    # Seem to be no cookies for this level
    check_cookies("http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=12345")

    # traverse_url("12345", 400)

    # url='http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing=83051'
    # Failed to find the next key. Page body: that's it.

    # Cookie of 83051: 

    # The 'busynothings' seem to have cookies.
    # Cookie title: 90
    # Cookie title: h

    # Cookies for the busynothings seem to be alpha chars
    # They look like a bz2 encoded string!

    decoded_string = urllib.parse.unquote_to_bytes(ENCODED_STRING)

    output = decode_bz2(decoded_string)
    print(f"{output=}")

    parse_xml(XML_URL, MOZART_FATHER)

    xmlrpc_get_methods(XML_URL)

    get_image_metadata("data/level_17/input/leopold.jpg")

    cookies = {"info": "the flowers are on their way"}

    response = requests.get(LEOPOLD_URL, cookies=cookies)
    print(response.text)


if __name__ == "__main__":
    main()
