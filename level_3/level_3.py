import re

# scan for 3 upper case, 1 lower case, 3 upper case. Add the line before
# and line after. Then inspect.
# One small letter, surrounded by EXACTLY three big bodyguards on each of its sides.

text_file = open("level_3.txt", "r")
text_lines = text_file.readlines()

small_letters = []

for i in range(len(text_lines)):
    if i > 0 and i < len(text_lines) - 2:
        current_line = text_lines[i]
        previous_line = text_lines[i-1]
        next_line = text_lines[i+1]

        small_letter_match = re.search(r"([a-z]{1}|\b)[A-Z]{3}[a-z][A-Z]{3}([a-z]{1}|\b)", current_line)

        if small_letter_match:
            start_index = small_letter_match.start()
            small_letter_index = start_index + 4
            small_letter = current_line[small_letter_index]
            small_letters.append(small_letter)

text_file.close()

print("".join(small_letters))
# linkedlist
