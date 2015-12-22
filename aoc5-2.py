import re
import requests
request = requests.get( 'http://adventofcode.com/day/5/input',
                   cookies = {'session':'53616c7465645f5f1f67ff685d72b6b7cc9c32e892bf4f09b44422b5ed91dff733905aaf35fa7d6895554ad0f8bfd069'}
                   )
instr = request.content.decode()
good = 0
for line in instr.split():
    has2pairs = any(line.count(line[i:i+2])>=2 for i in range(len(line)-1))
    hasRepeat = re.search(r'([A-Za-z]).\1',line) != None
    if has2pairs and hasRepeat:
        good += 1
    else:
        print(line, end=' ')
        if has2pairs:
            for i in range(len(line)-1):
                if line.count(line[i:i+2])>=2:
                    print(line[i:i+2],end=' ')
        print(has2pairs,hasRepeat)
print(good)
