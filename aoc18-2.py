import time
import copy

import requests
request = requests.get( 'http://adventofcode.com/day/18/input',
                   cookies = {'session':'53616c7465645f5f1f67ff685d72b6b7cc9c32e892bf4f09b44422b5ed91dff733905aaf35fa7d6895554ad0f8bfd069'}
                      )
instr = request.content.decode()

lights = []
for line in instr.split('\n'):
    if line.strip() == '':
        break
    lightsLine = []
    for c in line:
        lightsLine.append(0 if c == '.' else 1)
    lights.append(lightsLine)
lights[ 0][ 0] = 1
lights[ 0][-1] = 1
lights[-1][ 0] = 1
lights[-1][-1] = 1

def sumNeibours(lights,x,y):
    s = -lights[x][y]
    for i in range(max(0,x-1),min(len(lights[x]),x+2)):
        for j in range(max(0,y-1),min(len(lights),y+2)):
            s += lights[i][j]
    return s

def step(lights):
    newLights = copy.deepcopy(lights)
    for i in range(len(lights)):
        for j in range(len(lights[i])):
            s = sumNeibours(lights,i,j)
            if s == 3:
                newLights[i][j] = 1
            elif s!=2:
                newLights[i][j] = 0
    newLights[ 0][ 0] = 1
    newLights[ 0][-1] = 1
    newLights[-1][ 0] = 1
    newLights[-1][-1] = 1
    return newLights

start = time.process_time()

for i in range(100):
    lights = step(lights)


s = sum( light for line in lights for light in line )

end = time.process_time()-start

print( s )
print( end,'seconds passed')
