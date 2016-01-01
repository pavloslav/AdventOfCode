import itertools
import requests
request = requests.get( 'http://adventofcode.com/day/13/input',
                   cookies = {'session':'53616c7465645f5f1f67ff685d72b6b7cc9c32e892bf4f09b44422b5ed91dff733905aaf35fa7d6895554ad0f8bfd069'}
                      )
instr = request.content.decode()

happy = {}
persons = set()

for line in instr.split('\n'):
    #David would gain 41 happiness units by sitting next to Carol.
    #  0     1     2   3     4       5    6    7      8   9   10
    words = line[:-1].split() #викидаємо '.'
    if len(words)<11:
        break
    happy[(words[0],words[10])] = int(words[3]) if words[2]=='gain' else -int(words[3])
    persons.add(words[0])

print(
      max(
          sum(
              happy[(places[i],places[i-1])]+happy[(places[i-1],places[i])] for i in range(len(places))
              ) for places in itertools.permutations(persons)
          )
     )
        
