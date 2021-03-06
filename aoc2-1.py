import itertools
import requests
request = requests.get( 'http://adventofcode.com/day/2/input',
                   cookies = {'session':'53616c7465645f5f1f67ff685d72b6b7cc9c32e892bf4f09b44422b5ed91dff733905aaf35fa7d6895554ad0f8bfd069'}
                   )
instr = request.content.decode()
paper = 0
for line in instr.split():
    dims = [int(length) for length in line.split('x')]
    sizes = itertools.combinations(dims,2)
    areas = sorted( [ x*y for (x,y) in sizes ] )
    paper += 2*sum(areas)+areas[0]
print(paper)
