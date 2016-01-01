import time
import requests
request = requests.get( 'http://adventofcode.com/day/17/input',
                   cookies = {'session':'53616c7465645f5f1f67ff685d72b6b7cc9c32e892bf4f09b44422b5ed91dff733905aaf35fa7d6895554ad0f8bfd069'}
                      )
instr = request.content.decode()

bottles = [int(size) for size in instr.split('\n') if size!='']

def calculateVolume(bottles, count):
    return sum( bottles[j] for j in range(len(bottles)) if (count & (1<<j)) !=0 )
 
def calculateCombinations(bottles, volume):
    return sum( 1 for i in range(2**len(bottles)) if calculateVolume(bottles,i)==150 )
start = time.process_time()

print( calculateCombinations(bottles, 150) )
print( time.process_time()-start,'seconds passed')
