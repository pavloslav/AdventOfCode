instr = "3113322113"

for i in range(50):
    res = ''
    last = instr[0]
    count = 1
    for i in range(1,len(instr)):
        if instr[i] == last:
            count += 1
        else:
            res += str(count) + last
            last = instr[i]
            count = 1
    res += str(count) + last
    instr = res
    if len(instr) < 100:
        print(instr)

print(len(instr))
