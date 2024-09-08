from urllib import request
import re


# level url: http://www.pythonchallenge.com/pc/def/linkedlist.php

# Hint from page source: <!-- urllib may help. DON'T TRY ALL NOTHINGS, since
# it will never end. 400 times is more than enough. -->

url_key = '12345'

def traverse_url(url_key):
    for i in range(400):
        url = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={url_key}'
        print(f'{url=}')

        # Search for digits at end of string
        re_pattern = r'\d+$'

        with request.urlopen(url) as page:
            page_text = page.read(300).decode('utf-8')

            m = re.search(re_pattern, page_text)
            url_key = m.group(0)


def main():
    traverse_url(url_key)


if __name__ == "__main__":
    main()
