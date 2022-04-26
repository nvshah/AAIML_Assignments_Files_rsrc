from math import exp, log


def pow_scratch(a, b):
    def a1():
        return round(exp(b*log(a)))

    def a2(a, b):
        '''
        Approach :- using Recurrsion (Divide & Conquer)
        T.C :- logarithmic (log(n))

        NOTE :- pow() & log() are correlated to each other (probably inverse of each other)
        '''
        if a == 0: return 0
        if b == 0: return 1
        if b == 1: return a

        q, r = divmod(b, 2)

        half = a2(a, q)  # calc half

        # in case if remainder left (ie one x is yet left to be multiplied)
        # eg 3^5 = 3 * 3^4 * 3^4
        return a*half*half if r else half*half


if __name__ == '__main__':
    a, b = 1, 10
    ans = pow_scratch(a,b)
    print(ans)