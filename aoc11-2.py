instr = 'vzbxkghb'
errors = ['i','l','o']
def isValidPassword(s):
    incStraight = any( ord(s[i])+2 == ord(s[i+1])+1 == ord(s[i+2] 
                      ) for i in range( len(s)-2 ) )
    twoPairs = any( True for i in range(len(s)-3) if s[i]==s[i+1]
                    for j in range(i+2,len(s)-1) if s[j]==s[j+1]
                     )
    return incStraight and twoPairs

def nextCorrectLettersPassword(l):
    for i in range(-1,-1-len(l),-1):
        if l[i]!='z':
            l[i] = chr(ord(l[i])+( 2 if l[i] in errors else 1))
            return l
        else:
            l[i] = 'a'
    return ['a'] + l

inList= list(instr)
while not isValidPassword(inList):
    inList = nextCorrectLettersPassword(inList)
print(''.join(inList))
inList = nextCorrectLettersPassword(inList)
while not isValidPassword(inList):
    inList = nextCorrectLettersPassword(inList)
print(''.join(inList))

        
