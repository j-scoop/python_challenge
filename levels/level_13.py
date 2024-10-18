import requests


# level url: http://www.pythonchallenge.com/pc/return/disproportional.html
# level title: "call him"
# level text: "phone that evil"
# level picture is close up of old mobile phone buttons
# Clicking the number 5 button takes to:
# http://www.pythonchallenge.com/pc/phonebook.php
#
XML_URL = "http://www.pythonchallenge.com/pc/phonebook.php"

# Think we need to 'post' to the xml url?

def parse_xml(url):
    username = "huge"
    password = "file"
    response = requests.get(url, auth=(username, password))

    if response.status_code == 200:
        print(response.content)


def main():
    parse_xml(XML_URL)


if __name__ == "__main__":
    main()
