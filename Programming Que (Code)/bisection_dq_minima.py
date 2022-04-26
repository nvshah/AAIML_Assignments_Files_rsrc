import math

def fun1(x):
    '''cos(x) - sin(x)
        between 0 -> 1 decreases from pos -> neg
    '''
    return math.cos(x) - math.sin(x)

def fun2(x):
    '''x^5 - x^4 +2*x^3 - x^2 + 3'''
    return x**5 - x**4 + 2*x**3 - x**2 + 3

def bisect_and_find(s, e, f):
    '''
    Optima - Minima Problem (betn interval [s, e])
    find near to zero (precise upto 3 decimal places) for f(x) [not slope i.e derivative of f(x)]
    i.e If we find slopeF(x) = 0 then it will be soln to derivative (i.e optima - maxima/minima)
    But here we are only finding if f(x) -> near to -> 0
    '''
    while True:
        m = (s + e) / 2  # We need float val
        res = f(m)
        if abs(res) <= 0.001 : # -0.001 <= f <= 0.001
            break 
        if res > 0: # adjust start
            s = m 
        else:
            e = m   # adjust end
    return m

ans = bisect_and_find(0, 1, fun1)

print(ans)



