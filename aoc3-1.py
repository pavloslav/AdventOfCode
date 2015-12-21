import requests
request = requests.get( 'http://adventofcode.com/day/3/input',
                   cookies = {'session':'53616c7465645f5f1f67ff685d72b6b7cc9c32e892bf4f09b44422b5ed91dff733905aaf35fa7d6895554ad0f8bfd069'}
                   )
instr = request.content.decode()
location = (0,0)
visited = set([location])
print(visited)
arrows = {'<':(-1, 0),
          '>':( 1, 0),
          '^':( 0, 1),
          'v':( 0,-1)}
for dir in instr:
    location = tuple(location[i]+arrows[dir][i] for i in range(2))
    visited.add( location )
print(len(visited))
