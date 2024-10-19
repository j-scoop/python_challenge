import requests
# I believe xmlrpc is the intended library but it doesn't work
# import xmlrpc.client


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

# From the previous level, Bert is evil - maybe we call him?

EVIL = "Bert"
XML_URL = "http://www.pythonchallenge.com/pc/phonebook.php"


def parse_xml(url):

    xml_request = f"""<?xml version="1.0"?>
    <methodCall>
    <methodName>phone</methodName>
    <params>
        <param>
            <value><string>{EVIL}</string></value>
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

    # Failing xmlrpc implementation below:
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
