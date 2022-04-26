def combination(l, r):
    '''
    Find Combination using Recurrsion
     :param : l -> list
     :r : r -> num of elements to pick
    '''
    assert len(l) >= r, "Length of l must be >= r" 
    
    # base Case i.e when to select = 1 => select all
    if r == 1:
        return [[e] for e in l]
    if len(l) == r:
        return [l]

    ans = []
    
    for i in range(len(l)-r+1):
        rest_comb = combination(l[i+1:], r-1)
        ans.extend([[l[i], *c] for c in rest_comb])

    return ans 

l = [1,2,3,4]
c = combination(l, 3)
print(c)

    