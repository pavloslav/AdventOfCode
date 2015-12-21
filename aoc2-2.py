import operator
import requests
request = requests.get( 'http://adventofcode.com/day/2/input',
                   cookies = {'session':'53616c7465645f5f1f67ff685d72b6b7cc9c32e892bf4f09b44422b5ed91dff733905aaf35fa7d6895554ad0f8bfd069'}
                   )
instr = request.content.decode()
ribbon = 0
for line in instr.split():
    dims = sorted([int(length) for length in line.split('x')])
    volume = 1
    for dim in dims:
        volume *= dim
    ribbon += 2*sum(dims[:-1])+ volume
print(ribbon)
