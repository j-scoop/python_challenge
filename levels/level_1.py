import string


# level url: http://www.pythonchallenge.com/pc/def/map.html

source_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# Hint from the level below (letters are shifted by two places?)
# K -> M
# O -> Q
# E -> G


def translate(in_string):
    alpha_chars = string.ascii_lowercase
    alpha_shifted = alpha_chars[2:] + alpha_chars[:2]

    print(f"{alpha_chars=}")
    print(f"{alpha_shifted=}")

    map_table = in_string.maketrans(alpha_chars, alpha_shifted)

    translated = in_string.translate(map_table)

    return translated


def main():
    print(translate(source_string))


if __name__ == "__main__":
    main()
