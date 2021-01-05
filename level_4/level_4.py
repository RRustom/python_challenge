import urllib.request
import re

next_number = 72758 # 16044 # 44827

for i in range(400):
    with urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d' % next_number) as f:
        res = f.read().decode('utf-8')
        # if i > 80:
        print("i: ", i)
        print(res)
        next_number = int("".join(re.findall(r"\d", res)))
        #next_number //= 2
        print('next: ', next_number)

# peak.html
