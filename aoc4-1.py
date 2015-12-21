import hashlib
import binascii

instr = 'ckczppom'
count = 6

for order in range(0,7):
    for i in range(10**order,10**(order+1)):
        md5 = hashlib.md5()
        md5.update((instr+str(i)).encode())
        if binascii.hexlify(md5.digest()).startswith(b'0'*count):
            print(i, binascii.hexlify(md5.digest()))
            break
    else:
        print("No answer in range "+str(order))
