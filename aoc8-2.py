import requests
request = requests.get( 'http://adventofcode.com/day/8/input',
                   cookies = {'session':'53616c7465645f5f1f67ff685d72b6b7cc9c32e892bf4f09b44422b5ed91dff733905aaf35fa7d6895554ad0f8bfd069'}
                   )
instr = request.content.decode()
result = sum(line.count('\\')+line.count('"')+2 for line in instr.split('\n') if len(line)>0)

    

print(result)
