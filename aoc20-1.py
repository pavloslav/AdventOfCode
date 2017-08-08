def sumOfDivisors(n):
    s = 0
    i = 2
    while i*i <= n:
        if n % i ==0:
            s += i
            if i*i!= n:
                s += n//i
        i += 1
    return s + 1 + n

def solution( minNumber ):
    sumDivisors = minNumber / 10
    report = 1
    for i in range( 1,int(sumDivisors) + 1 ):
        if i%report == 0:
            print('Checking',i)
            report *= 10
        if sumOfDivisors(i) >= sumDivisors:
            return i
    return int(sumDivisors)

print(solution(34000000))
        
    
