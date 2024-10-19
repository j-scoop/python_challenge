import requests
# import xmlrpc.client  # I believe this is the intended library but it doesn't work


# level url: http://www.pythonchallenge.com/pc/return/disproportional.html
# level title: "call him"
# level text: "phone that evil"
# level picture is close up of old mobile phone buttons
# Clicking the number 5 button takes to:
# http://www.pythonchallenge.com/pc/phonebook.php

# Could the numbers/letters of 'evil' have something to do with it?
# to spell evil on phone: "3845"
# Or, to type exactly, press: "33, 888, 444, 555"
# Maybe we post either of these numbers to the phonebook xml?

PHONE_NUMBER = 3845
XML_URL = "http://www.pythonchallenge.com/pc/phonebook.php"

# Think we need to 'post' to the xml url?


def parse_xml(url):

    xml_request = """<?xml version="1.0"?>
    <methodCall>
    <methodName>phone</methodName>
    <params>
        <param>
            <value><string>Bert</string></value>
        </param>
    </params>
    </methodCall>
    """

    response = requests.post(
        url,
        data=xml_request,
        headers={"Content-Type": "text/xml"}
    )

    if response.status_code == 200:
        print(response.content)

    # with xmlrpc.client.ServerProxy(url) as client:

    #     try:
    #         result = client.call(PHONE_NUMBER)
    #         print(f"{result=}")
    #     except xmlrpc.client.Fault as err:
    #         print(f"An error occurred: {err}")


def main():
    parse_xml(XML_URL)


if __name__ == "__main__":
    main()
