import re
import numpy as np
from PIL import Image

text_file = open("level_2.txt", "r")

output_file = open("level_2_clean.txt", 'w+')


#ocr_image = np.asarray(Image.open('ocr.jpg'))

#print(ocr_image) (480, 640, 3)

pixels = []

characters = []

for line in text_file:
    for char in line:
        if char not in characters:
            characters.append(char)
    clean = re.sub(r'[%$@_^#\)&!+\[\]\(\{\}*]+',' ',line)
    output_file.write(clean)
    # row = []
    # for j in range(0, len(line), 3):
    #     row.append([ord(char) for char in line[j:j+3]])
    # for char in line:
    #     pixels.append(ord(char))
#     pixels.append(row)
#
# print(pixels)
#
# array = np.array(pixels, dtype=np.uint8)
# # (32922, 3)
#
# print(array.shape)
#
# new_image = Image.fromarray(array)
# new_image.save('level_2.png')

print(characters)
