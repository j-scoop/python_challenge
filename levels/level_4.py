from urllib import request
import re
import sys


# level url: http://www.pythonchallenge.com/pc/def/linkedlist.php

# Hint from page source: <!-- urllib may help. DON'T TRY ALL NOTHINGS, since
# it will never end. 400 times is more than enough. -->

# url_key = '12345'  # Initial url

# Stopped at url_key = 16044:
# url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=16044'
# Failed to find the next key. Page body: Yes. Divide by two and keep going.
# url no.2:  16044/2 = 8022
url_key = "8022"  # 2nd URL

# Stopped at url_key = 66831:
# url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=66831'
# Failed to find the next key. Page body: peak.html


def traverse_url(url_key):
    for i in range(400):
        url = f"http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={url_key}"
        print(f"{url=}")

        # Search for digits at end of string
        re_pattern = r"\d+$"

        with request.urlopen(url) as page:
            page_text = page.read(300).decode("utf-8")

            m = re.search(re_pattern, page_text)
            if m:
                url_key = m.group(0)
            else:
                print(f"Failed to find the next key. Page body: {page_text}")
                sys.exit()


def main():
    traverse_url(url_key)


if __name__ == "__main__":
    main()
