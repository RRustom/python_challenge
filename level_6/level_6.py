import os
import re
import zipfile

directory = './channel'

files = os.listdir(path=directory)

start = '90052.txt'

visited = [start]
visited_files = ['readme.txt']
visited_numbers = [90052]

comments_file = open("level_6.txt", 'w+')

archive = zipfile.ZipFile('channel.zip', 'r')

def walk_files(file):
    file_path = os.path.join(directory, file)
    with open(file_path, "r") as f:
        lines = f.readlines()

        # skip_text = "Next nothing is"
        #
        # for line in lines:
        #     #if skip_text not in line:
        comment = archive.getinfo(file).comment
        comments_file.write(comment.decode("utf-8") )

        first_line = lines[0]

        next_number = "".join(re.findall(r"\d", first_line))

        if not next_number:
            return

        next_file = next_number + ".txt"
        visited.append(next_file)
        visited_numbers.append(int(next_number))
        visited_files.append("".join(re.findall(r"\d", file)))
        walk_files(next_file)

walk_files(start)



# visited_numbers.append("Collect the comments.")
#
# zipped = zip(visited_files, visited_numbers)
#
# print(list(zipped))

comments_file.close()

#46145

with open(os.path.join(directory, '46145.txt'), 'r') as f:
    print(f.read())

# Collect the comments.
