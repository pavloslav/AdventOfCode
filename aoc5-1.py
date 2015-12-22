import requests
request = requests.get( 'http://adventofcode.com/day/5/input',
                   cookies = {'session':'53616c7465645f5f1f67ff685d72b6b7cc9c32e892bf4f09b44422b5ed91dff733905aaf35fa7d6895554ad0f8bfd069'}
                   )
instr = request.content.decode()
good = 0
for line in instr.split():
    has3Vowels = ( sum(line.count(vowel) for vowel in 'aeiou')>=3 )
    hasDouble  = any(line[i]==line[i+1] for i in range(len(line)-1))
    hasNoBad   = all(bad not in line for bad in ['ab','cd','pq','xy'])
    if has3Vowels and hasDouble and hasNoBad:
        good += 1
print(good)
