import time
import loader

class RTranslator:
    def __init__(self, lines):
        self.d = []
        for line in lines:
            words = line.split('=>')
            self.d.append( ( words[1].strip(), words[0].strip() ) )
    def transform(self, string):
        for i in range(len(string)):
            for change in self.d:
                if string[i:].startswith( change[0] ):
                    yield string[:i] + change[1] + string[i+len(change[0]):]

instr = loader.loadInput( 19 )
lines = instr.split('\n')
translator = RTranslator(lines[:-3])
formula = lines[-2]


variants = set([formula])
step = 0
start = time.process_time()
while True:
    step += 1
    newVariants = set()
    for variant in variants:
        newVariants |= set(formula for formula in translator.transform(variant))
    variants = newVariants
    print(step,len(variants))
    if 'e' in variants:
        print(step)
        break
print(time.process_time()-start)
        

#print(len(set(variant for variant in translator.transform(formula))))

