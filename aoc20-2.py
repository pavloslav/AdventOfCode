def sumOfDivisors(n):
    s = 0
    i = max((n+1)//50,2)
    while i*i <= n:
        if n % i ==0:
            s += i
            other = n//i
            if other < i and other > (n+1)//50:
                s += n//i
        i += 1
    if s <= 50:
            s += 1
    return s + n

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
        
    
