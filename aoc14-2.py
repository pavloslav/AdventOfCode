import requests
request = requests.get( 'http://adventofcode.com/day/14/input',
                   cookies = {'session':'53616c7465645f5f1f67ff685d72b6b7cc9c32e892bf4f09b44422b5ed91dff733905aaf35fa7d6895554ad0f8bfd069'}
                      )
instr = request.content.decode()

class Deer:
    def __init__(self, name, speed, flight, rest):
        self.name   = name
        self.speed  = speed
        self.flight = flight
        self.rest   = rest
        self.distance = 0
        self.lead     = 0

deers = []
time = 2503
maxDist = 0

for line in instr.split('\n'):
    #Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
    #  0    1   2   3   4   5   6   7       8   9    10   11   12  13   14
    words = line.split()
    if len(words) < 15:
        break
    name   = words[0]
    speed  = int( words[ 3] )
    flight = int( words[ 6] )
    rest   = int( words[13] )
    deers.append( Deer( name, speed, flight, rest ) )

for second in range(0,time):
    for deer in deers:
        if second%(deer.flight+deer.rest)<deer.flight:
            deer.distance += deer.speed
    maxDistance = max(deer.distance for deer in deers)
    for deer in deers:
        if deer.distance == maxDistance:
            deer.lead += 1

maxLead = max(deer.lead for deer in deers)
print( maxLead )
    
