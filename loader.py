import requests

def loadInput( number ):
    cookies = {}
    with open('settings.ini') as f:
        while True:
            line = f.readline()
            if line == '':
                break
            try:
                name, value = line.split( ':', 1 )
                cookies[name.strip()] = value.strip()
            except:
                pass
            
    response = requests.get( 'http://adventofcode.com/day/%d/input' % number,
                   cookies = cookies
                      )
    if response.status_code != 200:
        raise Exception('Request result code is ' + str(response.status_code))
    
    return response.content.decode()

