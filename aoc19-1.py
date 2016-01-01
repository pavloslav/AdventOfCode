import time
import loader

class Translator:
    def __init__(self, lines):
        self.d = {}
        for line in lines:
            words = line.split('=>')
            self.d[words[0].strip()] = words[1].strip()
    def transform(self, string):
        for i in range(len(string)):
            for molecule in self.d.keys():
                if string[i:].startswith( molecule ):
                    yield string[:i] + self.d[molecule] + string[min(len(string),i+len(molecule)):]

instr = loader.loadInput( 19 )
lines = instr.split('\n')
translator = Translator(lines[:-3])
formula = lines[-1]

print(len(set(variant for variant in translator.transform(formula))))
