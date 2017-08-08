import time
import loader

class Translator:
    def __init__(self, lines):
        self.d = []
        for line in lines:
            words = line.split('=>')
            self.d.append( ( words[0].strip(), words[1].strip() ) )
    def transform(self, string):
        for i in range(len(string)):
            for change in self.d:
                if string[i:].startswith( change[0] ):
                    yield string[:i] + change[1] + string[i+len(change[0]):]

instr = loader.loadInput( 19 )
lines = instr.split('\n')
translator = Translator(lines[:-3])
formula = lines[-2]

print(len(set(variant for variant in translator.transform(formula))))

