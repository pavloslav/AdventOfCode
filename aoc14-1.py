import requests
request = requests.get( 'http://adventofcode.com/day/14/input',
                   cookies = {'session':'53616c7465645f5f1f67ff685d72b6b7cc9c32e892bf4f09b44422b5ed91dff733905aaf35fa7d6895554ad0f8bfd069'}
                      )
instr = request.content.decode()

deers = []
time = 2503
maxDist = 0

for line in instr.split('\n'):
    #Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    #  0    1   2   3   4   5   6   7       8   9    10   11   12  13   14
    words = line.split()
    if len(words) < 15:
        break
    speed  = int( words[ 3] )
    flight = int( words[ 6] )
    rest   = int( words[13] )
    distance = 0
    deerTime = 0
    while True:
        if deerTime + flight >= time:
            distance += ( time - deerTime ) * speed
            break
        else:
            distance += flight * speed
            deerTime += flight
        if deerTime + rest >= time:
            break
        else:
            deerTime += rest
    maxDist = max( distance, maxDist )
print( maxDist )
    
