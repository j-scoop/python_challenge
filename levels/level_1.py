import string


level_url = 'http://www.pythonchallenge.com/pc/def/map.html'

in_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

x = string.ascii_lowercase
y = x[2:] + x[:2]

print(f'{x=}')
print(f'{y=}')

# K -> M
# O -> Q
# E -> G

map_table = in_string.maketrans(x, y)

print(in_string.translate(map_table))
