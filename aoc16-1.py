import requests
request = requests.get( 'http://adventofcode.com/day/16/input',
                   cookies = {'session':'53616c7465645f5f1f67ff685d72b6b7cc9c32e892bf4f09b44422b5ed91dff733905aaf35fa7d6895554ad0f8bfd069'}
                      )
instr = request.content.decode()

sues = []

for line in instr.split('\n'):
    if len(sues)>=500:
        break
    name, rest = line.split(':',1)
    d = {}
    for dna in rest.split(','):
        type, count = dna.split(':')
        d[type.strip()] = int(count)
    sues.append({'name':name, 'dna': d})

needed = {  'children': 3,
            'cats': 7,
            'samoyeds': 2,
            'pomeranians': 3,
            'akitas': 0,
            'vizslas': 0,
            'goldfish': 5,
            'trees': 3,
            'cars': 2,
            'perfumes': 1 }

results = []

for aunt in sues:
    suits = True
    for fact in needed.keys():
        try:
            if aunt['dna'][fact] != needed[fact]:
                suits = False
        except:
            pass
    if suits:
        results.append(aunt['name'])

print(results)
        
