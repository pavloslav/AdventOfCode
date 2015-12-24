import requests
request = requests.get( 'http://adventofcode.com/day/7/input',
                   cookies = {'session':'53616c7465645f5f1f67ff685d72b6b7cc9c32e892bf4f09b44422b5ed91dff733905aaf35fa7d6895554ad0f8bfd069'}
                   )
instr = request.content.decode()

wires = {}
connections = instr.split('\n')
for line in connections:
    try:
        operation, target = line.split(' -> ')
        wires[target.strip()] = operation.strip()
    except:
        pass

def calculate( expr ):
    try:
        return int(expr)
    except:
        parts = expr.split(' ')
        if len(parts) == 1: #один ідентифікатор
            if type(wires[parts[0]]) == int:
                return wires[parts[0]]
            else:
                wires[parts[0]] = calculate(wires[parts[0]])
                return wires[parts[0]]
        elif len(parts) == 2: #унарний оператор один - NOT
            if parts[0] != 'NOT':
                raise 'ERROR!' + parts[0]
            return ~calculate(parts[1])
        else: #бінарний оператор
            op1 = calculate(parts[0])
            op2 = calculate(parts[2])
            if   parts[1] == 'AND':
                return op1 & op2
            elif parts[1] == 'OR':
                return op1 | op2
            elif parts[1] == 'LSHIFT':
                return op1 << op2
            elif parts[1] == 'RSHIFT':
                return op1 >> op2
            else:
                raise 'ERROR ' + parts[1]

print(calculate('a'))
