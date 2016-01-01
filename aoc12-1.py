import json
import requests
request = requests.get( 'http://adventofcode.com/day/12/input',
                   cookies = {'session':'53616c7465645f5f1f67ff685d72b6b7cc9c32e892bf4f09b44422b5ed91dff733905aaf35fa7d6895554ad0f8bfd069'}
                      )
instr = request.content.decode()

data = json.loads(instr)

def recursiveSum(d):
    if type(d) == dict:
        return sum( recursiveSum(val) for val in d.values() )
    elif type(d) == list:
        return sum( recursiveSum(val) for val in d )
    elif type(d) in [int,float]:
        return d
    else:
        return 0

print(recursiveSum(data))
        
