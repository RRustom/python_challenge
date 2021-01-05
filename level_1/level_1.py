alphabet = "abcdefghijklmnopqrstuvwxyz"

ciphertext = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

url = "map"

plaintext = ""

for letter in url:
    if letter.isalpha():
        new_letter_index = (ord(letter) - 95) % 26 #shifted by 2
        plaintext += alphabet[new_letter_index]
    else:
        plaintext += letter

print(plaintext)

# solution: http://wiki.pythonchallenge.com/index.php?title=Level1:Main_Page
