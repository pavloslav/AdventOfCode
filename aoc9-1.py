import itertools

import requests
request = requests.get( 'http://adventofcode.com/day/9/input',
                   cookies = {'session':'53616c7465645f5f1f67ff685d72b6b7cc9c32e892bf4f09b44422b5ed91dff733905aaf35fa7d6895554ad0f8bfd069'}
                      )
instr = request.content.decode()

distances = {}
cities    = set()
for line in instr.split('\n'):
    parts = line.split()
    #London to Dublin = 464
    #  0     1    2   3  4
    if len(parts) < 5:
        break;
    distances[(parts[0], parts[2])]=int(parts[4])
    distances[(parts[2], parts[0])]=int(parts[4])
    cities.add( parts[0] )
def printRoute(route):
    print( ','.join(route[i]+' to '+route[i+1]+' = '+str(distances[ (route[i],route[i+1]) ]) for i in range(len(route)-1)))    

'''
minlen = min(
             sum(
                 distances[ (route[i],route[i+1]) ]
                     for i in range( len(route) - 1 )
                 ) for route in itertools.permutations(cities)
             )
'''
results = []
minlen = 1000000
for route in itertools.permutations(cities):
    s = sum(distances[ (route[i],route[i+1]) ] for i in range(len(route)-1))
    results += [(s,route)]
    if s < minlen:
        minlen = s
        minres = route
print(sorted(results,key=lambda x:x[0]))

printRoute( minres )
print( minlen )
