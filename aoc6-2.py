import requests
request = requests.get( 'http://adventofcode.com/day/6/input',
                   cookies = {'session':'53616c7465645f5f1f67ff685d72b6b7cc9c32e892bf4f09b44422b5ed91dff733905aaf35fa7d6895554ad0f8bfd069'}
                   )
instr = request.content.decode()

lights = [ [0]*1000 for i in range(1000) ]

for command in instr.split('\n'):
    if command.startswith('turn'):
        command = command[5:]
    command = command.split(' ')
    if len(command)<4:
        break
    (x1,y1) = map( int, command[1].split(',') )
    (x2,y2) = map( int, command[3].split(',') )
    for x in range(x1,x2+1):
        for y in range(y1,y2+1):
            lights[x][y] += ( 1 if command[0] == 'on' else
                             ( -1 if command[0] == 'off' else
                               2
                             )
                           )
            if lights[x][y]<0:
                lights[x][y] = 0

                           
print( sum( sum(lights[x]) for x in range(1000) ) )
                
        
        
